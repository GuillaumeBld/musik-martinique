#!/usr/bin/env python3
"""Sert la boîte à rythme (dossier site/) et un carnet de motifs partagés.

API :
  GET  /api/patterns  -> liste des motifs, le plus récent en premier
  POST /api/patterns  -> ajoute un motif {name, steps, bpm, swing, pattern}

Le carnet est un fichier JSON (PATTERNS_FILE, défaut /data/patterns.json).
Aucune dépendance hors bibliothèque standard.
"""
import json
import os
import re
import threading
import time
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
PATTERNS_FILE = os.environ.get('PATTERNS_FILE', '/data/patterns.json')
PORT = int(os.environ.get('PORT', '80'))

MAX_PATTERNS = 500          # au-delà, les plus anciens sortent du carnet
MAX_BODY = 16 * 1024        # un motif pèse moins d'un kilo-octet
NAME_RE = re.compile(r'^[\w\s\'’.\-!?àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ]{1,40}$')
TRACK_IDS = {
    'tanbouGrave', 'tanbouAigu', 'tambourBass', 'debonda', 'tibwa', 'chacha',
    'baril', 'siyak', 'cloche', 'lanbi', 'cuivres',
}

_lock = threading.Lock()


def _load():
    try:
        with open(PATTERNS_FILE, encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, ValueError):
        return []


def _save(items):
    os.makedirs(os.path.dirname(PATTERNS_FILE), exist_ok=True)
    tmp = PATTERNS_FILE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False)
    os.replace(tmp, PATTERNS_FILE)


def _validate(body):
    """Retourne (motif normalisé, None) ou (None, message d'erreur)."""
    if not isinstance(body, dict):
        return None, 'corps attendu : objet JSON'
    name = str(body.get('name', '')).strip()
    if not NAME_RE.match(name):
        return None, 'nom : 1 à 40 caractères (lettres, chiffres, espaces, ponctuation simple)'
    steps = body.get('steps')
    if steps not in (12, 16):
        return None, 'steps : 12 ou 16'
    bpm = body.get('bpm')
    if not isinstance(bpm, (int, float)) or not 50 <= bpm <= 200:
        return None, 'bpm : entre 50 et 200'
    swing = body.get('swing', 0)
    if not isinstance(swing, (int, float)) or not 0 <= swing <= 60:
        return None, 'swing : entre 0 et 60'
    pattern = body.get('pattern')
    if not isinstance(pattern, dict):
        return None, 'pattern : objet piste -> cases'
    clean = {}
    for track_id, line in pattern.items():
        if track_id not in TRACK_IDS:
            continue
        if not isinstance(line, list) or len(line) != steps:
            return None, f'pattern.{track_id} : {steps} cases attendues'
        if any(v not in (0, 1, 2) for v in line):
            return None, f'pattern.{track_id} : valeurs 0, 1 ou 2'
        clean[track_id] = line
    if not any(any(line) for line in clean.values()):
        return None, 'motif vide : rien à enregistrer'
    return {
        'id': f'{int(time.time() * 1000):x}',
        'name': name,
        'steps': steps,
        'bpm': int(bpm),
        'swing': int(swing),
        'pattern': clean,
        'created': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }, None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def log_message(self, fmt, *args):  # journal compact : méthode, chemin, statut
        print(f'{self.address_string()} {fmt % args}', flush=True)

    def _json(self, status, payload):
        data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.split('?')[0] == '/api/patterns':
            with _lock:
                items = _load()
            return self._json(HTTPStatus.OK, items)
        return super().do_GET()

    def do_POST(self):
        if self.path.split('?')[0] != '/api/patterns':
            return self._json(HTTPStatus.NOT_FOUND, {'error': 'inconnu'})
        length = int(self.headers.get('Content-Length') or 0)
        if length <= 0 or length > MAX_BODY:
            return self._json(HTTPStatus.BAD_REQUEST, {'error': 'corps absent ou trop grand'})
        try:
            body = json.loads(self.rfile.read(length).decode('utf-8'))
        except ValueError:
            return self._json(HTTPStatus.BAD_REQUEST, {'error': 'JSON invalide'})
        item, error = _validate(body)
        if error:
            return self._json(HTTPStatus.BAD_REQUEST, {'error': error})
        with _lock:
            items = _load()
            items.insert(0, item)
            del items[MAX_PATTERNS:]
            _save(items)
        return self._json(HTTPStatus.CREATED, item)


if __name__ == '__main__':
    print(f'musik-martinique : site={SITE_DIR} carnet={PATTERNS_FILE} port={PORT}', flush=True)
    ThreadingHTTPServer(('0.0.0.0', PORT), Handler).serve_forever()

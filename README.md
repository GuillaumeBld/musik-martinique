# Musik Martinique

Boîte à rythmes martiniquaise, synthèse Web Audio pure — aucun échantillon à télécharger.

Onze timbres traditionnels sont fabriqués en direct par la Web Audio API (oscillateurs,
bruit filtré, enveloppes percussives), groupés par formation d'origine.

## Instruments

**Bèlè, chouval bwa, bal**

- `tanbouGrave` — Tanbou bèlè : fût de lattes de tonneau de rhum, peau de cabri, frappé à la main
- `tanbouAigu` — Tanbou répondeur : phalanges sur le bord de la peau
- `tambourBass` — Tambour di bass
- `debonda` — Tanbou débonda, tambour à deux faces du chouval bwa
- `tibwa` — deux baguettes de bois frappées sur le fût, le tempo de base du bèlè
- `chacha` — calebasse séchée remplie de graines

**Carnaval — groupes à pied**

- `baril` — Tanbou baril, fût de récupération, plus clair et plus mordant que le tanbou bèlè
- `siyak` — grande râpe de bois ou de métal grattée à la baguette
- `cloche` — métal de parade
- `lanbi` — Konn lanbi, conque servant autrefois de signal
- `cuivres` — trombone de défilé

**Bouyon — électro**

- `kickBouyon` — grosse caisse électronique
- `snareBouyon` — caisse claire électronique, claquante
- `contretemps` — charley ouvert sur le « et » de chaque temps (bouyon, zouk)

## Rythmes

Bèlè — tak pi tak pi tak tak (3 temps), Bèlè (2 temps), Beliyà / Gran bèlè (3 temps),
Danmyé / Ladja, Chouval bwa, Biguine, Mazouk créole (3 temps), Zouk, Vidé / Karnaval,
Groupe à pied, Bouyon (2 temps, 160 BPM, kick électro sur la roulade du lapo kabwit).

**D'après des morceaux connus** (pulsation batterie seulement, ni mélodie ni paroles ni relevé
exact) : Kassav' « Zouk la sé sel médikaman nou ni » et « Syé bwa », Béroard & Lavil « Kolé
séré », Kali « Monté la riviè », Malavoi « Caressé mwen », Eugène Mona « Bwa brilé », Dédé
Saint-Prix « Mi sé sa », Plastic System Band (vidé).

La grille s'adapte à la mesure : 16 pas en deux temps, 12 pas en trois temps
(beliyà, gran bèlè et mazouk sont à trois temps).

Le tibwa porte la formule de base du bèlè, **tak pi tak pi tak tak** : dans les motifs, `x`
est un coup fort (tak) et `p` un coup léger (pi). La formule chantée s'affiche sous les
commandes quand un style la porte.

## Commandes

- `Espace` — lecture / pause
- clic sur une case — tak (fort), second clic — pi (léger), troisième — silence ; chaque clic pré-écoute
- touches `1` … `0` `-` — jouer les pistes au clavier (`Maj` pour un coup léger)
- `M` sur une piste — couper
- tempo, swing, volume général, volume et sourdine par piste
- le motif courant reste en mémoire dans le navigateur (localStorage)

## Carnet partagé

Un motif peut être enregistré sous un nom ; il devient visible par tous les visiteurs de la
page et se recharge d'un clic (mesure, tempo, swing, cases).

- `GET /api/patterns` — liste, le plus récent en premier (500 au maximum, les plus anciens sortent)
- `POST /api/patterns` — `{ name, steps (12|16), bpm, swing, pattern: { piste: [0|1|2, …] } }`

Le carnet est un fichier JSON sur le volume `patterns` (`/data/patterns.json`). Il n'y a
ni compte ni suppression : c'est un cahier ouvert.

## Sons : échantillons ou synthèse

Interrupteur dans la barre de commandes. En mode **Échantillons** (défaut), dix pistes jouent
de vrais enregistrements (`site/samples/*.mp3`, mono, 96 kb/s, moins de 1,2 s) : tablas pour
les tanbou, toms pour débonda et baril, cowbell, 808 et caisse claire pour le bouyon, cymbale
ouverte pour le contretemps. Plusieurs prises par instrument, tirées au hasard, avec un taux de
lecture ajusté. Chacha, siyak, lanbi et cuivres restent synthétisés (bruit et souffle).

Origine des fichiers : banque de Sonic Pi (`etc/samples`), échantillons Freesound placés dans
le domaine public (CC0). Conversion : `ffmpeg -t 1.2 -ac 1 -ar 44100 -b:a 96k`.

## Portée

Les timbres sont des synthèses qui cherchent le comportement des instruments, pas des
enregistrements. Les motifs sont des interprétations stylistiques, pas des transcriptions
du répertoire traditionnel.

## Déploiement

`server.py` (Python 3, bibliothèque standard seulement) sert `site/` et l'API. Sur VPS1, le
`docker-compose.yml` du dépôt branche le conteneur derrière Traefik sous
`rythme.madinina.cloud` (clone dans `/root/musik-martinique-deploy/repo`).

```sh
# en local
PATTERNS_FILE=/tmp/patterns.json PORT=8080 python3 server.py

# sur VPS1, après un push
cd /root/musik-martinique-deploy/repo && git pull && docker compose up -d --build
```

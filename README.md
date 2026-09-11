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

## Sons : uniquement des enregistrements

Il n'y a plus de synthèse. Chaque piste joue un ou plusieurs enregistrements
(`site/samples/*.mp3`, mono, 96 kb/s, moins de 1,2 s), tirés au hasard à chaque coup, avec
un taux de lecture ajusté (`rate`) et parfois une durée coupée (`cut`). La table `SAMPLES`
dans `site/index.html` fait foi. Le champ `role` de chaque piste dit ce qui est réellement
enregistré quand l'instrument martiniquais n'existe pas en licence libre.

Trente-six pistes, par famille :

- **Peaux — tambours traditionnels** : tanbou bèlè, tanbou répondeur, tambour di bass, tanbou
  débonda, tanbou baril, ka (gwoka)
- **Peaux — orchestre** : conga, tumbadora, quinto, bongos, timbales, djembé
- **Batterie** : grosse caisse 808, grosse caisse, caisse claire, tom, charley fermé, charley
  ouvert (contretemps)
- **Bois** : tibwa, ti-bwa bambou, claves
- **Métal** : cloche de carnaval, campana
- **Secoués et grattés** : chacha, siyak, güiro, shaker
- **Vents et appels** : konn lanbi, flûte des mornes, clarinette, saxophone, trompette, trombone
- **Cordes** : banjo, guitare, contrebasse

Les instruments mélodiques jouent une note fixe (do 4 pour clarinette, saxophone, trompette,
trombone ; do 5 pour la flûte ; do 4 et sol 3 pour le banjo ; mi 3 pour la guitare ; la 2
pincé pour la contrebasse). Les familles se replient d'un clic sur leur nom.

Sources et licences :

- `fs_conga_open`, `fs_tumba_open`, `fs_quinto_*`, `fs_bongo_*` : pack « Bongos and Conga Hits »
  de MrRentAPercussionist, Freesound, **CC BY 4.0**
  (https://freesound.org/people/MrRentAPercussionist/packs/25693/). Attribution en bas de page.
- `fs_conch` : « Conch.wav » de RoofDog, Freesound, **CC0** (https://freesound.org/s/78974/).
- `ph_*` : Philharmonia Orchestra sound samples (https://philharmonia.co.uk/resources/sound-samples/,
  miroir fichier par fichier : https://github.com/skratchdot/philharmonia-samples). Usage libre,
  y compris commercial ; interdiction de les revendre « en l'état » comme banque.
- autres (`bd_808`, `sn_dolf`, `drum_*`, `elec_wood`) : banque de Sonic Pi (`etc/samples`),
  échantillons Freesound placés dans le domaine public, **CC0**.

Conversion : `ffmpeg -t 1.2 -ac 1 -ar 44100 -af silenceremove,afade,alimiter -b:a 96k`.

Manque en licence libre, non trouvé : violon (Malavoi), accordéon (chouval bwa, mazurka),
et les vrais tanbou bèlè, tibwa, chacha, siyak. La voie propre reste d'enregistrer un tanbouyé
et de verser les coups dans `site/samples/`.

Banques explorées et écartées : le kit gwoka `matthCorvo/Mon-GWOKA-Drum-kit` (aucune licence,
sons apparemment extraits de vidéos), Wikimedia Commons (enregistrements d'ensemble, pas de
coups isolés). Aucun échantillon libre de tanbou bèlè, tibwa ou chacha martiniquais n'a été
trouvé : la voie propre serait d'enregistrer un tanbouyé et de verser les coups ici.

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

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

## Rythmes

Bèlè (2 temps), Beliyà / Gran bèlè (3 temps), Danmyé / Ladja, Chouval bwa, Biguine,
Mazouk créole (3 temps), Zouk, Vidé / Karnaval, Groupe à pied.

La grille s'adapte à la mesure : 16 pas en deux temps, 12 pas en trois temps
(beliyà, gran bèlè et mazouk sont à trois temps).

## Commandes

- `Espace` — lecture / pause
- clic sur une case — activer et pré-écouter
- `M` sur une piste — couper
- tempo, swing, volume général, volume et sourdine par piste

## Portée

Les timbres sont des synthèses qui cherchent le comportement des instruments, pas des
enregistrements. Les motifs sont des interprétations stylistiques, pas des transcriptions
du répertoire traditionnel.

## Deploy

Nginx sert `site/` en statique. Déployé via Dokploy sur `rythme.madinina.cloud`.

```sh
docker build -t musik-martinique .
docker run --rm -p 8080:80 musik-martinique
```

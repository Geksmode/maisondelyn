# Maison de Lyn

Site vitrine de Linh, maquilleuse de mariée à Paris. HTML et CSS statiques, publiés avec GitHub Pages depuis `main`.

- Français à la racine, anglais dans `en/` (mêmes noms de fichiers).
- Pages : `index`, `prestations`, `galerie`, `faq`, `contact`.
- Les pages sont générées par `build.py` : modifiez les textes dedans, puis lancez `python3 build.py .`

## Technologies
- Composants web natifs dans `components.js` : `<lyn-lightbox>` (visionneuse plein écran), `<lyn-book-button>` (bouton flottant mobile), `<lyn-quote-form>` (envoi du devis sans rechargement).
- Transitions entre pages (View Transitions API), apparitions pilotées par le défilement (`animation-timeline: view()`, repli JavaScript), `@starting-style`, container queries, `:has()`, `:user-invalid`, `field-sizing`.
- Les animations sont désactivées si l'appareil demande de réduire les mouvements.

## Formulaire
Le formulaire de `contact.html` utilise [Formspree](https://formspree.io) (gratuit). Créez un formulaire avec l'adresse e-mail de Linh, puis remplacez `VOTRE_ID` dans `build.py` et régénérez.

## Langues
Français à la racine, anglais dans `en/`, vietnamien dans `vi/`, coréen dans `ko/`. Les textes FR et EN sont dans `build.py`, les textes VI et KO dans `langues.py` (à faire relire par Linh). Après une modification des textes coréens, relancer `python3 polices.py` pour mettre à jour les caractères de la police coréenne.

## Photos
Les photos sources (2560 px) passent par `python3 images.py <dossier>` : chaque photo est déclinée en WebP de 640 à 2560 px, plus un JPEG de secours, et `img/manifest.json` est mis à jour. Relancer ensuite `python3 build.py .`.

## Sécurité et rapidité
- Politique de sécurité (CSP) dans chaque page : seules les ressources du site sont chargées et le formulaire n'envoie qu'à Formspree. Si un service externe est ajouté (vidéo, carte, statistiques), il faut l'autoriser dans `CSP` de `build.py`.
- Formulaire : longueurs limitées, champ piège `_gotcha` contre les robots, bouton désactivé pendant l'envoi.
- Pages suivantes préparées à l'approche d'un lien (Speculation Rules), transitions entre pages, polices et images servies par le site.
- `sitemap.xml` et `robots.txt` sont générés par `build.py`.

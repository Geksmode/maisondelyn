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

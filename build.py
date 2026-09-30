"""Génère le site Maison de Lyn (FR à la racine, EN dans en/).

Usage : python3 build2.py <dossier du dépôt>
"""
import os
import re
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
IG = "https://www.instagram.com/maisondelyn_mua/"
BASE = "https://geksmode.github.io/maisondelyn/"
NB = " "  # espace insécable

T = {
    "fr": {
        "nav": [("prestations.html", "Prestations"), ("galerie.html", "Galerie"), ("faq.html", "FAQ"), ("contact.html", "Contact")],
        "switch": ("EN", "English"),
        "book": "Prendre rendez-vous",
        "footer": "Maquillage de mariée, Paris",
        "close": "Fermer",
    },
    "en": {
        "nav": [("prestations.html", "Services"), ("galerie.html", "Gallery"), ("faq.html", "FAQ"), ("contact.html", "Contact")],
        "switch": ("FR", "Français"),
        "book": "Book an appointment",
        "footer": "Bridal make-up, Paris",
        "close": "Close",
    },
}


LDJSON = """  <script type="application/ld+json">
  {"@context": "https://schema.org", "@type": "BeautySalon", "name": "Maison de Lyn",
   "description": "Maquillage de mariée et d'événements à Paris et en Île-de-France",
   "url": "https://geksmode.github.io/maisondelyn/", "image": "https://geksmode.github.io/maisondelyn/img/mariee-fenetre.jpg",
   "priceRange": "€€", "areaServed": ["Paris", "Île-de-France"],
   "address": {"@type": "PostalAddress", "addressLocality": "Paris", "addressCountry": "FR"},
   "knowsLanguage": ["fr", "en", "vi", "ko"],
   "sameAs": ["https://www.instagram.com/maisondelyn_mua/"]}
  </script>
"""


def page(lang, fname, title, desc, body, script=""):
    t = T[lang]
    other = "en" if lang == "fr" else "fr"
    pre = "../" if lang == "en" else ""
    alt = ("en/" if lang == "fr" else "../") + fname
    cur = ' aria-current="page"'
    links = "\n".join(f'        <a href="{h}"{cur if h == fname else ""}>{n}</a>' for h, n in t["nav"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="alternate" hreflang="fr" href="{BASE}{fname}">
  <link rel="alternate" hreflang="en" href="{BASE}en/{fname}">
  <link rel="alternate" hreflang="x-default" href="{BASE}{fname}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500&family=Jost:wght@400;500&display=swap" rel="stylesheet">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{BASE}img/mariee-fenetre.jpg">
  <meta property="og:url" content="{BASE}{'en/' if lang == 'en' else ''}{fname}">
  <meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_GB'}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="{pre}style.css">
{LDJSON if fname == 'index.html' else ''}</head>
<body>
  <header class="top">
    <a class="brand" href="index.html">Maison de Lyn</a>
    <nav>
{links}
      <a class="switch" href="{alt}" hreflang="{other}" lang="{other}" title="{t['switch'][1]}">{t['switch'][0]}</a>
    </nav>
  </header>

  <main>
{body}
  </main>

  <footer class="bottom">
    <span>Maison de Lyn · {t['footer']}</span>
    <a href="{IG}">Instagram</a>
  </footer>
{script}</body>
</html>
"""


def fix(s):
    """Espaces insécables entre un nombre et son unité, et après « dès » / « from »."""
    s = re.sub(r"(\d) (€|h\b|%|am\b)", "\\1" + NB + "\\2", s)
    return re.sub(r"\b(dès|from) (\d)", "\\1" + NB + "\\2", s)


# ---------------------------------------------------------------- contenu
C = {}

C["fr"] = dict(
    home=("Maison de Lyn · Maquillage de mariée à Paris",
          "Linh, maquilleuse de mariée à Paris et en Île-de-France. Essai à domicile, jour J, maquillage des proches.",
          """    <section class="intro">
      <h1>Maquillage de mariée<br>à Paris</h1>
      <p>Je suis Linh. Je maquille les mariées et leurs proches, chez vous ou sur votre lieu de préparation, à Paris et en Île-de-France.</p>
      <a class="more" href="contact.html">Prendre rendez-vous</a>
    </section>

    <figure class="full"><img src="img/mariee-fenetre.jpg" alt="Mariée près d'une fenêtre, bouquet à la main"></figure>

    <section class="pair">
      <img src="img/mariee-tableau.jpg" alt="Mariée au bouquet rouge" loading="lazy">
      <img src="img/mariee-polaroid.jpg" alt="Mariée en voile" loading="lazy">
    </section>

    <section class="about">
      <p>Formée à Séoul, à l'académie de maquillage Art Stage 1992, je parle français, anglais, vietnamien et coréen. De l'essai au jour J, chaque mariée a toute mon attention.</p>
    </section>

    <section class="note">
      <p>Un essai pour trouver votre maquillage, puis le jour J à vos côtés. Forfait mariée dès 350 €.</p>
      <a class="more" href="prestations.html">Prestations et tarifs</a>
    </section>"""),
    services=("Prestations et tarifs · Maison de Lyn",
              "Tarifs de maquillage de mariée à Paris : forfait essai et jour J, proches, retouches, événements.",
              [("Forfait mariée", "dès 350 €", "Un essai d'environ 1 h 30, deux à quatre mois avant le mariage, puis le maquillage du jour J sur votre lieu de préparation. Faux cils et kit de retouche inclus."),
               ("Essai seul", "120 €", "Déduit du forfait si vous réservez."),
               ("Proches", "70 € par personne", "Mères, témoins, demoiselles d'honneur, maquillées le matin même."),
               ("Retouches", "60 € de l'heure", "Je reste jusqu'au vin d'honneur ou à la soirée, avec un changement de look si vous le souhaitez."),
               ("Événements et shootings", "dès 90 €", "Fiançailles, EVJF, séances photo, soirées.")],
              "Déplacement inclus dans Paris, sur devis en Île-de-France et ailleurs en France. Un acompte de 30 % réserve la date ; le solde est réglé le jour J. Supplément possible pour un début avant 7 h.",
              "Prestations"),
    gallery=("Galerie · Maison de Lyn", "Mariées et portraits éditoriaux maquillés par Linh, à Paris.", "Mariées", "Éditorial", "Plus sur Instagram"),
    faq=("FAQ · Maison de Lyn", "Questions fréquentes sur le maquillage de mariée : réservation, essai, tenue, déplacements.",
         [("Quand réserver ?", "Idéalement six à douze mois avant, surtout pour un samedi entre mai et septembre. Pour une date proche, demandez quand même."),
          ("L'essai est-il nécessaire ?", "Je le conseille : c'est là que nous choisissons le maquillage ensemble et que je découvre votre peau."),
          ("Où a lieu l'essai ?", "Chez vous à Paris, ou dans un lieu dont nous convenons."),
          ("Le maquillage tient-il toute la journée ?", "Oui. J'utilise des produits longue tenue qui résistent aux larmes, et je vous laisse un kit de retouche."),
          ("J'ai la peau sensible.", "Dites-le dans votre demande : j'adapte les produits et nous les testons pendant l'essai."),
          ("Combien de personnes le jour J ?", "Cela dépend de l'heure de la cérémonie. Comptez environ 45 minutes par personne ; au-delà de cinq, je viens avec une assistante."),
          ("Parlez-vous anglais ?", "Oui, ainsi que le vietnamien et le coréen. Je peux accompagner les mariées venues de l'étranger pour se marier à Paris."),
          ("Vous déplacez-vous hors de Paris ?", "Oui, en Île-de-France et partout en France, sur devis."),
          ("Comment réserver ?", "Écrivez-moi via la page Contact. La date est bloquée à réception de l'acompte et du contrat signé.")],
         "Questions"),
    contact=("Contact · Maison de Lyn", "Demandez un devis pour votre maquillage de mariée à Paris : réponse sous 48 h.",
             "Contact", "Parlez-moi de votre mariage. Je vous réponds sous 48 h avec mes disponibilités et un devis.",
             dict(nom="Nom", email="E-mail", tel="Téléphone", date="Date du mariage", lieu="Ville de préparation", nb="Nombre de personnes à maquiller",
                  prest="Prestation", opts=[("mariee", "Mariée"), ("proches", "Proches seulement"), ("evenement", "Événement ou shooting"), ("planner", "Je suis wedding planner")],
                  style="Style souhaité", styles=["Je ne sais pas encore", "Naturel", "Sophistiqué", "Glamour"],
                  msg="Votre message", send="Envoyer",
                  wip="Le formulaire sera actif très bientôt. En attendant, écrivez-moi sur Instagram.",
                  ok="Merci, votre demande est bien arrivée. Je vous réponds sous 48 h.",
                  err="L'envoi n'a pas fonctionné. Réessayez ou écrivez-moi sur Instagram."),
             "Ou sur Instagram"),
)

C["fr"]["reviews"] = []  # Avis de mariées : [("texte", "Prénom, juin 2025"), ...] — à fournir par Linh.
C["fr"]["extra"] = dict(
    styles_h="Trois styles",
    styles=[("Naturel", "Une peau lumineuse, un teint unifié, presque invisible."),
            ("Sophistiqué", "Un regard travaillé et une bouche affirmée, tout en restant vous."),
            ("Glamour", "Plus de lumière, de contraste et d'intensité pour la soirée.")],
    steps_h="Le déroulé",
    steps=[("L'essai", "Deux à quatre mois avant, nous choisissons ensemble le maquillage."),
           ("Le jour J", "Je vous rejoins sur votre lieu de préparation, avec tout le matériel."),
           ("Après la cérémonie", "Selon la formule, je reste pour les retouches ou un changement de look.")],
)

C["en"] = dict(
    home=("Maison de Lyn · Bridal make-up in Paris",
          "Linh, bridal make-up artist in Paris and Île-de-France. Trial at home, wedding day, make-up for your family and friends.",
          """    <section class="intro">
      <h1>Bridal make-up<br>in Paris</h1>
      <p>I'm Linh. I do make-up for brides and their loved ones, at home or wherever you get ready, in Paris and Île-de-France.</p>
      <a class="more" href="contact.html">Book an appointment</a>
    </section>

    <figure class="full"><img src="../img/mariee-fenetre.jpg" alt="Bride by a window holding a bouquet"></figure>

    <section class="pair">
      <img src="../img/mariee-tableau.jpg" alt="Bride with a red bouquet" loading="lazy">
      <img src="../img/mariee-polaroid.jpg" alt="Bride in a veil" loading="lazy">
    </section>

    <section class="about">
      <p>Trained in Seoul at the Art Stage 1992 make-up academy, I speak English, French, Vietnamese and Korean. From the trial to the wedding day, every bride has my full attention.</p>
    </section>

    <section class="note">
      <p>A trial to find your look, then the wedding day by your side. Bridal package from 350 €.</p>
      <a class="more" href="prestations.html">Services and prices</a>
    </section>"""),
    services=("Services and prices · Maison de Lyn",
              "Bridal make-up prices in Paris: trial and wedding-day package, family and friends, touch-ups, events.",
              [("Bridal package", "from 350 €", "A trial of about 1 h 30, two to four months before the wedding, then your wedding-day make-up wherever you get ready. False lashes and a touch-up kit included."),
               ("Trial only", "120 €", "Deducted from the package if you book."),
               ("Family and friends", "70 € per person", "Mothers, witnesses, bridesmaids, done on the morning itself."),
               ("Touch-ups", "60 € per hour", "I stay until the cocktail hour or the evening, with a change of look if you like."),
               ("Events and shoots", "from 90 €", "Engagements, hen parties, photo shoots, evenings.")],
              "Travel is included in Paris and quoted for Île-de-France and the rest of France. A 30 % deposit reserves your date; the balance is paid on the day. A supplement may apply for a start before 7 am.",
              "Services"),
    gallery=("Gallery · Maison de Lyn", "Brides and editorial portraits with make-up by Linh, in Paris.", "Brides", "Editorial", "More on Instagram"),
    faq=("FAQ · Maison de Lyn", "Frequently asked questions about bridal make-up: booking, trial, wear, travel.",
         [("When should I book?", "Ideally six to twelve months ahead, especially for a Saturday between May and September. For a closer date, ask anyway."),
          ("Do I need a trial?", "I recommend it: it's when we choose your make-up together and I get to know your skin."),
          ("Where is the trial?", "At your home in Paris, or somewhere we agree on."),
          ("Will the make-up last all day?", "Yes. I use long-wear, tear-proof products and leave you a touch-up kit."),
          ("I have sensitive skin.", "Mention it in your request: I adapt the products and we test them during the trial."),
          ("How many people on the day?", "It depends on the ceremony time. Allow about 45 minutes per person; for more than five, I bring an assistant."),
          ("Do you speak English?", "Yes, as well as French, Vietnamese and Korean. I can look after brides coming from abroad to marry in Paris."),
          ("Do you travel outside Paris?", "Yes, across Île-de-France and anywhere in France, on quote."),
          ("How do I book?", "Write to me from the Contact page. Your date is reserved once the deposit and signed contract are received.")],
         "Questions"),
    contact=("Contact · Maison de Lyn", "Request a quote for your bridal make-up in Paris: reply within 48 h.",
             "Contact", "Tell me about your wedding. I'll reply within 48 h with my availability and a quote.",
             dict(nom="Name", email="Email", tel="Phone", date="Wedding date", lieu="Town where you get ready", nb="Number of people",
                  prest="Service", opts=[("mariee", "Bride"), ("proches", "Family and friends only"), ("evenement", "Event or shoot"), ("planner", "I'm a wedding planner")],
                  style="Preferred style", styles=["Not sure yet", "Natural", "Sophisticated", "Glamour"],
                  msg="Your message", send="Send",
                  wip="The form will be live very soon. Meanwhile, message me on Instagram.",
                  ok="Thank you, your request has arrived. I'll reply within 48 h.",
                  err="Sending failed. Please try again or message me on Instagram."),
             "Or on Instagram"),
)

C["en"]["reviews"] = []
C["en"]["extra"] = dict(
    styles_h="Three styles",
    styles=[("Natural", "Luminous skin and an even complexion, almost invisible."),
            ("Sophisticated", "Defined eyes and a statement lip, while still looking like you."),
            ("Glamour", "More light, contrast and intensity for the evening.")],
    steps_h="How it works",
    steps=[("The trial", "Two to four months before, we choose your make-up together."),
           ("The wedding day", "I join you wherever you get ready, with everything needed."),
           ("After the ceremony", "Depending on your package, I stay for touch-ups or a change of look.")],
)

BRIDES = [("mariee-damas", "wide"), ("mariee-fenetre", "wide"), ("mariee-tableau", "wide"), ("mariee-polaroid", "wide"), ("couple", "wide")]
EDITO = ["boucles", "naturel", "robe-blanche", "tweed", "tweed-2"]


def build(lang):
    c = C[lang]
    pre = "../" if lang == "en" else ""
    out = os.path.join(OUT, "en") if lang == "en" else OUT
    os.makedirs(out, exist_ok=True)
    files = {}

    t, d, body = c["home"]
    if c["reviews"]:
        quotes = "\n".join(f"        <blockquote><p>{q}</p><cite>{who}</cite></blockquote>" for q, who in c["reviews"])
        body = body.replace('    <section class="note">', f'    <section class="reviews">\n{quotes}\n    </section>\n\n    <section class="note">')
    files["index.html"] = (t, d, body, "")

    t, d, rows, cond, h1 = c["services"]
    items = "\n".join(
        f"""      <li>
        <h2>{n}</h2>
        <p class="price">{p}</p>
        <p>{x}</p>
      </li>""" for n, p, x in rows)
    files["prestations.html"] = (t, d, f"""    <section class="page">
      <h1>{h1}</h1>
      <ul class="services">
{items}
      </ul>
      <h2 class="sub">{c['extra']['styles_h']}</h2>
      <dl class="steps">
{"".join(f"        <dt>{a}</dt><dd>{b}</dd>" + chr(10) for a, b in c['extra']['styles'])}      </dl>
      <h2 class="sub">{c['extra']['steps_h']}</h2>
      <dl class="steps">
{"".join(f"        <dt>{a}</dt><dd>{b}</dd>" + chr(10) for a, b in c['extra']['steps'])}      </dl>
      <p class="small">{cond}</p>
      <a class="more" href="contact.html">{T[lang]['book']}</a>
    </section>""", "")

    t, d, h_b, h_e, ig = c["gallery"]
    brides = "\n".join(f'        <img src="{pre}img/{n}.jpg" alt="" loading="lazy">' for n, _ in BRIDES)
    edito = "\n".join(f'        <img src="{pre}img/{n}.jpg" alt="" loading="lazy">' for n in EDITO)
    files["galerie.html"] = (t, d, f"""    <section class="page wide">
      <h1>{h_b}</h1>
      <div class="grid landscape">
{brides}
      </div>
      <h1 class="second">{h_e}</h1>
      <div class="grid portrait">
{edito}
      </div>
      <a class="more" href="{IG}">{ig}</a>
    </section>""", "")

    t, d, qa, h1 = c["faq"]
    qas = "\n".join(f"        <dt>{q}</dt>\n        <dd>{a}</dd>" for q, a in qa)
    files["faq.html"] = (t, d, f"""    <section class="page">
      <h1>{h1}</h1>
      <dl class="faq">
{qas}
      </dl>
      <a class="more" href="contact.html">{T[lang]['book']}</a>
    </section>""", "")

    t, d, h1, lead, f, ig = c["contact"]
    opts = "".join(f'<option value="{v}">{n}</option>' for v, n in f["opts"])
    files["contact.html"] = (t, d, f"""    <section class="page">
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <!-- Remplacer VOTRE_ID par l'identifiant Formspree (formspree.io) pour recevoir les demandes par e-mail. -->
      <form id="devis" action="https://formspree.io/f/VOTRE_ID" method="POST">
        <input type="hidden" name="langue" value="{lang}">
        <label>{f['nom']}<input name="nom" required autocomplete="name"></label>
        <label>{f['email']}<input name="email" type="email" required autocomplete="email"></label>
        <label>{f['tel']}<input name="telephone" type="tel" required autocomplete="tel"></label>
        <label>{f['date']}<input name="date" type="date" required></label>
        <label>{f['lieu']}<input name="lieu" required></label>
        <label>{f['nb']}<input name="personnes" type="number" min="1" value="1" required></label>
        <label>{f['prest']}<select name="prestation">{opts}</select></label>
        <label>{f['style']}<select name="style">{"".join(f"<option>{x}</option>" for x in f['styles'])}</select></label>
        <label class="full">{f['msg']}<textarea name="message" rows="4"></textarea></label>
        <button type="submit">{f['send']}</button>
        <p class="status" role="status" aria-live="polite"></p>
      </form>
      <a class="more" href="{IG}">{ig}</a>
    </section>""", f"""  <script>
    const form = document.getElementById('devis'), status = form.querySelector('.status');
    form.addEventListener('submit', async (e) => {{
      e.preventDefault();
      if (form.action.includes('VOTRE_ID')) {{ status.textContent = "{f['wip']}"; return; }}
      try {{
        const r = await fetch(form.action, {{ method: 'POST', body: new FormData(form), headers: {{ Accept: 'application/json' }} }});
        if (!r.ok) throw new Error();
        form.reset();
        status.textContent = "{f['ok']}";
      }} catch {{ status.textContent = "{f['err']}"; }}
    }});
  </script>
""")

    for fname, (t, d, body, script) in files.items():
        with open(os.path.join(out, fname), "w") as fh:
            fh.write(fix(page(lang, fname, t, d, body, script)))


build("fr")
build("en")
print("ok")

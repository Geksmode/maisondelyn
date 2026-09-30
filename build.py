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
        "prev": "Photo précédente",
        "next": "Photo suivante",
    },
    "en": {
        "nav": [("prestations.html", "Services"), ("galerie.html", "Gallery"), ("faq.html", "FAQ"), ("contact.html", "Contact")],
        "switch": ("FR", "Français"),
        "book": "Book an appointment",
        "footer": "Bridal make-up, Paris",
        "close": "Close",
        "prev": "Previous photo",
        "next": "Next photo",
    },
}


ARROW = '<svg aria-hidden="true" width="18" height="10" viewBox="0 0 18 10"><path d="M0 5h16M12 1l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'


def btn_inner(label):
    return f"<span>{label}</span>{ARROW}"


def btn(href, label, kind=""):
    cls = f"btn {kind}".strip()
    return f'<a class="{cls}" href="{href}">{btn_inner(label)}</a>'


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
    BOOK = f'  <lyn-book-button><a class="btn" href="contact.html">{btn_inner(t["book"])}</a></lyn-book-button>\n' 
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
<body{' class="home"' if fname == "index.html" else ""}>
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
  <lyn-lightbox label-close="{t['close']}" label-prev="{t['prev']}" label-next="{t['next']}"></lyn-lightbox>
{BOOK if fname != "contact.html" else ""}{script}  <script type="module" src="{pre}components.js"></script>
</body>
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
          None),
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
          None),
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

H = {
    "fr": dict(h1="Maquillage<br>de <em>mariée</em>", place="Paris et Île-de-France",
               alt_hero="Mariée près d'une fenêtre, bouquet à la main",
               marquee=["Naturel", "Sophistiqué", "Glamour", "Essai à domicile", "Paris", "Séoul", "Jour J", "Retouches"],
               hello="Je suis Linh.",
               intro="Je maquille les mariées et leurs proches, chez vous ou sur votre lieu de préparation. Un maquillage qui vous ressemble, pensé pour tenir de la cérémonie à la dernière danse.",
               cap1="Studio, bouquet rouge", cap2="Le jour J",
               seoul="Séoul — Paris",
               training="Formée en Corée du Sud, à l'académie de maquillage Art Stage 1992 à Séoul, j'apporte à Paris l'exigence du maquillage coréen : une peau travaillée, lumineuse et naturelle. Je vous accueille en français, anglais, vietnamien ou coréen.",
               offers=[("Forfait mariée", "dès 350 €"), ("Proches", "70 € par personne"), ("Événements et shootings", "dès 90 €")],
               offers_link="Prestations et tarifs",
               closing="Parlons de votre <em>mariage</em>"),
    "en": dict(h1="Bridal<br><em>make-up</em>", place="Paris and Île-de-France",
               alt_hero="Bride by a window holding a bouquet",
               marquee=["Natural", "Sophisticated", "Glamour", "Trial at home", "Paris", "Seoul", "Wedding day", "Touch-ups"],
               hello="I'm Linh.",
               intro="I do make-up for brides and their loved ones, at home or wherever you get ready. Make-up that looks like you, made to last from the ceremony to the last dance.",
               cap1="Studio, red bouquet", cap2="The wedding day",
               seoul="Seoul — Paris",
               training="Trained in South Korea at the Art Stage 1992 make-up academy in Seoul, I bring Korean make-up standards to Paris: skin that is carefully prepared, luminous and natural. I can look after you in English, French, Vietnamese or Korean.",
               offers=[("Bridal package", "from 350 €"), ("Family and friends", "70 € per person"), ("Events and shoots", "from 90 €")],
               offers_link="Services and prices",
               closing="Tell me about your <em>wedding</em>"),
}


def home_body(lang):
    h = H[lang]
    pre = "../" if lang == "en" else ""
    words = "".join(f"<span>{w}</span>" for w in h["marquee"])
    offers = "\n".join(
        f'        <li><span class="num">0{i}</span><span class="name">{n}</span><span class="price">{p}</span></li>'
        for i, (n, p) in enumerate(h["offers"], 1))
    return f"""    <section class="hero">
      <img src="{pre}img/mariee-fenetre.jpg" alt="{h['alt_hero']}">
      <div class="hero-text">
        <h1>{h['h1']}</h1>
        <p>{h['place']}</p>
      </div>
    </section>

    <div class="marquee" aria-hidden="true"><div>{words}{words}</div></div>

    <section class="hello reveal">
      <div>
        <h2>{h['hello']}</h2>
        <p>{h['intro']}</p>
        {btn("contact.html", T[lang]['book'])}
      </div>
      <img data-lightbox src="{pre}img/mariee-tableau.jpg" alt="" loading="lazy">
    </section>

    <section class="duo">
      <figure class="big reveal"><img data-lightbox src="{pre}img/mariee-damas.jpg" alt="" loading="lazy"><figcaption>{h['cap1']}</figcaption></figure>
      <figure class="small reveal"><img data-lightbox src="{pre}img/couple.jpg" alt="" loading="lazy"><figcaption>{h['cap2']}</figcaption></figure>
    </section>

    <section class="seoul reveal">
      <p class="huge">{h['seoul']}</p>
      <ul class="langs"><li>FR</li><li>EN</li><li>VI</li><li>KO</li></ul>
      <p>{h['training']}</p>
    </section>

    <section class="offers reveal">
      <ol>
{offers}
      </ol>
      {btn("prestations.html", h['offers_link'], "ghost")}
    </section>

    <section class="closing">
      <img src="{pre}img/mariee-polaroid.jpg" alt="" loading="lazy">
      <div>
        <h2>{h['closing']}</h2>
        {btn("contact.html", T[lang]['book'], "light")}
      </div>
    </section>"""


BRIDES = [("mariee-damas", "wide"), ("mariee-fenetre", "wide"), ("mariee-tableau", "wide"), ("mariee-polaroid", "wide"), ("couple", "wide")]
EDITO = ["boucles", "naturel", "robe-blanche", "tweed", "tweed-2"]


def build(lang):
    c = C[lang]
    pre = "../" if lang == "en" else ""
    out = os.path.join(OUT, "en") if lang == "en" else OUT
    os.makedirs(out, exist_ok=True)
    files = {}

    t, d, body = c["home"]
    body = home_body(lang)
    if c["reviews"]:
        quotes = "\n".join(f"        <blockquote><p>{q}</p><cite>{who}</cite></blockquote>" for q, who in c["reviews"])
        body = body.replace('    <section class="offers', f'    <section class="reviews">\n{quotes}\n    </section>\n\n    <section class="offers', 1)
    files["index.html"] = (t, d, body, "")

    t, d, rows, cond, h1 = c["services"]
    items = "\n".join(
        f"""      <li class="reveal">
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
      <dl class="steps reveal">
{"".join(f"        <dt>{a}</dt><dd>{b}</dd>" + chr(10) for a, b in c['extra']['styles'])}      </dl>
      <h2 class="sub">{c['extra']['steps_h']}</h2>
      <dl class="steps reveal">
{"".join(f"        <dt>{a}</dt><dd>{b}</dd>" + chr(10) for a, b in c['extra']['steps'])}      </dl>
      <p class="small">{cond}</p>
      {btn("contact.html", T[lang]['book'])}
    </section>""", "")

    t, d, h_b, h_e, ig = c["gallery"]
    brides = "\n".join(f'        <img class="reveal" data-lightbox src="{pre}img/{n}.jpg" alt="" loading="lazy">' for n, _ in BRIDES)
    edito = "\n".join(f'        <img class="reveal" data-lightbox src="{pre}img/{n}.jpg" alt="" loading="lazy">' for n in EDITO)
    files["galerie.html"] = (t, d, f"""    <section class="page wide">
      <h1>{h_b}</h1>
      <div class="grid landscape">
{brides}
      </div>
      <h1 class="second">{h_e}</h1>
      <div class="grid portrait">
{edito}
      </div>
      {btn(IG, ig, "ghost")}
    </section>""", "")

    t, d, qa, h1 = c["faq"]
    qas = "\n".join(f"        <dt>{q}</dt>\n        <dd>{a}</dd>" for q, a in qa)
    files["faq.html"] = (t, d, f"""    <section class="page">
      <h1>{h1}</h1>
      <dl class="faq reveal">
{qas}
      </dl>
      {btn("contact.html", T[lang]['book'])}
    </section>""", "")

    t, d, h1, lead, f, ig = c["contact"]
    opts = "".join(f'<option value="{v}">{n}</option>' for v, n in f["opts"])
    files["contact.html"] = (t, d, f"""    <section class="page">
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <!-- Remplacer VOTRE_ID par l'identifiant Formspree (formspree.io) pour recevoir les demandes par e-mail. -->
      <lyn-quote-form data-wip="{f['wip']}" data-ok="{f['ok']}" data-err="{f['err']}">
      <form id="devis" class="reveal" action="https://formspree.io/f/VOTRE_ID" method="POST">
        <input type="hidden" name="langue" value="{lang}">
        <label>{f['nom']}<input name="nom" required autocomplete="name"></label>
        <label>{f['email']}<input name="email" type="email" required autocomplete="email"></label>
        <label>{f['tel']}<input name="telephone" type="tel" required autocomplete="tel"></label>
        <label>{f['date']}<input name="date" type="date" required></label>
        <label>{f['lieu']}<input name="lieu" required></label>
        <label>{f['nb']}<input name="personnes" type="number" min="1" value="1" required></label>
        <label>{f['prest']}<select name="prestation">{opts}</select></label>
        <label>{f['style']}<select name="style">{"".join(f"<option>{x}</option>" for x in f['styles'])}</select></label>
        <label class="full">{f['msg']}<textarea name="message" rows="3"></textarea></label>
        <button class="btn" type="submit">{btn_inner(f['send'])}</button>
        <p class="status" role="status" aria-live="polite"></p>
      </form>
      </lyn-quote-form>
      {btn(IG, ig, "ghost")}
    </section>""", "")

    for fname, (t, d, body, script) in files.items():
        with open(os.path.join(out, fname), "w") as fh:
            fh.write(fix(page(lang, fname, t, d, body, script)))


build("fr")
build("en")
print("ok")

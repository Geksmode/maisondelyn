"""Télécharge les polices des versions vietnamienne et coréenne et les déclare dans style.css.

Usage : python3 build.py . && python3 polices.py
- Vietnamien : Bodoni Moda et Jost n'ont pas les lettres accentuées vietnamiennes (ạ, ế, ở...).
  On utilise Playfair Display (titres) et Be Vietnam Pro (texte), de la même famille de style.
- Coréen : Noto Serif KR (titres) et Noto Sans KR (texte), réduites aux seuls caractères
  utilisés dans ko/*.html pour rester légères. À relancer si les textes coréens changent.
Les polices ne sont téléchargées par le navigateur que sur les pages qui les utilisent.
"""
import glob
import html
import os
import re
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
START, END = "/* Polices vietnamiennes et coréennes (générées par polices.py) */", "/* Fin des polices générées */"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def faces(family, axes, prefix, subsets=None, text=None):
    """Télécharge les fichiers woff2 d'une famille Google Fonts et renvoie les @font-face locaux."""
    url = f"https://fonts.googleapis.com/css2?family={family}:{axes}&display=swap"
    if text:
        url += "&text=" + urllib.parse.quote(text)
    css = get(url).decode()
    out = []
    for comment, block in re.findall(r"(?:/\* ([\w-]+) \*/\s*)?(@font-face \{.*?\})", css, re.S):
        if subsets and comment not in subsets:
            continue
        style = re.search(r"font-style: (\w+)", block).group(1)
        weight = re.search(r"font-weight: (\d+)", block).group(1)
        name = f"{prefix}-{style}-{weight}{'-' + comment if comment else ''}.woff2"
        with open(os.path.join(FONTS, name), "wb") as fh:
            fh.write(get(re.search(r"url\((https://[^)]+)\)", block).group(1)))
        block = re.sub(r"src: url\([^)]+\) format\('woff2'\)", f"src: url(fonts/{name}) format('woff2')", block)
        out.append(block)
        print(name)
    return out


# Caractères coréens réellement utilisés (texte visible des pages et menus de langue).
text = ""
for path in glob.glob(os.path.join(HERE, "ko", "*.html")) + glob.glob(os.path.join(HERE, "*.html")):
    text += html.unescape(re.sub(r"<[^>]+>", " ", open(path).read()))
hangul = "".join(sorted({ch for ch in text if "㄰" <= ch <= "㆏" or "가" <= ch <= "힯"}))

blocks = []
blocks += faces("Playfair+Display", "ital,wght@0,500;1,500", "PlayfairDisplay", {"latin", "latin-ext", "vietnamese"})
blocks += faces("Be+Vietnam+Pro", "wght@400;500", "BeVietnamPro", {"latin", "latin-ext", "vietnamese"})
blocks += faces("Noto+Serif+KR", "wght@500", "NotoSerifKR-ko", text=hangul)
blocks += faces("Noto+Sans+KR", "wght@400;500", "NotoSansKR-ko", text=hangul)

path = os.path.join(HERE, "style.css")
css = open(path).read()
css = re.sub(re.escape(START) + ".*?" + re.escape(END) + "\n?", "", css, flags=re.S)
css = css.replace("\n:root {", f"\n{START}\n" + "\n".join(blocks) + f"\n{END}\n\n:root {{", 1)
open(path, "w").write(css)
print(len(hangul), "caractères coréens")

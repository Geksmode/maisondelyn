"""Prépare les photos du site : plusieurs tailles en WebP + une version JPEG de secours.

Usage : python3 images.py <dossier des photos sources>
Chaque photo source <nom>.jpg donne img/<nom>-<largeur>.webp et img/<nom>.jpg,
et img/manifest.json liste les tailles disponibles (lu par build.py).
"""
import glob
import json
import os
import sys

import cv2

SRC = sys.argv[1] if len(sys.argv) > 1 else "img"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
WIDTHS = [640, 960, 1280, 1920, 2560]

manifest = {}
for path in sorted(glob.glob(os.path.join(SRC, "*.jpg"))):
    name = os.path.splitext(os.path.basename(path))[0]
    img = cv2.imread(path)
    h, w = img.shape[:2]
    sizes = []
    for target in WIDTHS:
        if target > w:
            continue
        r = cv2.resize(img, (target, round(h * target / w)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(OUT, f"{name}-{target}.webp"), r, [cv2.IMWRITE_WEBP_QUALITY, 80])
        sizes.append(target)
    if w not in sizes and w < WIDTHS[-1]:
        cv2.imwrite(os.path.join(OUT, f"{name}-{w}.webp"), img, [cv2.IMWRITE_WEBP_QUALITY, 80])
        sizes.append(w)
    # JPEG de secours (vieux navigateurs, aperçus de partage) : 1920 px maximum.
    k = min(1, 1920 / w)
    j = cv2.resize(img, (round(w * k), round(h * k)), interpolation=cv2.INTER_AREA) if k < 1 else img
    cv2.imwrite(os.path.join(OUT, f"{name}.jpg"), j, [cv2.IMWRITE_JPEG_QUALITY, 82, cv2.IMWRITE_JPEG_PROGRESSIVE, 1])
    manifest[name] = {"w": w, "h": h, "sizes": sorted(sizes)}
    print(name, w, "x", h, sizes)

with open(os.path.join(OUT, "manifest.json"), "w") as fh:
    json.dump(manifest, fh, indent=1)

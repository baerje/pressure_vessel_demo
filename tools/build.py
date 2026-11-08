# Builds the hosted web app (index.html, icons, manifest at the repo root) from src/pressure-vessel.html.
# Run from anywhere:  python3 tools/build.py
import os, json
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'pressure-vessel.html')
OUT = ROOT
os.makedirs(OUT, exist_ok=True)
src = open(SRC).read()
body = src.split('\n', 2)[2]  # drop <title> and the claude viewport meta; we write our own head
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Pressure Vessel Mixer</title>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Vessel Mixer">
<meta name="theme-color" content="#eef1f3">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" href="icon-512.png">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)} body{margin:0;font:14px system-ui,sans-serif} [hidden]{display:none!important} img{max-width:100%}</style>
</head>
<body>
'''
open(f'{OUT}/index.html', 'w').write(head + body + '\n</body>\n</html>\n')

def icon(size):
    k = size / 180
    im = Image.new('RGB', (size, size), '#eef1f3'); d = ImageDraw.Draw(im)
    S = lambda *v: [x * k for x in v]
    d.rounded_rectangle(S(40, 50, 140, 145), radius=18 * k, fill='#f7f9fa', outline='#56646d', width=round(8 * k))
    d.rectangle(S(80, 22, 100, 52), fill='#56646d')
    for x, y, c in [(65, 80, '#d8423a'), (95, 95, '#2f6fd6'), (118, 75, '#22975a'), (70, 118, '#2f6fd6'), (105, 125, '#d8423a'), (88, 70, '#d8423a'), (122, 110, '#22975a')]:
        d.ellipse(S(x - 8, y - 8, x + 8, y + 8), fill=c)
    return im
icon(180).save(f'{OUT}/apple-touch-icon.png'); icon(512).save(f'{OUT}/icon-512.png')
json.dump({"name": "Pressure Vessel Mixer", "short_name": "Vessel Mixer", "start_url": "./", "display": "fullscreen",
           "orientation": "landscape", "background_color": "#eef1f3", "theme_color": "#eef1f3",
           "icons": [{"src": "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
                     {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(f'{OUT}/manifest.webmanifest', 'w'), indent=2)
print('Built', OUT)

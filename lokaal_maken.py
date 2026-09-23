"""
lokaal_maken.py
───────────────
Nabewerking van de door Folium gegenereerde kaart, zodat bezoekers géén
verzoeken meer doen naar externe partijen (Google Fonts, jsDelivr, cdnjs,
code.jquery.com, bootstrapcdn). Alleen de PDOK-kaarttegels blijven extern.

- Alle externe <script src="https://..."> en <link rel="stylesheet" href="https://...">
  worden verwijderd (Folium laadt standaard veel ongebruikte libraries).
- Leaflet (JS + CSS) en Bootstrap-CSS worden uit vendor/ ingebed.
- De lettertypen worden als base64 ingebed (SIL Open Font License).

Wordt automatisch aangeroepen onderaan maak_kaart.py, maar kan ook los:
    python lokaal_maken.py afdelingsgrenzen_kaart.html
"""
import base64
import re
import sys
from pathlib import Path

VENDOR = Path(__file__).parent / 'vendor'


def _tekst(naam):
    t = (VENDOR / naam).read_text(encoding='utf-8')
    return re.sub(r'(/\*# sourceMappingURL=.*?\*/|//# sourceMappingURL=.*)', '', t)


def _font_face(familie, gewicht, bestand):
    data = base64.b64encode((VENDOR / bestand).read_bytes()).decode()
    return (f"@font-face{{font-family:'{familie}';font-style:normal;font-weight:{gewicht};"
            f"font-display:swap;src:url(data:font/woff2;base64,{data}) format('woff2');}}\n")


def lokaal_maken(pad):
    pad = Path(pad)
    html = pad.read_text(encoding='utf-8')

    # 1. Externe scripts, stylesheets en preconnects eruit
    html = re.sub(r'\s*<script src="https?://[^"]+"></script>', '', html)
    html = re.sub(r'\s*<link rel="stylesheet" href="https?://[^"]+"\s*/?>', '', html)
    html = re.sub(r'\s*<link href="https://fonts\.googleapis\.com[^>]*>', '', html)
    html = re.sub(r'\s*<link rel="preconnect"[^>]*>', '', html)

    # 2. Lokale versies direct na <head> invoegen (vóór de Folium-code die L gebruikt)
    fonts = ''.join(_font_face('Barlow Condensed', w, f'barlow-condensed-latin-{w}-normal.woff2')
                    for w in (400, 600, 700))
    fonts += _font_face('Special Gothic Condensed One', 400,
                        'special-gothic-condensed-one-latin-400-normal.woff2')
    ingebed = (
        '\n<script>/* Leaflet 1.9.3 (lokaal) */\n' + _tekst('leaflet.js') + '\n</script>\n'
        '<style>/* Leaflet 1.9.3 CSS (lokaal) */\n' + _tekst('leaflet.css') + '\n</style>\n'
        '<style>/* Bootstrap 5.2.2 CSS (lokaal) */\n' + _tekst('bootstrap.min.css') + '\n</style>\n'
        '<style>/* Lettertypen lokaal ingebed (SIL Open Font License) */\n' + fonts + '</style>\n'
    )
    html = html.replace('<head>', '<head>' + ingebed, 1)

    # 3. Controle: welke externe verzoeken blijven over?
    over = set(re.findall(r'(?:src|href)="(https?://[^"/]+)', html))
    pad.write_text(html, encoding='utf-8')
    print(f'Lokaal gemaakt: {pad.name}. Resterende externe src/href-hosts: {sorted(over) or "geen"}')


if __name__ == '__main__':
    lokaal_maken(sys.argv[1] if len(sys.argv) > 1 else 'afdelingsgrenzen_kaart.html')

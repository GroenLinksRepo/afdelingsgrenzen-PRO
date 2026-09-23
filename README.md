# Afdelingsgrenzen Progressief Nederland

Interactieve kaart van de afdelingsgrenzen, gehost via GitHub Pages en ingesloten op groenlinkspvda.nl/afdelingen.

**Opnieuw genereren:** zet `Afdelingsgrenzen PRO.xlsx` in deze map en draai `python maak_kaart.py`.
Het script roept daarna automatisch `lokaal_maken.py` aan.

**Privacy:** de kaart laadt geen externe lettertypen of libraries. Leaflet, Bootstrap-CSS en de
lettertypen (Barlow Condensed, Special Gothic Condensed One, SIL Open Font License) staan in `vendor/`
en worden in het HTML-bestand ingebed. Het enige externe verzoek zijn de kaarttegels van de
BRT Achtergrondkaart (PDOK/Kadaster).

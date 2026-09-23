# Afdelingsgrenzen Progressief Nederland

Interactieve kaart van de afdelingsgrenzen, gehost via GitHub Pages en ingesloten op groenlinkspvda.nl/afdelingen.

**Opnieuw genereren:** zet `Afdelingsgrenzen PRO.xlsx` in deze map en draai `python maak_kaart.py`.
Het script roept daarna automatisch `lokaal_maken.py` aan.

**Links naar lokale websites:** bij het genereren zoekt het script per gemeente op of er een lokale
website `<gemeente>.progressiefnederland.nl` bestaat (via DNS). Heeft een gemeente geen eigen site, dan
toont de popup de lokale websites van de andere gemeenten binnen dezelfde afdeling. Nieuwe subsites worden dus vanzelf opgepikt bij de volgende run. Afwijkende namen
(bv. 's-Gravenhage → `denhaag`) staan in `SITE_OVERRIDES` in `maak_kaart.py`. Het script print aan
het eind welke gemeenten nog geen site hebben.

**Privacy:** de kaart laadt geen externe lettertypen of libraries. Leaflet, Bootstrap-CSS en de
lettertypen (Barlow Condensed, Special Gothic Condensed One, SIL Open Font License) staan in `vendor/`
en worden in het HTML-bestand ingebed. Het enige externe verzoek zijn de kaarttegels van de
BRT Achtergrondkaart (PDOK/Kadaster).

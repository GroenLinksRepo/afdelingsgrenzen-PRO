# Afdelingsgrenzen Progressief Nederland

Interactieve kaart van de afdelingsgrenzen, gehost via GitHub Pages en ingesloten op groenlinkspvda.nl/afdelingen.

**Opnieuw genereren:** zet `Afdelingsgrenzen PRO.xlsx` in deze map en draai `python maak_kaart.py`.
Het script roept daarna automatisch `lokaal_maken.py` aan.

**Links naar subsites:** bij het genereren zoekt het script per gemeente op of er een subsite
`<gemeente>.progressiefnederland.nl` bestaat (via DNS). Heeft een gemeente geen eigen site, dan wordt
de site onder de afdelingsnaam gebruikt, of anders de site(s) van de andere gemeenten in dezelfde
afdeling. Nieuwe subsites worden dus vanzelf opgepikt bij de volgende run. Afwijkende namen
(bv. 's-Gravenhage → `denhaag`) staan in `SITE_OVERRIDES` in `maak_kaart.py`. Het script print aan
het eind welke gemeenten nog geen site hebben.

**Privacy:** de kaart laadt geen externe lettertypen of libraries. Leaflet, Bootstrap-CSS en de
lettertypen (Barlow Condensed, Special Gothic Condensed One, SIL Open Font License) staan in `vendor/`
en worden in het HTML-bestand ingebed. Het enige externe verzoek zijn de kaarttegels van de
BRT Achtergrondkaart (PDOK/Kadaster).

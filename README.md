# bgt2osm

Een repository om `.osm`-bestanden te maken van BGT data, om ze bijvoorbeeld in te laden in JOSM om te helpen tijdens het editen. Op dit moment alleen om de geometrie te gebruiken en hieraan eigen tags toe te voegen, maar mogelijk kunnen tags later ook automatisch vertaald worden uit de originele BGT-waardes. Op dit moment werkt alleen `bgt_begroeidterreindeel.gml`.

## Instructies:

- Download de gewenste BGT data via https://app.pdok.nl/lv/bgt/download-viewer/
- Extract het gedownloade zipbestand.
- Navigeer met een terminal in de uitgepakte `extract/`-map, dezelfde map waar nu ook `bgt_begroeidterreindeel.gml` te vinden is.
- Download `cleaner.py` uit deze repo naar de locatie waar je nu in zit.
- Met dezelfde terminal, run `python3 cleaner.py`, dit maakt een nieuw bestand genaamd `source.geojson`.
- Run `ogr2ogr -f "GML" destination.gml source.geojson -simplify 0.000001`.
- Run `python3 -m ogr2osm -e 28992 destination.gml bgt_begroeidterreindeel.osm`. (`ogr2osm` is te vinden op https://github.com/roelderickx/ogr2osm) 
- Open `bgt_begroeidterreindeel.osm` in je editor, negeer of verwijder de artifacts, en veel editplezier!

## Uitleg

Het liefst zou je meteen `ogr2osm` gebruiken op `bgt_begroeidterreindeel.gml`, maar dit faalt op features met het type CURVEPOLYGON. Hierom worden deze features eerst vertaald naar gewone polygons via `cleaner.py`

`cleaner.py` maakt een nieuw `.geojson` bestand aan zonder enige CURVEPOLYGONs, en vervolgens wordt dit `.geojson`-bestand weer terugvertaald naar een `.gml`-bestand via `ogr2ogr`. Deze stap haalt meteen ook overbodige nodes weg met `-simplify`, al moet ik nog even testen of dit wel echt werkt.

Hierna wordt dit nieuwe `.gml`-bestand zonder CURVEPOLYGONs vertaald naar een `.osm`-bestand via `ogr2osm`.

Geïnspireerd door https://community.openstreetmap.org/t/voorverwerken-bgt-voor-import-in-osm/105109/79
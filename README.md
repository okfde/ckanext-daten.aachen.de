ckanext-daten.aachen.de
=======================

Theme für http://daten.aachen.de.

Das Plugin erweitert Standard-CKAN an folgenden Stellen:

- Header (Bild, sollte 940x140px sein und ist im CSS Konfig zu verlinken)
- Footer (Über -> Impressum)
- 'Promoted', den Teil wo das Stadt Aachen Bild steht/stehen soll

Zusätzlich wurden CSS Erweiterungen über Fanstatic (https://ckan.readthedocs.org/en/1377-javascript-tutorial/theming/fanstatic.html) implementiert (https://github.com/okfde/ckanext-daten.aachen.de/issues/1) aber noch nicht getestet; da am Anfang kein Plugin nötig war, ist viel vom 'Theme' (=CSS) als CSS Überschreibungen im Admin Konfig implementiert.

### Hilfreiche Paster Befehle
Suche Indices aktualisieren (Tags Anzahlen nicht stimmen oder ähnliche Problemen):

    paster --plugin=ckan search-index rebuild -c /opt/ckan/etc/stac/od_prod.ini
    
Templates/caching in Ordnung bringen:

    paster --plugin=ckan front-end-build -c /opt/ckan/etc/stac/od_prod.ini
    
(plus Apache Neustart(?))

    



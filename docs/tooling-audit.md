# Repository- und Werkzeugprüfung — 2026-10-03

## Produktionsauftrag

V1 ist ein organischer, stilisierter Owli-Avatar auf einer Stange. Zuerst
Issue #3 (Blockout aus vier Ansichten), danach #4 (Primärformen), #5 (Füße/Stange),
#6 (Federgruppen), #7 (Materialien), #8 (Rig) und #9 (Animationen).
Issue #2 ist noch offen, seine neun Referenzdateien sind jedoch bereits vorhanden
und entsprechen dem Manifest einschließlich SHA-256 und Abmessungen.

## Ausstattung und Korrekturen

- Windows: Python 3.11.9, Pillow 12.2.0, Git und Git LFS 3.7.1 vorhanden.
- Blender 5.2.1 LTS und 5.0.0 vorhanden, aber nicht im PATH.
- FFmpeg, Make und GitHub CLI vorhanden; sie sind für den Blender-Start optional.
- Beide Blender-Versionen melden `BLENDER_EEVEE`; das bisherige
  `BLENDER_EEVEE_NEXT` verhinderte den Szenenstart. Die Auswahl ist korrigiert.
- Ein Python-Runner ergänzt automatische Blender-Suche, Diagnose, strikte
  Validierung, geschützten Szenenstart und einen isolierten Smoke-Test.
- Die Materialbibliothek wird jetzt gespeichert und durch Fake Users auch ohne
  Objektzuweisung erhalten. Bisher ging sie nach Beenden des Skripts verloren.
- CI prüft Windows/Linux, LFS-Checkout, Referenzen, Syntax und Regressionen.
- Der Manifeststatus ist an die tatsächlich vorhandenen Referenzen angepasst.

## Grenzen und offene Arbeit

Der lokale GitHub-CLI-Token ist ungültig. Im eingeschränkten Arbeitskontext konnte
SSH außerdem die Benutzerdatei `known_hosts` nicht lesen. Der verbundene
GitHub-Connector funktioniert als Alternative. Diese lokalen Zugangsdaten werden
nicht ins Repository geschrieben.

Die Blender-Skripte sind Produktionsgerüste. Ein technischer Smoke-Test bestätigt
weder Designfreigabe noch fertige Topologie, Materialien oder Rig-Funktionen.
Der aktuelle Validierungsrenderer enthält noch keinen Studio-Lichtaufbau.
Die Silhouettenprüfung und Dokumentation tatsächlicher Modellierungsabweichungen
gehören zu Issue #3. Diese Repo-Optimierung verändert keine Anatomie, Kameraposition,
Referenzpriorität oder Materialgestaltung; die 3+1-Regel bleibt bestehen.

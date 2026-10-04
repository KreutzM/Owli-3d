# #37 — Reproduktion und Primärbelege

Die eigene Lieferung liegt in `owli_review_fixes_v01.blend`; Ausgang #5 bleibt
unverändert. [Bericht](report.md), [Vieransichtenentscheidung](review.json),
[maschinelle Nachweise](verification.json), [Vorher/Nachher](baseline_vs_corrected.png).
Die generierte Proof-Datei vergibt keine visuelle Freigabe (`design_approval=false`).

Vom Repository aus, neue explizite Work-Verzeichnisse wählen:

```powershell
python scripts/review_fixes_review.py --work tmp/review-fixes-37/reproduction01 --output validation/reviews/review_fixes_v01 --scene-output blender/scene/owli_review_fixes_v01.blend
python scripts/audit_review_fixes_history.py --output tmp/review-fixes-37/history-reproduction.json
python scripts/project.py doctor
python scripts/project.py validate
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

Der Producer ersetzt nur seine eigene #37-Lieferung. Die Ausgangsszene und alle
384 code-owned Vorgängerdateien müssen vor und nach dem Run unverändert sein.
Ein erneuter Producer-Run kann den Blend-Containerhash ändern und macht die
separate visuelle Entscheidung deshalb frisch prüfpflichtig; keine Review-Hashes
automatisch nachtragen. Reproduktion nach Abschluss bevorzugt auf isoliertem
Repository-Checkout ausführen, wenn die akzeptierte #37-Lieferung erhalten soll.

Fünf echte Blender-Prozesse: Build/Repeat, gespeicherter Build, Reload A, Reload B,
Foot-Parameterecken. Der Build und alle drei frischen Opens haben dieselben
Geometrie-/Probe-/Studio-Daten. Die drei frischen Renderer liefern identische
1024px-RGBA-Pixel. Veröffentlichte Textlogs verwenden UTF-8/LF ohne abschließende
Leerzeichen; die unveränderten Prozesslogs bleiben im expliziten Scratch-Verzeichnis.
`evidence/live_neutral` bewahrt die ursprünglichen In-Process-
Ansichten; Eevee-Cacheabweichungen gegenüber frischen Renderern sind kein
Geometrie- oder Kameradifferenzbeweis und werden nicht als Pixelgleichheit ausgegeben.

`evidence/baseline`, `neutral`, `blink`, `beak_open`, `reload_a`, `reload_b` und
`live_neutral` verwenden dieselben vier unveränderten Kameras. Es gibt keine neue
allgemeine Konzeptreferenz. Boards und der Vorher/Nachher-Vergleich skalieren nur
die tatsächlich erzeugten Pixel. Referenzen behalten Rang 00 > 07 > 08 > Beauty.

Historische Face/Beak/Feet-Producer bleiben Version 1. `delivery_gates.py` und
`history_gate.py` sind aktuelle Version 2; `review_fixes_gate.py` prüft diese eigene
Lieferung. Quelldaten, vollständige Inventare, konkrete Vergleichsfeldschemas,
worker-generierte Daten und unabhängige Reviewbelege ergänzen die echten Blender-
Proben; Hashes alleine beweisen weder Markenidentität noch fertiges Avatar-Rig.

Der globale Smoke startet in Scratch bei Stufe 00 und führt 30 vor 40 aus.
Produktionsfortsetzung #6 startet zusätzlich von dieser neuen #37-Kopie. `GRP_`
bleibt Füßen/Stange vorbehalten; Material-/Rig-Gerüste und generisches Rendern
nur auf Arbeitskopien anwenden. Weitere konkrete QA: [Folgeplan](../../../docs/review-fixes-qa-followup.md).

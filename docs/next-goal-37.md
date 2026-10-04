# Fortsetzungsplan #37 — Review-Findings

Auftrag: [#37](https://github.com/KreutzM/Owli-3d/issues/37), Teilaufgaben #34/#35.
Ausgangspunkt: `473f8726d32ac7852ef93884b3010b52b8836521`, echte Szene
`blender/scene/owli_feet_v01.blend`, SHA256
`0fb1512b3a27c4ebe5b7cbdebf520643b7208f2c74f8a847545ffc51dda66797`.

1. Gates als Version 2 ergänzen, historische Produzenten und ihre Quellbindungen
   bytegleich erhalten. `delivery_gates.py` erzwingt komplette Pflichtinventare;
   `history_gate.py` verankert zwei Archive und zwölf Snapshots im echten Git-Vorgänger.
2. Nur eine neue Arbeitskopie bearbeiten. Gesichtsscheibe/Wangen verbreitern und
   in den Kopf führen; Brauen organisch anheben/verjüngen. Logo 00 für Identität,
   07 für Profil/Volumen, 08 für Konstruktion. Parameter separat versionieren.
3. Auf neuer Geometrie Blink/Blick/Schnabel und Fußkontakt prüfen, Cage/evaluierte
   Flächen einschließlich adjazenter Faltungen prüfen. Wiederholter Build und
   zwei neue Blender-Prozesse; exakt dieselben vier Kameras/Studio verwenden.
4. Eigene dauerhafte Belege, Vieransichtenentscheidung und IR-01–05-Matrix liefern;
   unabhängige visuelle/technische Prüfung; Tests/Validate/Compileall/Scratch-Smoke.
5. Eigenen PR erstellen und nach geprüfter Lieferung mergen; #34/#35/#37/Epic und
   Übergabe aktualisieren. #6 startet erst vom tatsächlich gelieferten neuen Blend.

Neue Gates übernehmen keine rückwirkende Designentscheidung. Die historischen
`face_review.py`, `beak_review.py`, `feet_review.py`, `history_bindings.py` sind
Version 1; neue Produktionsnachweise verwenden Version 2 und eigene vollständige
Inventare. `validate_project.py` ist nicht in historischen Nachweisen gebunden und
kann die zusätzlichen aktuellen Gates ausführen, ohne Approval-Hashes zu ändern.

Runner: Ausgangsszene, Arbeitskopie und Ausgabe explizit wählen. Der generische
Render-Befehl speichert die geladene Datei. Material-/Rig-Gerüste speichern nach
`owli.blend`; nur in Scratch ausführen. Vollständiger Smoke bleibt numerisch sortiert
(30 vor 40); #37/#6 laufen zusätzlich vom akzeptierten #5 beziehungsweise #37.
`GRP_` bleibt Fuß/Stange vorbehalten. Neue Gesichtslagen verwenden `RFX_`, später
Flügel-/Körper-/Schwanzlagen einen eigenen Präfix. Alte Gesamtverifier erwarten
ersetzte Guide-Namen: nur kompatible generische Auditoren gezielt verwenden.

Lieferstand: neue parametrisierte Geometrie, strenge v2-Gates und echte neue
Blender-Belege liegen unter `validation/reviews/review_fixes_v01/`; der
[Korrekturbericht](../validation/reviews/review_fixes_v01/report.md) enthält
Abschlussmatrix, Referenzentscheidung und konkrete Grenzen. Aktuelle Szene:
`owli_review_fixes_v01.blend`. Der eigene #37-PR/Git-Verlauf verankert den Merge;
die tatsächliche Issue-/Epic-Fortsetzung folgt dessen Abschluss. #6 hat seinen
aktualisierten vollständigen [Startplan](next-goal-6.md).

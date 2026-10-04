# Startplan für Goal #6

Verbindlicher Umfang: [Issue #6](https://github.com/KreutzM/Owli-3d/issues/6).
Dieser Plan ergänzt das Issue, schränkt dessen Lieferumfang aber nicht ein.
Ausgang nach Abschluss/Merge von #37:
`blender/scene/owli_review_fixes_v01.blend` und dessen
[Korrekturbericht](../validation/reviews/review_fixes_v01/report.md).
Für dieses Goal wurde noch kein neuer Modellierungsstand begonnen.

## Zuerst prüfen

- [Agent-Übergabe](agent-handoff.md), AGENTS-Pflichtlektüre und Referenzen lesen.
- Aktuelles #37 mit `review_fixes_gate.validate_review_fixes` sowie historische
  Lieferungen mit `delivery_gates` (Version 2) und Tests bestätigen; nur eine Kopie
  der akzeptierten Szene bearbeiten.
- `30_wings_feathers.py` ist derzeit nur Policy-Metadaten. Tatsächliche
  `BLK_Wing_L/R`-Volumes und `BLK_Tail` sind die groben Ausgangsformen;
  Collection `FEATHERS` ist leer.
- Turnaround 07 bestimmt Profil, Rücken und kompakten Schwanz; Sheet 08 bestimmt
  große überlappende Federlagen. Das Logo bestimmt weiterhin Farb-/Gesichtsidentität.

## Vollständiger Bauauftrag

1. Bearbeitbare saubere Primärflügel an den Körper anschließen; ruhende Flügel
   bleiben körpernah. Kein Flug-Rig und keine volle Flugartikulation hinzufügen.
2. Eine überschaubare Anzahl großer entworfener Federgruppen für **Flügel,
   Körper und Schwanz** bauen. Wiederverwendbarkeit/Symmetrie nachvollziehbar
   über Geometrie, Instanzen, Spiegelung oder Parameter umsetzen. Keine
   bloßen Metadaten, keine hunderten Einzelfedern und keine Federsimulation.
3. Flügelwurzel und Federbindung als zusammenhängende Gesteneinheit vorbereiten.
   Eine begrenzte tatsächliche Gesten-/Poseprobe muss zeigen, dass Primärflügel
   und sichtbare Lagen gemeinsam folgen. Endgültige Benutzercontrols bleiben #23.
4. Profil und Rücken mit 07/08 vergleichen; Schwanz kompakt, Kontur sauber,
   Feather-Layering erkennbar. Front und 3/4 ebenfalls beurteilen. Größere
   Silhouettenänderungen aus den Referenzen begründen und neu dokumentieren.
5. Unbetroffene Kopf-/Gesichts-/Schnabel-/Fuß-/Stangenkomponenten erhalten.
   Insbesondere echte 3+1-Anatomie und tragenden Stangengriff weiter prüfen.
6. Verbliebenen Gesichtsfederfluss aus #37 mit wenigen breiten, symmetrischen
   cream Gruppen ausarbeiten: äußerer Maskenrand sowie Wangen-/Mittelstegübergang.
   Das ist die explizite weitere Zuständigkeit für Gesichts-Federfinish, keine
   erneute Ringmasken-/Querbrauenkonstruktion. Logo 00/Parts 08; separate Augen,
   nichtlinearen vollständigen Blink, ±12° Blick und 0–18° Beak erneut prüfen.

## Architekturhinweise, keine vorgeschriebene neue Konstruktion

`PRI_HeadNeckTorso` hat vorbereitete Gruppen `wing_root_L/R`; die dokumentierten
Root-Zentren sind (±0,085, −0,018, 0,307) m, Radius 0,045 m bei Referenzhöhe 0,45 m.
Die #15-Probe verschob den Root-Bereich um 12 mm. Diese Parameter und Gewichte sind
ein Anhaltspunkt, kein fertiges Wing-Rig und keine Bestätigung der neuen Lagen.

Eine mögliche Bindung sind eigene Root-Pivots plus lokale Federlagen oder
gemeinsame Deformationsgewichte. Auswahl, Kontakt-/Überlappungsabsicht und Pose-
Grenzen in JSON und `docs/decisions.md` festhalten. Beabsichtigte offene Karten und
Federüberlappungen von unbeabsichtigten Kollisionen unterscheiden; der bestehende
Closed-Surface-Auditor darf nicht unverändert auf alle Karten erzwungen werden.

Der generische Smoke führt numerische Stufen in sortierter Reihenfolge aus:
`30_wings_feathers.py` läuft vor `40_feet_perch.py`. Ein eigener #6-Review-Runner
soll dagegen vom akzeptierten #5 ausgehen. Beide Ablaufarten berücksichtigen;
keine bestehenden Produktionsprüfungen durch stilles Überspringen ersetzen.
`project.py` und mehrere gemeinsam genutzte Helfer sind in alten Reviews
hashgebunden. Neue Helfer bevorzugen; bei nötigen Änderungen die Nachweiskette
ehrlich erhalten, nicht nur gespeicherte Hashes umschreiben.

Die alten `face_review.py`/`beak_review.py`/`feet_review.py`/`history_bindings.py`
bleiben historische Version 1. Aktuelle Abnahme nutzt `delivery_gates.py` und
`history_gate.py` (Version 2), eigene vollständige Quellen-/Referenz-/Reload-
Inventare und typisierte Vergleichsfelder. Leere/verkürzte Maps, identische
Null-/Leerwerte und fehlende Unterfelder negativ prüfen. Historische Daten nicht
aus einer gerade gelieferten Map als ihren eigenen Pflichtumfang ableiten.

Weitere konkrete QA-Zuständigkeiten: [Folgeprüfungen #20–#24](review-fixes-qa-followup.md).

Für neue Feather-Objekte einen eigenen Präfix wählen: `GRP_` gehört derzeit dem
Fuß-Verifier, der alle so benannten Objekte als Fuß-/Stangenflächen untersucht.
Alte Gesamt-Verifier für #15/#16 erwarten ihre historischen Guide-Namen; aus ihnen
die passenden generischen Mesh-Audits übernehmen, nicht die komplette alte
Szenenprüfung auf den neuen Blend anwenden.

## Liefer- und Abschlussnachweise

| Anforderung | Zu liefernder Beleg |
|---|---|
| Reale Flügel/Körper-/Schwanzlagen | ausführbare `30_wings_feathers.py`-Stufe, versionierte Parameter, bearbeitbarer LFS-Blend |
| Symmetrie/Wiederverwendung | nachvollziehbarer Komponentenaufbau und tatsächliche Geometrieprüfung |
| Gestenfähigkeit | beschriebene Bindung plus geprüfte reale Pose-/Layer-Motion, keine alleinige Policy-Property |
| Saubere Kontur / Referenztreue | Front, Linksprofil, Rücken, 3/4 in unverändertem Studio plus geschriebene Befunde |
| Anatomie / unveränderte Bereiche | Mesh-/Transform-/Material-/Modifier-Nachweise, weiterhin echte Foot-Contact-Prüfung |
| Reproduzierbarkeit | wiederholter Build, gespeicherte Datei in frischen Blender-Prozessen öffnen; Neutral- und Poseproben prüfen |
| Dokumentation | `docs/decisions.md`, dauerhafter Federbericht mit Befehlen, Ergebnissen, Abweichungen und Grenzen |
| Integration | relevante neue Gates, alle bisherigen Tests, Projektvalidierung, compileall, Blender-Smoke, eigener grüner PR |

Geeignete neue Artefaktnamen stehen in der [Repo-Karte](repository-map.md).
Die automatischen Proofs und die nach tatsächlicher Bildinspektion verfasste
visuelle Entscheidung getrennt halten. `design_approval=false` in generierten
Dateien bedeutet nicht, dass ein visueller Review entfallen darf.

Finale Materialien/Tech-Motive folgen #18, Augenlookdev #19, vollständige
Topologieprüfung #20 und Rig #21–#23. Nach Lieferung/Merge #6 und Epic #11
aktualisieren; erst dann ist #18 startbereit.

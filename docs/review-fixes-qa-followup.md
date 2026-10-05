# Prüfzuständigkeiten nach #37

IR-04 beschreibt Prüfgrenzen, keine pauschale Produktionsfreigabe. Aktueller
Nachweis: [Korrekturbericht](../validation/reviews/review_fixes_v01/report.md).
Die unten genannten Rig-Prüfungen sind **deferred** bis zu ihrem jeweiligen Goal.
Keine Druckflächen-/Lastsimulation und keine Flugartikulation sind erforderlich.

Fortschreibung 2026-10-05: #6 liefert die zugewiesenen großen Cream-Gesichts-
und vollständigen Flügel-/Körper-/Schwanzgruppen. Neue tatsächliche Blink/Blick/
Beak-, Root-/Gesten- und Griffproben bestehen; unabhängige Reviews sind geschlossen.
[Federbericht](../validation/reviews/feathers_v01/report.md). Die folgende #6-Zeile
bleibt als ursprünglicher Umfang erhalten; #20–#24 sind weiterhin offen.

| Goal | Konkrete spätere Abnahme |
|---|---|
| [#6](https://github.com/KreutzM/Owli-3d/issues/6) | Große Gesichtsfederzüge für den verbliebenen äußeren cream Rand und Wangen-/Mittelstegfluss ausdrücklich mitliefern. Wenige breite, bearbeitbare Gruppen; primäre organische #37-Maske erhalten. Blink/Blick/Beak erneut prüfen. Vollständige Flügel-/Körper-/Schwanzlagen und Gestenbindung bleiben zusätzlich verbindlich. |
| [#20](https://github.com/KreutzM/Owli-3d/issues/20) | Gesamte finale Topologie: adjazente Faltungen und coplanare Überlappungen, Cage und evaluierte Flächen, besonders Hals/Lider/Wing Roots. Beabsichtigte Federkarten/-überlappungen und eingebettete Wurzeln einzeln klassifizieren. Nicht den Shared-Vertex-BVH-Filter als universellen Selbstschnittbeweis ausgeben. |
| [#21](https://github.com/KreutzM/Owli-3d/issues/21) | Tatsächlich gebundene Kopfneigung ±15°, Drehung ±20° und dokumentierte Body-Lean-Grenzen mit allen Gesichtsanbauten durchführen. Augen/Masken/Tech/Schnabel folgen dem Kopf; keine offenen Anschlüsse. Root bewegt Owli relativ zur stationären Stange, noch keine pauschale Kontaktgarantie bei ungeprüfter Fußsteuerung. Neutral-Rückkehr und frisches Reload nachweisen. |
| [#22](https://github.com/KreutzM/Owli-3d/issues/22) | Kombinierte Kopf-/Blick-/Blink-/Beak-Matrix: beide Kopfneigungs-/Drehgrenzen, ±12° Blick über beide Achsen, Blink 0/0.5/1, Schnabel 0/9/18°. Auswahl inklusive ungünstiger Kombinationen konkret versionieren; echte Lid/Cornea-Clearance, vollständige Closure, Masken-/Beak-Schnitte prüfen. Nichtlineare Lidbewegung und korrekt folgende Pivots/Driver nach Save/Reload. |
| [#23](https://github.com/KreutzM/Owli-3d/issues/23) | #22-Matrix mit linker/rechter Erklärgeste bei Neutral/Halb/Grenze und Body-Lean kombinieren. Flügel und sichtbare Lagen folgen gemeinsam; Wurzelkontakte und unbeabsichtigte Schnitte klassifizieren. Auf echten neutralen Perch-Posen 3+1-Verzweigungen, opposed grip, acht Krallen-/Bar-Kontakte und Padkontakt prüfen; Controls neutral zurückstellen. Animierte Abhebungen ausdrücklich als solche kennzeichnen. |
| [#24](https://github.com/KreutzM/Owli-3d/issues/24) | Vollständiges finales Rig und benannte Actions erneut öffnen; alle Pflichtcontrols und dokumentierten Kombinationsgrenzen prüfen. Keyframes und Zwischenframes aller finalen Clips auf Durchdringungen, Closure, ruhige Gesten und Kontaktverlust untersuchen. Vier unveränderte Referenzkameras; endgültige Grenzen/Abweichungen mit Ressourcen- und Reproduktionsnachweisen in finaler Übergabe festhalten. |

Die #37-Flächenprüfung verwendet Dreiecksinnenflächen mit einem relativen Inset
von 0,001, eine zusätzliche coplanare 2D-Schnittprüfung und reale Negativfixtures.
Der tatsächlich größte Inset wird pro Mesh dokumentiert; Faltungen unter diesem
Abstand sowie coplanare Flächen unter 1e-12 m²/1e-8 m Ebenentoleranz werden nicht
universell ausgeschlossen. Die positive Closure-/Clearance-/Grip-Prüfung bleibt
zusätzlich erforderlich. Ein punktueller Padkontakt ist geometrischer Support,
keine Behauptung eines Druckflächen- oder Physikmodells.

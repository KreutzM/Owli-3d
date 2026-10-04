# Unabhängiges Owli-Zwischenreview nach #5

**Urteil: technisch belastbarer, reproduzierbarer Zwischenstand; #6 ist bedingt
fortsetzbar. Die organische Gesichtsintegration ist visuell noch nicht überzeugend.**
Kein technischer Blocker für die Flügel-/Rückenarbeit wurde festgestellt. Vor
verbindlicher Detailbindung ist IR-01 einem konkreten Liefergoal zuzuordnen;
vor Abnahme neuer Nachweise ist IR-02 zu beheben. Dies ist keine fertige V1-Freigabe
und keine nachträgliche Änderung früherer Meilensteinentscheidungen.

Auftrag: [#33](https://github.com/KreutzM/Owli-3d/issues/33), Parent
[#11](https://github.com/KreutzM/Owli-3d/issues/11). Folgearbeit:
[#34 / IR-01](https://github.com/KreutzM/Owli-3d/issues/34) und
[#35 / IR-02–03](https://github.com/KreutzM/Owli-3d/issues/35).

## Prüfstand, Unabhängigkeit und Methode

- Datum: **2026-10-04**, Prüfung ab ca. 14:49 UTC.
- Vollständiger geprüfter Commit: **`ee48046b792e3647f454bc4223788271283542b9`**.
  Nach `git fetch origin` entsprach `origin/main` diesem Commit. Keine neueren
  Produktionsänderungen gegenüber der vorgesehenen Baseline. Anfangs sauberer
  Arbeitsbaum; eigener Dokumentationsbranch `review/33-independent-interim`.
- Modellierungscommit: `8dcbebac1e8df0487246f818cdd0c3396c9f5265` (PR #31).
- Tatsächlich geöffnet: `blender/scene/owli_feet_v01.blend`, **1.020.254 Bytes**, SHA256
  **`0fb1512b3a27c4ebe5b7cbdebf520643b7208f2c74f8a847545ffc51dda66797`**.
  Echte Blend-Datei, kein LFS-Pointer. Hash vor/nach read-only Prüfungen identisch.
- Reviewer: frischer Codex-Review-Agent `/root`; getrennte frische Reviewer
  `/root/history_audit` für Provenienz und `/root/reproduction_audit` für
  Werkzeuge/Gates. Keiner dieser Reviewer implementierte die geprüften Milestones.
  Getrennte Scope-Ergebnisse wurden anhand der Primärbelege zusammengeführt.
- Umgebung: Windows; Python **3.11.9**, Pillow **12.2.0**, Git
  **2.53.0.windows.3**, Git LFS **3.7.1**, Blender **5.2.1 LTS**, Build
  **`9e2066aef7ef`**. Blender-Pfad:
  `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`.
  FFmpeg, gh und Make vorhanden; Git/SSH und GitHub-Connector funktionieren.
  Der lokale gh-Token liefert **401**: CLI-Verfügbarkeit ist keine Authentifizierung.

Die acht Pflichtquellen wurden in vorgeschriebener Reihenfolge gelesen, danach
Übergabe, Repo-Karte, Entscheidungen, #6-Startplan und die aktuellen Issues
#33/#11/#6. Logo 00, Turnaround 07, Parts 08 und Beauty 01 wurden tatsächlich
betrachtet. Original-Logo regelt Identität/Gesicht/Farbe, 07 Volumen/Profil/Rücken,
08 Konstruktion; Beauty ergänzt die Stilbeurteilung. Keine Mittelung widersprüchlicher
Referenzen, kein neues Konzeptbild, kein geänderter Freeze.

Eigene Evidenz liegt unter
[`validation/reviews/independent_interim_after_feet/`](../../validation/reviews/independent_interim_after_feet/README.md).
Die Szene wurde in zwei frischen Blender-Prozessen geöffnet; ein dritter prüfte
Bewegungsproben. Alle vier **gespeicherten** Kameras wurden verwendet. Vor dem
Rendern wurde bewiesen, dass der gespeicherte Studiozustand exakt der kanonischen
Konfiguration entspricht; Setup änderte weder Studio noch Mesh-Signaturen.
Neue neutrale Pixel stimmen zwischen beiden Prozessen **und** mit den vorhandenen
#5-Renderings überein. Der komplette #5-Build wurde zusätzlich von einer Kopie der
akzeptierten #17-Szene in Scratch ausgeführt und zweimal frisch wieder geöffnet.
Kein akzeptierter Blend, PNG, Parameter oder historischer Review wurde überschrieben.

## Abdeckungsmatrix

`pass` gilt nur für den angegebenen Prüfbereich; `fail` benennt einen belegten
Befund; `unverified` bezeichnet fehlende ausreichende Prüfung; `deferred` ist
ausdrücklich späterer Lieferumfang. Ein Bereich kann deshalb mehrere Status tragen.

| Prüfbereich aus #33 | Status | Primärbelege und Ergebnis |
|---|---|---|
| 1. Anforderungen/Referenztreue | **fail: IR-01**; Teilanforderungen pass; Lookdev deferred | Eigene Front/Profil/Back/3Q-Boards: dominanter Kopf, große separate cyan/blaue Augen, sichtbare helle Maske, orange Schnabel/Brustakzente und kompakte Perch-Pose vorhanden. Organische Gesichtsscheibe/freundliche neutrale Brauen noch schwach; siehe visuelle Einzelbefunde. |
| 2. Tatsächliche Szene | **pass** | Zwei unabhängige Inventare identisch, vier unveränderte Kameras, fünf Lichter, 62 Objekte/50 Meshes, Framing bestanden; keine versteckten Meshes, losen Meshteile, Orphan-Meshes oder Fremdbibliotheken. Keine ungelöste externe Bildressource. |
| 3. Abgeschlossene Geometrie | **pass im neutralen Zustand und getesteten Proben**; kombinierte Rig-Posen deferred | Cage-/evaluierte Topologie, echte 3+1-Verzweigungen, acht separate Krallen, Kontakt/Halfspaces/Clipping, 45 Fußpaare, 41 Blink- und 41 Schnabelzustände, Blick-/Kopf-/Root-Proben. Keine universelle Kollisions-/Physikfreigabe. |
| 4. Skripte/Reproduktion | **pass**; kontinuierlicher Parameterraum unverified | Vollständige Scratch-Reproduktion mit Repeat/0,5×/2×/Negativproben und zwei Reloads; Bild-/Build-Ergebnisse identisch zur Lieferung. Fünf erlaubte Radius/Spacing-Konfigurationen zusätzlich geprüft; vier außerhalb abgewiesen. |
| 5. Nachweise/Historie | Aktueller Inhalt/Migration **pass**; Gate-Vollständigkeit **fail: IR-02**; Vertrauensgrenze IR-03 | Zwei Archive und zwölf Snapshots gegen echte Vorgänger-Git-Bytes geprüft; 240 weitere Vorgängerdateien unverändert. Aktuelle Hash-/Referenztabellen vollständig vorhanden. Omission-Proben zeigen zukünftige Schema-Lücken. |
| 6. Repository/Werkzeuge/Übergabe | **pass**; gh-CLI-Zugriff fail; lokale Linux-/andere Blender-Ausführung unverified | Doctor, Tests, CI-Quellen, aktuelles Inventar und Issues geprüft. Die dokumentierten Runner-Fallen stimmen mit dem Code überein; nutzbarer GitHub-Connector kompensiert den 401-Zugriff. |
| 7. Fortsetzungsfähigkeit #6 | **pass mit konkreten Bedingungen** | Aktuelle #5-Szene ist belastbarer Ausgangspunkt. IR-01 vor Detailbindung zuordnen; IR-02 vor neuen Abnahmen beheben. Eigener #6-Runner und Smoke-Reihenfolge berücksichtigen. |
| Finale Federlagen/Lookdev/Topologieabnahme/Rig/Animation/Übergabe | **deferred** | #6/#18/#19/#20/#21/#22/#23/#9/#24. Leere FEATHERS/RIG, Diagnosematerialien und fehlende Actions sind korrekt dokumentierter Zwischenstand. |

## Visuelle Referenzprüfung

Die [Vieransichtenübersicht](../../validation/reviews/independent_interim_after_feet/contact_sheet.png)
zeigt die tatsächliche Szene, nicht ein neu erzeugtes Konzept.

- **Front:** [Vergleich](../../validation/reviews/independent_interim_after_feet/VAL_FRONT_comparison.png).
  Symmetrische sitzende Eule, Kopf visuell dominant, große Augen, klare helle
  Flächen und sparsame Orangeverteilung. Navy-Körper/Blue-Flügel sind organische
  Volumen, keine Metallschale. Gegen Logo 00 fehlt jedoch die zusammenhängende,
  breit auslaufende cream Gesichtsscheibe: helle ringförmige Fassungen und schmaler
  Mittelsteg bestimmen die Form. Dunkle querliegende Brauen wirken strenger als
  der aufmerksame Logoausdruck. Das ist IR-01, keine Behauptung kleiner/fehlender Augen.
- **Linksprofil:** [Vergleich](../../validation/reviews/independent_interim_after_feet/VAL_LEFT_comparison.png).
  Rundes Kopfvolumen, körpernaher gefalteter Flügel, kurzer nach unten laufender
  Schwanz und hakenförmiger orangefarbener Schnabel sind lesbar. Das cream Socket
  erscheint als fast senkrechte aufgesetzte Scheibe mit sichtbarer seitlicher
  Tiefe; die organische Wangen-/Brow-Integration aus 07/08 fehlt noch. Der hintere
  Zehenhaken liegt tatsächlich auf der Rückseite der Stange und läuft unter deren
  Mitte, nicht als vierter Vorderhaken. Die Referenzen sind keine exakten Orthoprojektionen.
- **Rücken:** [Vergleich](../../validation/reviews/independent_interim_after_feet/VAL_BACK_comparison.png).
  Symmetrische Flügel, zentrierter Schwanz und Kopfkörperfolge vorhanden.
  Rücken/Flügel sind weiterhin große glatte Massen; Layering/Cyan-Tipps gehören
  #6. Der schmale cream Rand an beiden Kopfseiten ist sichtbar und bereits
  dokumentiert. Die oben sichtbaren cyan Punkte gehören zum vorderen Graphen;
  keine zweite Rückensignatur modelliert. Das widersprüchliche Graphzeichen in
  Turnaround 07 überstimmt Logo/Spezifikation nicht.
- **3/4 vorne:** [Vergleich](../../validation/reviews/independent_interim_after_feet/VAL_3Q_comparison.png).
  Beide Augen behalten Volumen, Schnabelprojektion und Perch-Griff bleiben sichtbar.
  Aufgesetzte Maskenringe, getrennte Orange-/Brustmassen und glatte Horn-/Brauenmassen
  reduzieren derzeit die Markenähnlichkeit. Beauty 01 unterstützt die Stilbeurteilung;
  der technische 3/4-Referenzpanel zeigt die andere Seite und wurde weder gespiegelt
  noch metrisch ausgerichtet. Rückkrallenspitzen sind teilweise natürlich verdeckt;
  [isolierte Zehen](../../validation/reviews/independent_interim_after_feet/toes/VAL_3Q.png)
  ergänzen die unveränderte Gesamtansicht.

Fehlende irisinterne Netzwerkstruktur, Glanz/Tiefenwirkung, Feder-Cyanverteilung,
subtile Stirnemission und Metall/Cyan-Stangenfinish sind **deferred**, keine Fehler
abgeschlossener Geometrie. Die starke Ringform/harte Brauen sind dagegen sichtbare
Form- und Integrationsfragen. Shader allein belegen ihre spätere Lösung nicht.

## Tatsächliche Szene und Geometrie

[Eigenes Inventar](../../validation/reviews/independent_interim_after_feet/scene-inspection.json)
bestätigt die Übergabe: 50 Meshes, vier Kameras, fünf Lichter, drei Empty-Pivots;
keine Armature, keine Actions. Sieben tatsächlich benutzte Diagnosematerialien.
FEATHERS, RIG und CLAWS leer; die Krallen liegen in FEET. Alle 50 Meshes haben
eine zusammenhängende geschlossene Fläche, konsistente Kantenorientierung,
positive signierte Volumina, keine losen Vertices/Edges oder degenerierten Faces
im Cage und in den evaluierten neutralen Flächen. Iris-/Maskenannuli haben
absichtlich Genus eins. Primär-/Fußflächen bleiben editierbar; rigid animierte
Augenpole und planare Schnabelcaps benötigen keine deformierende Quadlattice.

Meter/Z-oben/+Y-vorne sind konsistent. Evaluierte Gesamtgrenzen einschließlich
Stange und Stirnguide: X ±0,185 m, Y −0,133677…0,153418 m, Z 0…0,542744 m.
Die JSON-Referenzhöhe 0,45 m ist ein globales Rezeptmaß, keine strikte
Fuß-bis-Kronen-Höhe; dies ist in den Entscheidungen bereits erklärt. Eltern-/lokale
Transformationen der Augen und unteren Kieferhälfte sind Teil der Pivotkonstruktion;
keine zufälligen Transformreste wurden festgestellt.

Keine externe Library, kein externes Shaderbild. Zwei VIEWER-Image-Datablocks
(`Render Result`, `Viewer Node`) sind Blender-Laufzeitpuffer, keine fehlenden Assets.
50 Mesh-Datablocks/50 Meshobjekte, keine verwaisten Meshes, keine Objekte außerhalb
der geladenen Szene. Das eigene Inventar bestätigt das versionierte Übergabeinventar.

Die gesamte neutrale Szene wurde über **1.225 Meshpaare** mit evaluierten
World-Surface-BVHs gescannt; **65 Paare** melden Berührung/Überschneidung. Dies ist
keine Liste von 65 Defekten: Brust/Flügel/Schwanz/Brow/Tuft-Wurzeln und Globe sitzen
absichtlich im Körper; Masken-/Lid-/Bridge-Interfaces überlappen für den Anschluss;
Netzwerklinks treffen Nodes. Fußankles stecken im Körper, Stem trifft Bar/Base.
Toe-Claw-Caps und Stangenkontakt erzeugen ebenfalls BVH-Treffer. Für diese
Fußkontakte prüft der spezielle Verifier gemeinsame Cap-Grenzen und exakte
Bar-Halfspaces/Innenraum-Clipping. Augenlagen untereinander und der Schnabel mit
der Maske erzeugen keine unerlaubten Surface-Treffer. Die Kontaktklassifikation
rechtfertigt **keine** pauschale Boolean-/Containment- oder spätere Posefreigabe.
Generische Selbstschnittprüfer ignorieren Facepaare mit gemeinsamem Vertex;
adjazente Faltungen und kombinierte Posen benötigen spätere gezielte QA (IR-04).

[Bewegungsproben](../../validation/reviews/independent_interim_after_feet/movement-probes.json)
wurden auf dem tatsächlichen #5-Blend ausgeführt, unter Wiederverwendung kompatibler
geometrischer Helfer. Historische Gesamt-Inspector mit ersetzten GUIDE-Namen wurden
bewusst nicht als aktuellen Gesamtcheck verwendet:

- Kopfneigung 15°, Kopfdrehung 20°, Root-Verschiebungen je 12 mm: Cage und
  evaluierte Primärfläche bestehen; Edge-Ratios insgesamt 0,7565…1,2503.
  Offene Fläche, umgedrehte Face, loser Vertex und Asymmetrie werden abgewiesen.
  Dies bewegt die Prüfhaut, noch nicht sämtliche Gesichtsteile durch ein Rig.
- **41** Blinkzustände: kleinster tatsächlicher Dreiecksabstand zur Cornea
  **1,024827 mm** (Anforderung 0,3 mm). **10.034** Aperturrays bedeckt;
  vollständige Vorder-/Rückseam geschlossen. Eigene
  [Blinkansicht](../../validation/reviews/independent_interim_after_feet/blink/VAL_FRONT.png).
  Vier ±12° Pitch/Yaw-Proben bestanden. Nichtlineare Lidrekonstruktion ist
  erforderlich; lineare Shape-Key-Interpolation ist kein äquivalenter Rig.
- **41** Schnabelzustände über 0–18°, **2.337** Kollisionschecks:
  Oberteil bleibt fest, Unterkiefer bewegt sich real (max. **21,502 mm**),
  vorderer Vertex fällt **10,958 mm**. Minimaler beidseitig gesampelter
  Maskenabstand **5,614 mm**. Eigene
  [offene Profilansicht](../../validation/reviews/independent_interim_after_feet/beak_open/VAL_LEFT.png).
- Pro Fuß eine verbundene Haut mit **drei Front- und einer Rear-Verzweigung**,
  acht separate geschlossene Krallen. Reale Branch-Adjazenz und Lage beiderseits
  der Stange geprüft; größte minimale Krallen-Bar-Distanz **7,45 Nanometer**, unter
  der 0,2-µm-Floattoleranz. Der Pad berührt die Krone (bei Neutral je ein exakt
  passender Cage-Vertex), Zehen/Krallen folgen der realen 128-seitigen Bar.
  **45** getrennte Fuß-/Krallenpaare bestanden. Dies belegt geometrischen
  Kontakt und plausible Gegenhaken, keine Druckfläche/Lastsimulation oder
  bereits gewichtete Beinmechanik. Solche Physiksimulation ist kein V1-Auftrag.

## Reproduktion, Nachweiskette und CI

[Frische #5-Reproduktion](../../validation/reviews/independent_interim_after_feet/feet-comparison.json):
Build-Checks stimmen vollständig mit dem akzeptierten Datensatz überein,
einschließlich 37 unveränderter Vorgängermeshes, drei Pivots, wiederholtem Build,
0,5×/2×-Skalierung und beiden Produktionsparameterproben. Tatsächlich verschobene
Rückkralle wird als schwebend, penetrant bzw. auf falscher Stangenseite abgewiesen.
Beide Reload-Checks und die vier 1024px-Renders stimmen exakt mit Build und
akzeptierter Lieferung überein. Unterschiedliche neu gespeicherte Blend-Containerbytes
werden nicht mit geometrischer Nichtdeterministik gleichgesetzt.

Zusätzlich [vier Parameterecken und Mittelpunkt](../../validation/reviews/independent_interim_after_feet/parameter-corners.json)
geprüft: (Radius/Halbspacing in m) `(0.016,0.050)`, `(0.016,0.062)`,
`(0.022,0.050)`, `(0.022,0.062)`, `(0.019,0.056)`; jeweils echte Kontakte und
45 Kollisionspaare pass. Vier knapp außerhalb der Bereiche liegende Werte abgewiesen.
Der Produktionsprobe testet nur zwei diagonale Ecken; diese Grenze wurde im
Review ergänzt, ohne historische Quellen zu ändern. Kein Beweis für jeden Wert
des kontinuierlichen Parameterraums oder jede neue visuelle Proportion.

[Historischer Audit](../../validation/reviews/independent_interim_after_feet/history-audit-evidence.json)
verwendet tatsächliche Git-Bytes aus
`84bee42c19e12af090b5d1d741dccf81f7fee800` (vor #5), unabhängig vom Manifest:
zwei Archive bytegleich, zwölf Original-JSON-Snapshots bytegleich. Alle live
JSON-Differenzen sind ausschließlich Dependency-Pfadumzüge und daraus folgende
Hash-Kaskaden; Kriterien, Gründe, Ergebnisse und Referenzränge unverändert.
Weitere **240** Vorgängerdateien unverändert, darunter **193 PNGs und fünf Blenddateien**.
Bei den Blenddateien wurden echte Bytes/Größe mit den früheren LFS-OIDs verglichen.
[Coarse-Dispatch](../../validation/reviews/independent_interim_after_feet/coarse-dispatch.json)
liefert in Scratch identische Geometrie/Transforms/Materialindices/Normals/Properties
und `[55,47,7]` Objekt-/Mesh-/Materialcounts. Dies bewahrt alte Evidenz, bestätigt
aber nicht automatisch deren damalige visuelle Urteile neu.

Hashes binden Bytes. Sie beweisen allein weder korrekte Algorithmen noch durchgeführte
Geometrieprüfung noch passende Referenzinterpretation. PNG-Hashes binden Bilder,
nicht deren Designqualität. Deshalb wurden die aktuellen Pixel neu erzeugt,
Primärdaten gelesen und die technischen Proben tatsächlich wiederholt. IR-02/03
begrenzen die weitergehenden Garantien der gespeicherten Gate-Metadaten.

CI ist laut `.github/workflows/validate.yml` Windows/Ubuntu mit Python 3.12,
LFS-Checkout, Requirements, Projektvalidierung, Compileall und Tests. **Kein Blender**
wird installiert/ausgeführt. Die lokale unabhängige Blender-Evidenz trägt die
Laufzeit-/Geometrieaussagen. Grüner Smoke erzeugt ein Rig-/Materialgerüst in
Scratch; er bedeutet weder zugewiesene finale Shader noch fertige Feather-/Rigarbeit.

### Ausgeführte Befehle

Alle folgenden erfolgreichen Prüfungen hatten **Exit 0**. Vollständige Logs und
Argv stehen in der Evidenz; die eigenen Prüfskripte sind ebenfalls versioniert.
Arbeitsverzeichnis ist das Repository, außer explizit Scratch. Erstaufrufe
`gh issue view ... --json ...` für #33/#11 scheiterten mit **Exit 1 / HTTP 401**;
anschließende Connector-Reads waren erfolgreich. `git fetch` war zunächst im
Sandboxkontext verweigert, danach autorisiert erfolgreich; kein Produktionsfehler.

| Befehl/Prüfung | Ergebnis und Grenze |
|---|---|
| `python scripts/project.py doctor` | Versionen, Tools, neun Referenzen gültig |
| `python scripts/project.py validate` | Strikte Referenz-/Policy-/Studio-Validierung bestanden |
| `python -m unittest discover -s tests -v` | 25 Tests bestanden; erwarteter Scene-exists-Negativtest ist kein Laufabbruch |
| `python -m compileall -q scripts` | Kompilierung bestanden |
| `python scripts/project.py smoke` | Vollständige sortierte Stufen, tatsächlicher Foot-Inspector, vier 64px-Renders; ausschließlich Scratch |
| Blender `--background …owli_feet_v01.blend --python-exit-code 1 --python …/inspect_scene.py` | Zweimal neutral, einmal MODE=probes; Inventar, Topologie, Framing, vier feste 1024px-Views |
| `python validation/reviews/independent_interim_after_feet/reproduce_feet.py --output tmp/independent-review-33/feet-reproduction` | Vollständiger #5-Build plus zwei frische Reloads, identische Checks/Pixel |
| `python …/history_audit.py` | Git-Bytevergleich und kontrollierte Omission-/Korruptionsproben |
| Blender `--background …owli_feet_v01.blend --python-exit-code 1 --python …/parameter_corners.py` | Vier Ecken, Mittelpunkt, vier ungültige Werte |
| Blender `--background --factory-startup --python-exit-code 1 --python …/history_coarse.py`, CWD Scratch | Archivierter/current Coarse-Dispatch identisch |

Vollständig ausführbare Befehle mit Pfaden/Umgebungsvariablen stehen im
[Evidenz-README](../../validation/reviews/independent_interim_after_feet/README.md).
Die beiden archivierten Hilfsskripte wurden nach dauerhafter Ablage erneut
ausgeführt; ROOT-/Output-Pfade wurden für den neuen Speicherort angepasst.

## Priorisierte Findings

### IR-01 — major — Organische Gesichtsform und Integrationsauftrag fehlen

**Ort:** `FAC_Mask_L/R`, `FAC_MaskBridge`, `PRI_Brow_L/R`; Front/Links/3Q.
**Beleg/Reproduktion:** tatsächliche Szene mit `inspect_scene.py` rendern;
die oben verlinkten eigenen Vergleichsboards gegen Logo 00 und 07/08 ansehen.
Die Ringfassungen mit sichtbarer Tiefe, der schmale Mittelsteg und dunkle
Querbrauen ergeben eine mechanischere/strengere Gesichtssprache. Helle Flächen
und große Augen sind vorhanden, ihre organische Verbindung ist schwach.
**Auswirkung:** Marken-/Freundlichkeitsqualität und spätere Gesichtsfederbindung
sind nicht durch bestandene Topologie-/Blinktests abgesichert.
`face_v01/report.md` verweist für die Glättung auf spätere Gesichtsfedern;
#6/Startplan nennen hingegen ausdrücklich Flügel/Körper/Schwanz. Ein klarer
Lieferauftrag für diese Gesichtsintegration fehlt.
**Handlung:** [#34](https://github.com/KreutzM/Owli-3d/issues/34) vor Detailbindung
zuordnen und entscheiden. Geometriekorrekturen separat parametrisieren und mit
unveränderten vier Views neu beurteilen, ohne alte Freigaben umzuschreiben.
Augenschichten/Blink/Beak-Clearance erhalten. Unabhängige Flügel-/Rückenarbeit aus
#6 kann beginnen; finale Oberflächenabnahme darf IR-01 nicht als automatisch gelöst behandeln.

### IR-02 — minor — Delivery-Gates erzwingen den vollständigen Tabellenumfang nicht

**Ort:** `scripts/face_review.py`, `beak_review.py`, `feet_review.py` und Tests.
**Beleg/Reproduktion:** `history_audit.py`, Abschnitt `delivery_probes` im
eigenen JSON. Auf tiefen Proof-Kopien akzeptieren alle drei Validatoren
`reference_sha256={}` und `reloaded={}` weiterhin mit `[]`; Face/Beak zusätzlich
`source_sha256={}`. Feet erzwingt neun Pflichtquellen, nicht das gesamte aktuelle
24-Quellen-Inventar.
**Auswirkung:** `.items()` prüft deklarierte Einträge, garantiert nicht die
Vollständigkeit einer zukünftigen neu erstellten/neu gebundenen Lieferung.
Die aktuellen echten Tabellen sind gefüllt/hashrichtig; diese In-Memory-Proben
belegen **keine** unbemerkte Änderung gespeicherter Approvaldateien oder grüne
Gesamt-CI nach Dateikorruption.
**Handlung:** [#35](https://github.com/KreutzM/Owli-3d/issues/35): Pflichtsets und
fehlende Einzelkeys/Leer-Tabellen negativ testen, bevor das Muster #6 abnimmt.
Historische Source-/Approval-Bindungen dabei ehrlich erhalten.

### IR-03 — observation — History-Gate setzt ein vertrauenswürdiges Inventar voraus

**Ort:** `scripts/history_bindings.py`, `validation/history/pre_feet_v01/manifest.json`.
**Beleg/Reproduktion:** beide Relocation-Maps in einer Scratch-Kopie leeren;
Standalone-Validator liefert trotz dort geänderter Archiv-/Entscheidungsdatei `[]`.
Einzeln entfernte Einträge werden durch abhängige Beziehungen teilweise erkannt;
fehlender Snapshot löst `FileNotFoundError` aus und scheitert geschlossen.
**Auswirkung:** der Validator ist kein unabhängiger Git-Ancestry-/Vollständigkeitsbeweis.
Feet bindet das Manifest zusätzlich; diese Beobachtung ist kein nachgewiesener
Bypass der unveränderten gesamten Lieferkette. Der echte Vorgängerbytevergleich
dieses Reviews bestätigt die aktuelle Migration dennoch.
**Handlung:** bei nächster Gate-/Migrationsarbeit (#35) Pflichtinventar,
Predecessor-Verankerung und erlaubte Dependency-Felder erzwingen. Keine Historie neu modellieren.

### IR-04 — observation — Begrenzte Mesh-/Pose-/Kontaktprüfungen

**Ort:** `verify_face.audit`, `verify_primary.audit_mesh`, `verify_feet.inspect`;
eigene `scene-inspection.json`/`movement-probes.json`.
**Beleg/Reproduktion:** Self-BVH-Filter ignorieren alle Facepaare mit gemeinsamem
Vertex. Die Szene enthält absichtliche Root-/Socket-Überlappungen und punktuellen
Padkontakt. Bestehende Poseproben testen getrennte Zustände, kein vollständiges
gebundenes Avatar-Rig. Der Produktionsfootprobe testet zwei diagonale Parametergrenzen;
die übrigen Ecken bestanden dieses unabhängige Review.
**Auswirkung:** keine universelle Adjacent-Fold-, Containment-, Last-/Druckflächen-
oder kombinierte Rig-Posegarantie. Kein aktueller zusätzlicher Defekt belegt.
**Handlung:** #20/#21–23/#24 für gezielte kombinierte Deformation und
Attachment-/Kontaktklassifikation nutzen; keine Flug- oder Physiksimulation hinzufügen.

### IR-05 — observation — Generische CLI ist kein beliebiger read-only Milestone-Editor

**Ort:** `scripts/project.py`, `90_validation.py`, `50_materials.py`, `60_rig.py`.
**Beleg/Reproduktion:** Dispatch/Save-Aufrufe lesen: `--scene/--output` nur für
`render`; Renderer speichert die geladene Datei. Material-/Rig-Gerüste speichern
nach `blender/scene/owli.blend`. Smoke sortiert #30 vor #40; der #6-Produktionsreview
muss hingegen von #5 ausgehen. `GRP_` ist im Foot-Inspector für Füße/Perch reserviert.
**Auswirkung:** unvorsichtige Wiederverwendung kann einen akzeptierten Stand ändern
oder am falschen Ziel arbeiten. Die Übergabe dokumentiert diese Fallen korrekt.
**Handlung:** eigene #6-Arbeitskopie/Runner, eigener Feather-Präfix und beide
Integrationspfade testen; keine bestehenden Gates still überspringen.

## Nächste Schritte und verbleibende Grenzen

1. #34 vor verbindlicher Gesicht-/Federdetailbindung einem konkreten Auftrag
   zuordnen. #6 kann seine unabhängigen Flügel-/Körper-/Schwanzarbeiten auf der
   unveränderten #5-Szene beginnen; kein Neustart abgeschlossener Milestones.
2. #35 vor neuer Nachweisabnahme bearbeiten. Änderungen an gebundenen Helfern
   benötigen eigene überprüfbare Gate-Lieferung bzw. ehrliche Provenienzmigration.
3. #6 liefert echte Flügel und große symmetrische/reusable Körper-/Schwanzlagen,
   dokumentierte Root-Bindung und tatsächliche gemeinsame Gestenprobe. Alle 37
   unbetroffenen Meshes/Pivots und 3+1-Griff erhalten, neue Vieransichtenbeurteilung.
4. Danach #18/#19 Lookdev, #20 Topologie, #21–23 Rig, #9 Animation und #24 finale QA.

Lokal nicht geprüft: Blender auf Linux oder anderen Versionen; jede kontinuierliche
Parameterkombination; fertig gebundene kombinierte Kopf/Auge/Beak/Wing-/Foot-Posen;
noch nicht existierende finale Shader, Actions, Benutzercontrols und Export für ein
unbestimmtes Zielsystem. Remote gh-CLI-Auth nicht verfügbar; Connector/Git nutzbar.
Kein manuelles Blender-UI-Editing erforderlich: echte Blend-Daten, evaluiertes
Blender-Mesh und Renderings wurden über dessen Python-Laufzeit inspiziert.
Diese Grenzen bleiben sichtbar und werden nicht aus Hashes oder CI extrapoliert.

Dieser Review beschreibt Untersuchung und separate Folgeaufgaben. Originaldateien,
Referenzautorität und historische Freigaben sind unverändert. Der Abschluss von
#33 ist eine Veröffentlichung dieses Reviews, kein Abschluss von #6 oder des V1-Epics.

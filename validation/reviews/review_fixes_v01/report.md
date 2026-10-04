# #37 — Review-Findings IR-01–05 nachgearbeitet

Neue bearbeitbare Szene: `blender/scene/owli_review_fixes_v01.blend`,
**1.068.211 Bytes**, SHA256
`8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`.
Ausgangspunkt: Review-Merge `473f8726d32ac7852ef93884b3010b52b8836521`,
akzeptierte #5-Szene SHA256
`0fb1512b3a27c4ebe5b7cbdebf520643b7208f2c74f8a847545ffc51dda66797`.
Auftrag [#37](https://github.com/KreutzM/Owli-3d/issues/37), Teilaufgaben #34/#35.

## Sichtbare Korrektur und Referenzentscheidung

Logo **00** regelt freundlich aufmerksame Gesichtssprache und zusammenhängende
helle Gesichtsscheibe; **07** regelt Kopfvolumen/Profil, **08** große cream
Gesichtsfederzüge. Die frühere runde Maskenfassung ist kein höherer Designrang.
Der grobe historische Freeze bleibt unverändert; diese neue Vieransichtenentscheidung
ersetzt für die fünf betroffenen Primärteile dessen damalige Forminterpretation.
Es wurden keine neuen allgemeinen Konzepte erzeugt oder widersprüchliche Quellen gemittelt.

`FAC_Mask_L/R` besitzen verbreiterte Wangen und einen an der realen unveränderten
Kopfoberfläche angepassten Außenrand. Die schwächere Ridge reduziert die aufgesetzte
Fassung. `FAC_MaskBridge` verbreitert sich unter dem Schnabel und verbindet die
Wangen mit der hellen Brust; kubisch interpolierte Ringschemata glätten den Mittelsteg.
`PRI_Brow_L/R` steigen als verjüngte gebogene Primärformen Richtung Ohrbüschel,
anstatt dunkle horizontale Querbalken zu bilden. `design/review_fixes.json` und
`review_fixes_geometry.py` parametrisieren die tatsächliche neue bearbeitbare Geometrie.

| Unveränderte Kamera | Tatsächlich geprüftes Ergebnis |
|---|---|
| [Front](VAL_FRONT.png) | Breite helle Wangen, cream Verbindung unter dem Schnabel; angehobene schmale Brauen. Große blue/cyan Augen bleiben primär, Neutralität wirkt freundlicher. Kleine äußere Formspitzen und Ringkonturen der unveränderten Blink-Lider bleiben für Federfinish sichtbar. |
| [Links](VAL_LEFT.png) | Wangen laufen hinter die vordere Augenöffnung zum tatsächlichen Kopf zurück; Schnabelprojektion bleibt erhalten. Die äußere cream Grenzkante ist noch deutlich und erhält ausdrücklich Gesichts-Federfinish in #6. |
| [Rücken](VAL_BACK.png) | Körper, Flügel, Schwanz, Perch und Sitzform erhalten; keine Gesichtskorrektur verändert die hintere Primärsilhouette. |
| [3/4](VAL_3Q.png) | Neue räumlich breite Wange und zentraler Übergang sind sichtbar; Augenlagen bleiben groß/getrennt und Schnabel frei. Die Verbindung ist Primärgeometrie, keine Shaderzusage. |

[Vorher/Nachher](baseline_vs_corrected.png) und Referenzboards verbinden genau
die festen Kamerapixel mit den freigegebenen Quellen. Ein unabhängiger Reviewer
hat die aktuellen 1024px-Ansichten tatsächlich angesehen und IR-01 für den
Primärformumfang bestanden. Große cream Gesichtsfederzüge zur Randauflösung und
Wangen-/Mittelstegfluss sind als **konkrete weitere #6-Lieferung** im
[Folgeplan](../../../docs/review-fixes-qa-followup.md) und #6-Startplan verankert.
Das ist keine ausstehende bloße Zusage einer Primärmaskenkorrektur.

## Abschlussmatrix

| Finding | Änderung / Primärbeleg | Status und Grenze |
|---|---|---|
| IR-01 major | Tatsächliche neue parametrisierte Masken-/Bridge-/Brow-Geometrie; vier aktuelle Pflichtansichten, Vorher/Nachher und unabhängige Bildprüfung | **resolved** für Primärform/#34. Konkretes Gesichtsfederfinish #6; finale Shader #18/#19. |
| IR-02 minor | Gate v2 `delivery_gates.py`, vollständige Quellen-/Referenz-/Reloadinventare, rekursive konkrete Feldschemas; Leerung, jeder fehlende Key, matched null/empty, verschachtelte Lücken, falsche Hashes negativ geprüft | **resolved**. Face 18/9/8, Beak 20/9/12, Feet 24/9/11 Pflichtfelder; neue #37-Lieferung bindet 50 Quellen und tatsächliche worker-generierte Daten. |
| IR-03 observation | `history_gate.py`, code-owned Inventar und echte Vorgängerhashes; typed top-level Dependency-Maps; [echter Git/LFS-Audit](history-git-audit.json) | **resolved**. Zwei Archive/zwölf Snapshots sind Git-bytegleich; 384 geschützte Review-/Quellen-/Bild-/Blenddateien unverändert. Kein rückwirkendes Approval-Rehash. |
| IR-04 observation | Cage/evaluierte Dreiecksprüfung inklusive Adjazenzerfassung und coplanarem 2D-Flächenschnitt, vier tatsächliche negative Flächenfixtures; Closure/Clearance/Grip und Foot-Ecken | **resolved current, deferred rig**. Konkrete kombinierte gesamte Avatar-/Rig-Prüfungen bleiben #20–#24; Tests sind keine universelle Containment-/Physikfreigabe. |
| IR-05 observation | Expliziter isolierter Producer, unveränderte Vorgängerinventare vor/nach Run; fünf eigene Blender-Prozesse mit Exitnachweisen; zusätzlicher kompletter ursprünglicher Scratch-Smoke | **resolved**. #6 startet von neuer #37-Kopie; generische Renderer speichern weiterhin geladene Datei, Material-/Rig-Gerüste gehören in Scratch. |

Historische Version-1-Producer/Validatoren bleiben bytegenau als Quellenbeleg
erhalten. Projektvalidierung und Tests verwenden die neuen Version-2-Abnahmegates.
Neue Lieferung ist damit eine geprüfte zusätzliche Gate-Version, keine unbemerkte
semantische Migration alter Freigaben. `history_gate` akzeptiert keine verkürzten
selbstdeklarierten Maps; fehlende Snapshots liefern verständliche Fehler. Nur
`source_sha256`, `evidence_sha256`, `recipe_sources`, `fixture_sources` dürfen die
bekannten mechanischen Dependency-Umzüge enthalten. Gründe/Kriterien/Nested-Maps
werden nicht global nach Hashwerten umgeschrieben.

## Tatsächliche Blender-Prüfung

- 50 Meshes/62 Objekte bleiben bestehen. Alle **45 unbetroffenen Meshes** stimmen
  in Cage/Transforms/Materialslots/Vertexgruppen/Modifiern exakt mit #5 überein;
  auch die drei Pivots und das vollständige feste Studio bleiben identisch.
- Wiederholter Build identisch; gespeicherter Build und zwei weitere frische
  Blender-Reloads liefern identische Probe-/Geometrie-/Studio-Daten und exakt
  identische **1024px-RGBA-Pixel** in allen vier Ansichten. Die frisch gerenderten
  gespeicherten Buildansichten sind die kanonischen Abnahmebilder.
- Live-Renderings innerhalb des Build-Prozesses enthalten kleine Eevee-RGB-
  Cacheabweichungen gegenüber den frischen Opens. `evidence/live_neutral`
  bewahrt sie; für diese Bilder wird keine Pixelidentität behauptet. Geometrie
  und Kameras waren identisch. Ein frischer eigener Renderer löst diese Grenze
  reproduzierbar, ohne Kamera-/Materialänderung oder abgeschwächte Vergleichstoleranz.
- Alle fünf korrigierten Meshes: geschlossen/verbunden, positive Volumina,
  konsistente Normals, keine doppelten Vertices/degenerierten Faces, kein
  nichtadjazenter Schnitt. Zusätzlich keine Dreiecksinnenflächenkreuzung in Cage
  und evaluierten Flächen, einschließlich benachbarter Flächen.
- Relative Innenflächen-Inset 0,001; maximaler gemessener Cage-Inset **17,28 µm**.
  Coplanare Flächen werden zusätzlich projiziert/geclippt, weil Blender-BVH solche
  Überlappungen nicht zuverlässig meldet. Flächentoleranz 1e-12 m²,
  Ebenentoleranz 1e-8 m. Vier tatsächliche negative Fixtures (shared vertex,
  shared edge, degeneriertes Dreieck, gefaltetes Quad) werden abgewiesen.
- 96 Außenrandpunkte je Maske: maximaler nächster Kopfabstand **1,083 mm** bei
  1-mm-Frontoffset und bewusst zurückgesetztem medialem Schnabelsitz; Limit 1,2 mm.
  Die 2-mm-Maskenhaut überlappt an ihren Wurzeln absichtlich den Kopf. Das ist
  ein klassifizierter Anschluss, keine pauschale kollisionsfreie Gesamtbehauptung.
- **41 Blinkzustände**, minimaler exakter Dreiecks-/Cornea-Abstand **1,025 mm**,
  **10.034** vollständige Closure-Rays; Vorder-/Rückseam exakt geschlossen.
  Vier tatsächliche **±12°** X/Z-Blickproben ohne Schnitte.
- **41 Schnabelzustände über 0–18°**, **2.337** Kollisionschecks; Oberteil fest,
  Unterkiefer fällt sichtbar **10,958 mm**, kleinster beidseitig gesampelter
  neuer Maskenabstand **7,247 mm**. Keine Durchdringung der neuen Gesichtsteile.
- Echte 3+1-Verzweigungen pro Fuß, acht Krallen-/Bar-Kontakte und Padkontakt;
  **45** unabhängige Fuß-Kollisionspaare. Alle vier erlaubten Radius/Spacing-Ecken
  plus Mittelpunkt bestehen; vier knapp außerhalb liegende Werte werden abgewiesen.

Diese Prüfung behandelt die in #37 geänderte Gesichtstopologie und vorhandene
Funktionsproben. Sie beweist kein fertiges Rig, keine allgemeine kombinierte
Containment-/Lastfreigabe und keine kontinuierliche Parameterraumgarantie.
Die konkrete noch nicht ausführbare Avatar-QA bleibt in #20/#21/#22/#23/#24.
Finale Flügel/Körper/Schwanzfedern, Lookdev, Benutzercontrols und Actions fehlen
weiterhin gemäß Produktionsfolge; keine Flug- oder Druckflächenphysik eingeführt.

## Reproduktion, Versionen und Abschlussprüfung

[README](README.md) enthält ausführbare Befehle. `verification.json` bindet Szene,
50 Quellen, neun Referenzen, 384 historische Dateien, eigene JSONs/PNGs und
vollständige Worker-Logs/Argv/Exitcodes. Blender **5.2.1 LTS**,
Hash `9e2066aef7ef`, Python **3.11.9**, Pillow **12.2.0**, Git **2.53.0.windows.3**,
Git LFS **3.7.1**. Alle fünf gelieferten Blender-Worker endeten mit **Exit 0**.
Kontrollierte vorläufige Fehlversuche sind keine gültigen Liefernachweise;
die kanonische Reproduktion ist `run07` mit dem frischen gespeicherten Renderer.
Nach der letzten Gate-Härtung und UTF-8/LF-Normalisierung neuer Logs wurde die vollständige Lieferung erneut erzeugt;
Geometrie-/Probe-Daten und alle vier kanonischen Pixelbilder stimmen exakt mit
dem unabhängig geprüften vorherigen `run05` überein. Blend-Containerbytes ändern
sich durch erneute Speicherung/Work-Pfade; die finale Datei ist oben exakt gebunden.

Projektvalidierung/Tests/Compileall/Doctor/kompletter Scratch-Smoke sowie
abschließende unabhängige technische Prüfung und PR-/CI-Status werden in
`command-results.json` und den verknüpften unabhängigen Berichten festgehalten.
Lokal bestehen **45 Tests**, Doctor, strikte Projektvalidierung, Compileall und
der vollständige Scratch-Smoke mit **Exit 0**. Unabhängige
[Gate-Prüfung](independent-gates-review.md) und
[visuelle/Blender-Prüfung](independent-visual-review.md) bestätigen den finalen
exakten Lieferstand; keine blockierenden Findings bleiben. Die konkreten späteren
Rig-Prüfungen wurden in den offenen Issues #20–#24 als Abnahmepunkte verankert.
Die aktuelle Lieferung ist vor Merge ein prüfbarer Kandidat; Issues schließen
erst nach dem eigenen erfolgreichen PR-Merge.

Der erste Windows-CI-Checkout wandelte 14 historische Review-Logs nach CRLF um;
die neue strikte Hashprüfung wies sie korrekt zurück. Die gezielte `-text`-Regel
in `.gitattributes` bewahrt deren ursprüngliche Git-Bytes auf allen Plattformen;
historische Logs und ihre Freigabebindungen wurden nicht geändert.

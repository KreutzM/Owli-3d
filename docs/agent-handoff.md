# Übergabe an einen frischen Agenten

Stand: 2026-10-04, nach der geprüften Korrekturlieferung
[Goal #37](https://github.com/KreutzM/Owli-3d/issues/37).
Vorgänger-/Review-Merge: `473f8726d32ac7852ef93884b3010b52b8836521`.
Der genaue neue Produktionscommit ist im zugehörigen #37-PR und Git-Verlauf verankert.
Diese Übergabe beschreibt einen Zwischenstand, keinen fertigen Owli-V1-Avatar.

**Nächster Auftrag: [Goal #6](https://github.com/KreutzM/Owli-3d/issues/6).**
Ausgangsszene: [`blender/scene/owli_review_fixes_v01.blend`](../blender/scene/owli_review_fixes_v01.blend).
Gesamtauftrag und Reihenfolge: [Epic #11](https://github.com/KreutzM/Owli-3d/issues/11).
Die Findings-Nacharbeit hat ihren eigenen Branch `fix/37-review-findings` und
vollständige versionierte Nachweise; der verbindliche Einstieg benötigt keine Chat-Historie.

## Sofortiger Einstieg

1. `AGENTS.md` lesen und danach dessen acht Pflichtquellen in genau dieser Reihenfolge:
   `DESIGN_FREEZE.md`, `CHARACTER.md`, `design/reference_hierarchy.json`,
   `design/character_spec.json`, `design/materials.json`, `design/rig_spec.json`,
   `references/manifest.json`, `validation/checklist.json`.
2. Diese Übergabe, [Repo-Karte](repository-map.md), [Startplan #6](next-goal-6.md),
   [Entscheidungen](decisions.md), [#37-Bericht](../validation/reviews/review_fixes_v01/report.md)
   und [konkrete Folge-QA](review-fixes-qa-followup.md) lesen.
3. GitHub-Issues #6/#11 und aktuellen Branch/Arbeitsbaum erneut prüfen. Bei einem
   neueren `main` dessen Änderungen berücksichtigen; der obige Commit ist ein
   belegter Ausgangspunkt, kein Befehl zum Zurücksetzen.
4. Referenzen 00, 07 und 08 tatsächlich ansehen. Bilder sind in
   `references/approved/`; keine neuen allgemeinen Konzepte generieren.
5. Werkzeuge und bestehende Nachweise prüfen, dann einen eigenen Branch für #6
   anlegen. Die akzeptierte Szene in einen neuen Arbeits-/Meilensteinstand kopieren.

```powershell
git status --short --branch
git fetch origin
git lfs pull
python -m pip install -r requirements.txt
python scripts/project.py doctor
python scripts/project.py validate
python -m unittest discover -s tests -v
python scripts/project.py smoke
```

Vor einem Branchwechsel oder Pull eigene lokale Änderungen sichern. Ein LFS-
Pointer statt einer echten Blend-Datei ist kein Modellierungsstand. Die neue
geprüfte #37-Szene hat SHA-256
`8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`
und 1.068.211 Bytes. `review_fixes_gate.validate_review_fixes` bindet ihre eigene
Lieferung. Die historische #5-Baseline bleibt unverändert:
`0fb1512b3a27c4ebe5b7cbdebf520643b7208f2c74f8a847545ffc51dda66797`, 1.020.254 Bytes.

## Geprüfte Meilensteine

| Ergebnis | Issues / PR | Autoritative Szene | Dauerhafter Bericht |
|---|---|---|---|
| Referenzen, Repo-/Werkzeuggerüst | #2 / #10 | neun verifizierte PNGs | `docs/tooling-audit.md` ist der historische Erstaudit |
| Festes Validierungsstudio | #12 / #25 | `owli_validation_setup.blend` | `validation/reviews/setup/report.md` |
| Parametrischer Blockout und grober Silhouetten-Freeze | #13/#14, Container #3 / #26/#27 | `owli_blockout_v01.blend` | `validation/reviews/blockout_v01/report.md`, `design/silhouette_freeze.json` |
| Zusammenhängender Kopf/Hals/Torso, Brow/Büschel | #15 / #28 | `owli_head_body_v01.blend` | `validation/reviews/head_body_v01/report.md` |
| Getrennte Augenlagen, Maske, geometrischer Blink | #16 / #29 | `owli_face_v01.blend` | `validation/reviews/face_v01/report.md` |
| Ober-/Unterschnabel und kollisionsfreie Öffnungsprobe | #17, Container #4 / #30 | `owli_beak_v01.blend` | `validation/reviews/beak_v01/report.md` |
| Zusammenhängende 3+1-Füße, acht Krallen, tragender Griff | #5 / #31 | `owli_feet_v01.blend` | `validation/reviews/feet_v01/report.md` |
| Organische Maske/Bridge, angehobene Brauen, strikte v2-Gates | #37 mit #34/#35 | `owli_review_fixes_v01.blend` | `validation/reviews/review_fixes_v01/report.md` |

Alle Szenen liegen unter `blender/scene/` und werden durch Git LFS übertragen.
Die älteren Szenen sind eingefrorene Vergleichsstände, keine alternativen aktuellen
Produktionsdateien. `blender/scene/owli.blend` ist der allgemeine Runner-Zielpfad;
seine Existenz oder Aktualität ersetzt nicht den akzeptierten Meilenstein.

## Tatsächlicher Inhalt der aktuellen Szene

Frisch in Blender geöffnet: 62 Objekte, davon 50 Mesh-Objekte, vier Kameras,
fünf Studio-Lichter und drei Empty-Pivots. Keine Armature, keine Actions.

| Bereich | Tatsächlicher Stand |
|---|---|
| Kopf/Körper | `PRI_HeadNeckTorso` ist eine zusammenhängende Fläche; `PRI_Brow_L/R` und `PRI_Tuft_L/R` sind getrennte Primärformen. Gruppen `body`, `head_neck`, `wing_root_L/R` dienen der Vorbereitung und Probe. |
| Augen/Maske | `FAC_Globe/Iris/Pupil/Cornea_L/R`, `FAC_Mask_L/R`, `FAC_MaskBridge`, `FAC_Lid_Upper/Lower_L/R`; `FAC_EyeAim_L/R` sind Blick-Pivots. |
| Schnabel | `BAK_Upper`, `BAK_Lower`, `BAK_LowerPivot`; Öffnung um lokales negatives X, 0–18 Grad. |
| Füße/Stange | `GRP_Foot_L/R`, je `GRP_Claw_<side>_Front_1..3` und `Rear_1`; `GRP_PerchBar/Stem/Base`. Zehengruppen `toe_Front_1..3`, `toe_Rear_1`. |
| Noch grob | `BLK_Wing_L/R`, `BLK_Tail`, `BLK_Chest`, `BLK_ChestAccent_L/R`, `BLK_ForeheadNode_*` und `BLK_ForeheadLink_*`. |
| Noch leer | Collection `FEATHERS` und `RIG`; die Krallen liegen tatsächlich in `FEET`, die Collection `CLAWS` ist leer. |

Die sieben Materialien sind fünf `BLK_Swatch_*`-Diagnosefarben,
`FAC_CorneaInspection` und `GRP_PerchDiagnostic`. Finale Feder-/Augenshader,
gebürstetes Metall, Cyan-Stangenakzente und ausgearbeitete Tech-Motive fehlen.
Die Renderings sind geometrische Meilensteinansichten und entsprechen noch nicht
dem fertigen Beauty-/Feder-Look der Referenzen.

#37 verändert genau fünf Meshes: `FAC_Mask_L/R`, `FAC_MaskBridge`, `PRI_Brow_L/R`.
Neue Parameter in `design/review_fixes.json`; breite Wangen führen auf den echten
Kopf zurück, die helle Verbindung läuft unter den Schnabel, Brauen steigen verjüngt
zu den Ohrbüscheln. Alle 45 übrigen Meshes, drei Pivots und das feste Studio bleiben
exakt erhalten. Gesichts-Federfluss/Randfinish ist jetzt ausdrücklich Teil von #6.

## Noch offene Produktionskette

| Reihenfolge | Goal | Abhängigkeit / Ergebnis |
|---|---|---|
| Jetzt | #6 | nach #37: Primärflügel, große Flügel/Körper/Schwanzlagen, zugewiesenes Gesichtsfederfinish, Gesten-Bindungsstrategie |
| Danach | #18 | nach #4/#5/#6: tatsächlich zugewiesene Nicht-Augen-Materialien, Stirnmotiv und Stangenakzente |
| Danach | #19 | nach #18: tiefe blue/cyan Augen und Iris-Netzwerkmotiv; damit Container #7 abschließen |
| Danach | #20 | nach #7: gesamte Topologie und Deformationsbereitschaft prüfen |
| Danach | #21 → #22 → #23 | Körper/Kopf-Rig → Gesicht → Flügel/Füße; damit Container #8 abschließen |
| Danach | #9 | nach #8: ruhiges Animationsset mit echten Actions |
| Zuletzt | #24 | nach #9: `owli_v1.blend`, finales QA und `docs/handoff.md`; Epic #11 abschließen |

Die Container #3/#4/#7/#8 sind keine zusätzlichen unbegrenzten Modellierungsgoals.
Dieses Dokument heißt absichtlich `agent-handoff.md`: `docs/handoff.md` ist die
noch ausstehende finale Produktübergabe aus #24.

## Verifikation und ihre Grenzen

#37 liefert 41 Blink-/41 Beak-Zustände, ±12° Gaze, reale 3+1-Kontakte und alle vier
Foot-Parameter-Ecken plus Mittelpunkt/Outside-Negatives. Drei frische Blender-Opens
haben identische Geometrie/Proben und vier identische 1024px-RGBA-Ansichten.
Ein unabhängiger Reviewer hat die endgültigen Bilder angesehen und `inspect`/`exercise`
in einem weiteren frischen Blender-Prozess tatsächlich ausgeführt. Fünf korrigierte
Mesh-Cages/evaluierte Flächen sind inklusive adjazenter/coplanarer Innenflächen und
vier realer Negativfixtures geprüft; Inset-/Flächentoleranzen bleiben dokumentierte
Grenzen. Gesamtavatar-/Rig-Kombinationsprüfungen sind konkret #20–#24 zugeordnet.

Aktuelle CI-Abnahme nutzt `delivery_gates.py`/`history_gate.py` (Version 2)
und `review_fixes_gate.py`. Komplette Quell-/Referenz-/Reloadinventare, rekursive
Schemas, echte Worker-Daten und tatsächliche kanonische Pixelvergleiche sind Pflicht.
Byte-exakte historische Version-1-Producer bleiben erhalten. 14 Git-Vorgängeranker
und 384 geschützte Review-/Quellen-/Bild-/Blenddateien wurden byte/LFS-OID-geprüft;
kein altes Approval/Pixel/Szene wurde auf einen neuen Quellhash umgeschrieben.

PR #31 bestand Windows-/Ubuntu-CI; lokal bestanden 25 Python-Tests,
Projektvalidierung, compileall und der vollständige Blender-Smoke. Der Fuß-Build
prüfte echte geschlossene Quad-Flächen, alle Zehen-/Krallenkontakte, tragenden
Polsterkontakt, 45 unabhängige Kollisionspaare, Wiederholbarkeit, halbe/doppelte
Skalierung und erlaubte Parametergrenzen. 37 andere Meshes und die drei Pivots
blieben unverändert. Zwei frische Blender-Prozesse lieferten identische Geometrie
und Pixel aus allen vier Kameras. Der ausführliche Bericht nennt tolerierte
Kontaktstellen und die natürliche Verdeckung der hinteren Krallenspitzen.

CI installiert kein Blender. Sie prüft Quellen-/Artefakt-/Referenzbindungen und
Tests; echte Blender-Prüfungen werden lokal im jeweiligen Review-Runner ausgeführt.
Ein grüner Gerüst-Smoke allein beweist weder fertige Federn noch Materialzuweisung,
Rig-Funktion oder Animation. `30_wings_feathers.py` schreibt derzeit nur Policy-
Metadaten; `50_materials.py` erzeugt eine Bibliothek; `60_rig.py` ein ungewichtetes
Gerüst. Deren Konsolenausgaben sind keine Produktionsfreigabe.

## Fallstricke für die Fortsetzung

- Meter, Z oben, +Y vorne; globale Referenzhöhe 0,45 m. Links ist negatives X.
  Vier feste Kameras heißen `VAL_FRONT`, `VAL_LEFT`, `VAL_BACK`, `VAL_3Q`.
  `validation/reference_views.json` steuert Licht, Framing und Referenzpanels.
  Kameras nicht zum Kaschieren von Fehlern umstellen.
- Quelle 00 regelt Marke/Gesicht/Farbe, 07 Form/Profil/Rücken, 08 Konstruktion/
  Materialintention, Beauty nur unterstützend. Referenzen sind keine metrisch
  exakten Orthoprojektionen. Grobe eingefrorene Formen nur mit dokumentierter
  Vieransichten-Neubewertung ändern; keine widersprüchlichen Bilder mitteln.
- `face_geometry.set_blink` rekonstruiert Lider nichtlinear auf einer Kugel.
  Lineare Shape-Key-Interpolation würde ins Auge schneiden. Blick-Pivots und
  `beak_geometry.set_open` sind Probe-APIs, noch keine fertigen Rig-Controls.
- `scripts/project.py --scene/--output` gilt nur für `render`. Der Render-Befehl
  speichert Studiozustand in die geladene Szene. Auf einer Arbeitskopie rendern,
  nicht beiläufig ein akzeptiertes LFS-Artefakt überschreiben.
- Gespeicherte Review-JSONs binden exakte Quellen, Parameter, Blend-Dateien und
  PNGs. Änderungen an gemeinsam genutzten Helfern oder `project.py` können ältere
  Nachweise ungültig machen. Nicht einfach Hashes nachtragen oder Tests schwächen.
  Neue Goal-Helfer bevorzugen; notwendige Migrationen bytegenau archivieren und
  semantisch auditieren. Siehe `validation/history/pre_feet_v01/README.md` und
  `scripts/history_bindings.py` für das bereits eingeführte Verfahren.
- Alte vollständige Blender-Verifier erwarten teilweise ihre damaligen
  Guide-Objekte. Beispielsweise sucht der #16-Verifier noch `BLK_Beak` und
  `GUIDE_Toe_*`, die im aktuellen Blend ersetzt sind. Historische Artefakte mit
  ihren eigenen Validierern prüfen; generische Mesh-Audit-Helfer gezielt wiederverwenden.
  Einen alten Gesamt-Verifier nicht ungeprüft auf die neue Gesamtszene anwenden.
- `verify_feet.inspect` behandelt den Präfix `GRP_` als Fuß-/Stangengeometrie.
  Neue Federobjekte mit eigenem Präfix benennen. Die aktuellen Material-/Rig-
  Gerüste speichern fest nach `blender/scene/owli.blend`; sie sind noch keine
  sicheren produktiven Editierbefehle für beliebige geladene Meilensteinszenen.
- Auf Windows JSON/Markdown explizit als UTF-8 mit LF schreiben und lesen.
  Für Rohhashes `read_bytes()` verwenden; Standard-Codepages können Umlaute
  verfälschen. Neue Textdateien werden durch `.gitattributes` auf LF normalisiert.
- `tmp/` und `validation/renders/` sind ignorierte Arbeitsbereiche, keine
  Übergabenachweise. Dauerhafte Nachweise gehören nach `validation/reviews/`.
- Bestehende Review-Runner können akzeptierte Artefakte neu erzeugen und deren
  Hashes ändern. Für einen Einstieg zunächst Validierer/Tests verwenden;
  alte Milestones nicht ohne Anlass regenerieren.

## Werkzeuge und GitHub

Auf diesem Windows-Rechner zuletzt erneut geprüft: Python 3.11.9, Pillow 12.2.0,
Git 2.53.0, Git LFS 3.7.1, Blender 5.2.1 LTS unter
`C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`.
FFmpeg, GitHub CLI und Make sind vorhanden; Blender muss nicht im PATH sein.
`--blender` oder `BLENDER_EXECUTABLE` wählen eine andere Installation.

Der frühere lokale `gh`-Token war ungültig; CLI-Existenz bedeutet keine erfolgreiche
Authentifizierung. In dieser Sitzung funktionierten Git/SSH-Push sowie der
verbundene GitHub-Connector für Issues, PRs, Checks und Merge. Ein frischer Agent
muss die tatsächlich verfügbaren Zugänge prüfen. Keine Zugangsdaten versionieren.
Im eingeschränkten Codex-Arbeitskontext brauchten Git-Schreiboperationen eine
Sandbox-Freigabe; diese Umgebungseigenschaft ist keine GitHub-Repository-Regel.

Je Produktionsgoal einen eigenen PR mit überprüfbaren Ergebnissen erstellen.
Issue-Abschluss und Epic-Fortschritt an tatsächliche Lieferung und Merge binden.
Für die nächste Übergabe dieses Dokument, das Goal-Issue und Epic #11 aktualisieren;
vor allem neuen Ausgangscommit, Szene, Tests und verbleibende Grenzen nennen.

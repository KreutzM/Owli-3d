# Übergabe für einen frischen Agenten

Stand 2026-10-05: Materiallieferung [#18](https://github.com/KreutzM/Owli-3d/issues/18).
Dies ist ein Zwischenstand, kein fertiger Owli-V1-Avatar.
**Nächster Auftrag: [#19](https://github.com/KreutzM/Owli-3d/issues/19), Augenlookdev
mit F-03 aus [Nacharbeit #40](https://github.com/KreutzM/Owli-3d/issues/40).**

## Verbindlicher Einstieg

AGENTS und dessen acht Pflichtquellen in genau der angegebenen Reihenfolge
lesen. Danach diese Übergabe, [Startplan #19](next-goal-19.md), tatsächliche
GitHub-Issues #19/#40/#11, [Repo-Karte](repository-map.md),
[Entscheidungen](decisions.md) und [Materialbericht](../validation/reviews/materials_v01/report.md).
Referenzen 00 > 07 > 08 tatsächlich ansehen; bestehende Meilensteine bewahren.
Aktuellen Branch/main erneut prüfen; ältere Chatstände nicht als Startbefehl nehmen.

Aktuelle LFS-Szene: `blender/scene/owli_materials_v01.blend`, 1,793,740 Bytes,
SHA256 `ca5522b3948e2d3501eb47c0b0f3099a7ca9d7e596e8e9af5b9f6128353acaa3`. Der zugehörige #18-PR/Git-Verlauf verankert Produktionscommit,
Integration/CI und Issueabschluss; vor Fortsetzung tatsächlichen Merge prüfen.
Maschinen-/Quellen-/Bildbindungen in `validation/reviews/materials_v01/verification.json`,
separate visuelle Abnahme in `review.json`.

```powershell
git status --short --branch
git fetch origin
git lfs pull
python scripts/project.py doctor
python scripts/project.py validate
python scripts/feathers_gate.py
python scripts/materials_gate.py
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

Eigene Änderungen vor Branchwechsel sichern. Ein LFS-Pointer ist kein echter
Blend-Arbeitsstand. Historische Runner zum Prüfen vorhandener Nachweise nicht neu ausführen.

## Tatsächlicher Szeneninhalt

117 Objekte/103 Meshes, fünf Empty-Pivots, vier feste Kameras, fünf Lichter,
14 Materialdatablocks, keine Armature/Actions. Meter, Z oben, +Y vorne; links −X.

| Bereich | Tatsächlicher Stand |
|---|---|
| Kopf/Körper | Zusammenhängender PRI_HeadNeckTorso, separate Brow/Tuft; Gruppen body/head_neck/wing_roots vorbereitet |
| Augen/Gesicht | FAC_Globe/Iris/Pupil/Cornea je L/R unverändert diagnostisch; organische Maske/Bridge/Lider mit echten Blink-/Gazefunktionen |
| Schnabel | BAK_Upper/Lower und LowerPivot; reale 0–18°-Öffnung; Nasenlöcher fehlen |
| Federn/Flügel | 51 FTH-Meshes, davon 48 geschlossene breite Gruppen; WingRoot L/R bewegen die Teile gemeinsam 0–12° mit 45-mm-Schulterblend und festen Roots |
| Füße/Stange | Je drei vordere/eine hintere Zehe und Kralle; acht Krallenkontakte; GRP_PerchBar/Stem/Base |
| Materialien | Zehn tatsächlich zugewiesene Nicht-Augen-Shaders, sRGB→linear; satin/matte Federn, Keratin, gebürstetes Metall, Cyan-Emission |
| Tech | Sieben TECH_ForeheadNodes/sechs Links auf der Stirn, vier schmale TECH_PerchRings; noch keine finale Rigbindung |

F-01 ist gelöst: acht Cream-/Orange-Gruppen gezielt angepasst, breitere Cream-
Brust mit diagonalen begrenzten Gold/Orange-Verläufen, ohne homogene Orangefläche.
78 alte Cages, acht Augen samt Slots/Graphs, ursprüngliche Pivots und das Studio
bleiben exakt. Krümmung verkürzt das Stirnmotiv in Profil/3Q. Die wenigen breiten
Gruppen bleiben eine grobe Stilentscheidung; der Augenlook ist weiterhin unfertig.

## Nachweise und verbleibende Kette

Vier Blender-Worker liefern exakte gespeicherte Laufzeitdaten und kanonische
RGBA-Pixel; separate visuelle/technische Reviewer öffnen/rendern/proben selbst.
Alle 51 FTH/17 TECH sowie 41 Blink-/41 Schnabelzustände, ±12° Gaze, sechs Gesten
und 3+1-Griff werden tatsächlich geprüft. 83 Python-Tests plus Strictvalidate,
Gates, Compileall und Blender-Smoke gehören zur Abnahme. Windows/Ubuntu-CI
validiert Artefakte/Tests; Blender wird dort nicht installiert.

| Reihenfolge | Goal |
|---|---|
| Nächstes | #19: tiefe Blue/Cyan-Augen, Cornea/Reflexe/Netzwerk; F-03-Verhältnis/Ringe ausdrücklich bewerten |
| Zusätzlich vor #20 | #40/F-02: zwei echte Nasenlochvertiefungen; #40 erst mit allen drei Findings am gemeinsamen Stand schließen |
| Danach | #20 kombinierte Topologie/Deformationsbereitschaft nach #7 |
| Danach | #21 → #22 → #23 Körper/Kopf → Gesicht → Flügel/Füße-Rig; Container #8 |
| Danach | #9 Animation, #24 finale owli_v1.blend/QA/docs/handoff.md; Epic #11 |

Container #7 endet erst nach #19. Eine Materialabnahme erledigt Augen und
Nasenlöcher nicht. Die kombinierte Rig-/Animations-QA aus
[review-fixes-qa-followup](review-fixes-qa-followup.md) bleibt #20–#24.

## Historie und Arbeitsregeln

#6/PR #39: Git `a8634936494512d64e311149f20ed4e24ea492ac`,
`owli_feathers_v01.blend`, SHA256
`76ee3f1c0f8b4314aee40585445c14e3b2d193b7aa04c7e2c86e6f810f576b0a`, 1,385,718 Bytes.
#37: Git `966b7f02489ebad4890ba17a6c64f4c03adc2803`, Szene SHA256
`8685fc054428ec848f20a922c995487f9ac4a2797cbe3713eaeb5e364b02e8fb`.
Frühere Blockout/Head/Face/Beak/Feet-Belege bleiben in ihren eigenen Reviewordnern.
`materials_contracts.py` fixiert 548 Vorgänger-Git/LFS-Anker und 68 Quellen;
Stage50 ist aus a863493 bytegenau archiviert. `design/materials.json`, project.py
und gemeinsam gebundene Helfer bleiben exakt. Neue Augenhelfer/-parameter
bevorzugen; alte Approvals nicht auf neue Implementierungen umschreiben.

Je Produktionsgoal eigener Branch/PR/LFS-Szene/Reviewordner; separate visuelle
und technische Sub-Agents, ein Schreiber pro Produktionsdatei. Reviewer an finale
Artefakte binden; betroffene Checks nach Änderungen erneut prüfen. `tmp/` und
`validation/renders/` sind Scratch, keine Lieferung.

Alte volle Verifier erwarten ersetzte Guides; generische Audit-/Funktions-APIs
gezielt wiederverwenden. `digest_part` enthält Materialnamen; Cage-Erhaltung
nutzt `materials_checks.shape_hashes`. Augenhash umfasst Slots und vollständige
Graphs und hält volatile Usercounts außen. TECH-Tori haben Euler 0. `GRP_` ist
für Fuß/Stange reserviert; neue Objekte brauchen eigene Kollisionsziele.
`set_blink` rekonstruiert nichtlinear; lineare Lid-Keys können die Cornea schneiden.

Der Render-CLI kann geladene Szenen speichern; nur Arbeitskopien verwenden.
Stage50 weist nun tatsächlich zu und baut Tech, speichert im Smoke aber
scratch-relativ nach owli.blend. Stage60 bleibt ein ungewichtetes Rig-Gerüst.
`materials_review.py` publiziert nur den benannten eigenen Meilenstein.
UTF-8/LF, read_bytes für Hashes; .gitattributes hält Crossplatform-Bytes gleich.

Zuletzt verifiziert: Python 3.11.9, Pillow 12.2.0, Git 2.53.0, LFS 3.7.1,
Blender 5.2.1 LTS unter `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`.
Git/SSH-Push und GitHub-Connector funktionierten; früherer gh-Token ungültig.
Sandboxfreigabe für Git-Writes ist eine Umgebungseigenschaft; keine Zugangsdaten versionieren.

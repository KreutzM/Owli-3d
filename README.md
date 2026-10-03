# Owli 3D

Produktions-Repository für **Owli**, die kleine Tech-Eule und das Brand-/Mascottchen von Owli-AI.

Ziel ist ein sauber modellierter, riggbarer und später animierbarer 3D-Avatar in Blender. Die erste Version sitzt auf einer Stange; Fliegen ist ausdrücklich **nicht** Teil von V1.

## Produktionsprinzip

- Original-Logo = Markenidentität.
- Finales technisches Turnaround = primäre Form-/Silhouettenreferenz.
- Finales Parts-/Lookdev-Sheet = primäre Detail-/Materialreferenz.
- Beauty-Views = Stil, Charakter und Look.
- Frühere Concept-Sheets dürfen finale technische Sheets nicht überstimmen.
- 3D-Entscheidungen werden dokumentiert; neue Konzeptbilder nur bei echten offenen Designfragen.

## Start für GPT-6.1-Sol

1. `AGENTS.md` lesen.
2. Die Pflichtlektüre in der Reihenfolge aus `AGENTS.md` lesen, beginnend mit `DESIGN_FREEZE.md`.
3. `python scripts/project.py doctor` ausführen.
4. `python scripts/project.py smoke` ausführen.
5. Erst Blockout, dann Silhouette-Review, dann Federn/Materialien, dann Rig.

## Kernreferenzen

Die freigegebenen Referenzen sind in `references/manifest.json` mit Dateiname, Abmessungen und SHA-256 fixiert.
Die eigentlichen PNG-Dateien sollen unter `references/approved/` liegen.

## Ziel für V1

- sitzende Owli auf moderner Tech-Stange;
- klare Wiedererkennbarkeit zum Logo;
- bewegliche Augen;
- Blinzeln;
- Kopf-/Körperbewegung;
- einfacher Schnabel für Sprache;
- Flügelgesten;
- pro Fuß **4 Zehen/Krallen: 3 vorne + 1 hinten**;
- kein Flug-Rig.

## Workflow

```bash
python -m pip install -r requirements.txt
python scripts/project.py validate
```

Blender (Windows/PowerShell und Linux; kein Make erforderlich):
```bash
python scripts/project.py scene
python scripts/project.py blockout
python scripts/project.py feet
python scripts/project.py render
```

Der Runner arbeitet immer vom Repository-Verzeichnis aus. Er findet Blender im PATH
oder unter Windows in `Program Files/Blender Foundation` (höchste Versionsnummer).
Ziel ist Blender 5.x; die Engine-Auswahl berücksichtigt auch Blender 4.2+.
Eine bestimmte Installation kann über `--blender "C:/.../blender.exe"` oder
`BLENDER_EXECUTABLE` gewählt werden. `scene` verweigert das Überschreiben einer
vorhandenen Produktionsszene. Python-Fehler in Blender ergeben einen Fehlerstatus.

`doctor` prüft Python, Pillow, Git, Git LFS, Blender und die Referenzen.
`smoke` führt alle vorhandenen Blender-Skripte und vier 64px-Test-Renderings in einem
temporären Arbeitsverzeichnis aus; die Produktionsszene bleibt erhalten.
Dieser technische Test ersetzt keine Silhouettenprüfung anhand der Referenzen.
Die CI prüft strikte Referenzvalidierung, Python-Syntax und Tooling-Regressionschecks
unter Windows und Linux; der Blender-Smoke-Test läuft lokal.

## Aktueller Arbeitsstand

Alle neun Referenz-PNGs sind vorhanden. Der nächste Produktionsschritt ist
[Issue #3: Blockout und Silhouette](https://github.com/KreutzM/Owli-3d/issues/3).
Die Skripte sind derzeit Gerüste: Kopf-/Flügeltopologie, echter Stangengriff,
Materialzuweisung, Lichtaufbau, vollständige Rig-Steuerung und Animationen sind
noch umzusetzen. Die Folgeaufgaben stehen in Issues #4–#9.

Große Blender-/3D-Artefakte sind für Git LFS vorgesehen.

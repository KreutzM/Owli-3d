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
2. `CHARACTER.md` und `DESIGN_FREEZE.md` lesen.
3. `design/*.json` prüfen.
4. `python scripts/validate_project.py` ausführen.
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
python scripts/validate_project.py
```

Blender:
```bash
blender --background --python scripts/blender/00_scene_setup.py
blender blender/scene/owli.blend --background --python scripts/blender/10_blockout.py
```

Große Blender-/3D-Artefakte sind für Git LFS vorgesehen.

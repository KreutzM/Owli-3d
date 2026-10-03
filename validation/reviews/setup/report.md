# Owli — technischer Vieransichten-Review, Issue #12

Datum: 2026-10-03. Blender: **5.2.1 LTS**. Status: **Studio-Aufbau technisch geprüft**.
Die dargestellte Geometrie ist das vorhandene grobe Gerüst; dieser Bericht erteilt
keine Silhouetten- oder Modellfreigabe.

## Prüfnachweise

| Anforderung | Ergebnis | Nachweis |
|---|---|---|
| Vier ausreichend beleuchtete 1024px-Ansichten | Erfüllt; Kopf, Körper, Flügel, Augen/Schnabel, Füße und vollständige Stange inklusive Basis sind sichtbar | [Übersicht](contact_sheet.png), Originalrenderings unten |
| Kein Bildrand- oder Tiefen-Clipping | Erfüllt; alle 21 Geometrieobjekte in jeder Kamera innerhalb des festen 2%-Sicherheitsrahmens | `render_manifest.json`: framing, Objektbounds und Clip-Distanzen |
| Kamerapositionen unverändert | Erfüllt; ursprüngliche Positionen/Targets, 0,58-m-Orthoscale und 65-mm-Linse übernommen | `validation/reference_views.json`, gespeicherte Studio-Snapshots |
| Kameras und Licht gespeichert | Erfüllt; 4 Kameraobjekte/-datablocks, 5 Lichtobjekte/-datablocks, insgesamt 30 Szenenobjekte | `owli_validation_setup.blend`, `verification.json` |
| Erneutes Öffnen und Rendern reproduzierbar | Erfüllt; separater Blender-Prozess, Studio/Geometrie identisch, alle vier Bilder pixelgleich | `verification.json`: reload_before/after_identical und render_metrics |
| Keine Duplikate bei wiederholtem Setup | Erfüllt; Setup mehrfach vor/nach Reload geprüft; Objekt-/Datablock-Zahlen identisch | Integrationstest `verify_validation_setup.py` |
| Clipping wird erkannt | Erfüllt; absichtlich verschobener Kopf und ungültiger Far-Clip werden abgewiesen; Kameras bewegen sich dabei nicht | `verification.json`: image_clipping_rejected, depth_clipping_rejected |
| 3+1-Regel erhalten | Erfüllt für vorhandene Guides; je drei Frontguides und ein Rearguide mit negativem Y | Integrationstest und Links-/Rückenansicht |
| Referenzhierarchie und Zuordnung nachvollziehbar | Erfüllt; Dateinamen, Ränge und Ausschnitte versioniert; alle neun Original-PNGs hash-/dimensionsgeprüft | JSON-Rezept, Reference-Hashes, Vergleichsbilder |

Konservative minimale Bildrandabstände: Front **3,214%**, Linksprofil **3,214%**,
Rücken **3,214%**, 3/4 vorne **17,660%**. Die größere 3/4-Randfläche stammt aus
der bereits bestehenden Perspektivkamera; es wurde nicht hineingezoomt.

Die neutralen Area-Lichter zeigen jetzt eine lesbare Gradation über Kopf, Flügel,
Körper, Augen und Stange. Eine erste zu helle Variante wurde nach Bildprüfung
verworfen; der finale Aufbau besitzt **0% fast-weiße Vordergrundpixel** in jeder
Testansicht. Die Belichtungsgrenze gilt für diese graue Setup-Testgeometrie, nicht
als pauschales Verbot glänzender Highlights in späteren Lookdev-Renderings.

## Referenzvergleich aus allen vier Ansichten

| Ansicht | Originalrender | Vergleich | Geometrie-/Stilquelle und Befund |
|---|---|---|---|
| Front | [VAL_FRONT.png](VAL_FRONT.png) | [Front-Vergleich](VAL_FRONT_comparison.png) | Turnaround FRONT, Rang 2. Kopf-/Körpervolumen, beide Augen, Flügel und drei vordere Zehenguides je Fuß sind lesbar. Das Gerüst besitzt noch keine Cream-Maske und keine Brow-/Ohrbüschelform. |
| Linksprofil | [VAL_LEFT.png](VAL_LEFT.png) | [Profil-Vergleich](VAL_LEFT_comparison.png) | Turnaround LEFT SIDE, Rang 2. Kopftiefe, Schnabelprojektion, Flügelmasse und Rear-Richtung sind sichtbar. Die ellipsoidalen Zehenguides bilden noch keinen mechanischen Griff. |
| Rücken | [VAL_BACK.png](VAL_BACK.png) | [Rücken-Vergleich](VAL_BACK_comparison.png) | Turnaround BACK, Rang 2. Gefaltete Flügel, zentraler Schwanz, rückwärtige Zehenguides und Support sind sichtbar. Federlagen und finale Schwanzproportionen fehlen. |
| 3/4 vorne | [VAL_3Q.png](VAL_3Q.png) | [3/4-Vergleich](VAL_3Q_comparison.png) | Beauty 01, Rang 4 für Stil; technische 3/4-Ansicht, Rang 2 für Volumen. Beide Quellen stehen auf dem Board. Augen-/Schnabeltiefe, Sitzaufbau und komplette Basis bleiben sichtbar. |

Der technische 3/4-Ausschnitt zeigt die gegenüberliegende laterale Seite zur
vorhandenen +X/+Y-Kamera. Referenzen werden nicht gespiegelt oder geometrisch
verzogen; der Vergleich ist daher keine metrische Überlagerung. Die Panels sind
KI-generierte Designansichten, keine exakten Orthoprojektionen.

Das [Original-Logo](../../../references/approved/00_original_logo.png) bleibt
Rang 1 für Markenidentität, Gesicht und Farbe. Das
[Parts-/Lookdev-Sheet](../../../references/approved/08_parts_lookdev_technical.png)
bleibt Rang 3 für Augen/Schnabel, Federlagen, Griff und Materialintention.
Der im Rückenpanel gezeichnete Cyan-Kronenakzent wird nicht als Freigabe für ein
zweites rückseitiges Tech-Symbol interpretiert: Logo und Spezifikation definieren
das Stirnmotiv. Uneindeutige Krallendarstellungen ändern die explizite 3+1-Regel
nicht. Diese Entscheidungen stehen auch in `docs/decisions.md`.

## Artefakte und Reproduktion

Gespeicherter, erneut geöffneter Blend-Stand:
[`blender/scene/owli_validation_setup.blend`](../../../blender/scene/owli_validation_setup.blend)
(Git LFS). Kamera-/Licht-/Renderparameter:
[`validation/reference_views.json`](../../reference_views.json).
Maschinenlesbare Nachweise: [Render-Manifest](render_manifest.json) und
[Verifikation](verification.json), einschließlich Quell-/Konfigurations-/Referenz-
Hashes, Geometrie-Digest und Pixelvergleich. Die Quellgeometrie aus `10_blockout.py`
und `40_feet_perch.py` wurde durch Setup/Rendering nicht geändert.

```powershell
python scripts/project.py validate
python scripts/project.py setup-review
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

Einzelner Renderlauf mit dem geprüften Blend:

```powershell
python scripts/project.py render --scene blender/scene/owli_validation_setup.blend --output validation/renders/setup-check
```

Die Produktionsdatei `blender/scene/owli.blend` wird durch `setup-review` nicht
erstellt oder überschrieben. Der erzeugte Test-Blend nutzt ausschließlich die
bereits vorhandenen groben Volumen plus Zehenguides. Alle Kameras/Lichter bleiben
über sämtliche Ansichten gleich; PNGs sind 1024 x 1024 ohne Renderborder, DoF,
Motion Blur oder Compositor-Effekte. Die Ansicht nach erneutem Laden startet
mit `VAL_FRONT` und den kanonischen Renderparametern.

## Offene Modellierungsarbeit und Grenzen

Proportionen und Schnabel sind provisorisch. Brow-/Ohrbüschelsilhouette,
Cream-Maske, Schichtung der Augen, Stirnmotiv, Federschichten und echte
Greifgeometrie fehlen im bisherigen Gerüst. Diese Befunde werden in #13/#14 und
den folgenden Produktionsaufgaben bearbeitet; sie sind keine verdeckte
Designänderung dieses Studio-Aufbaus. Die vier Ansichten zeigen diese Fehler
bewusst mit festen Kameras.

Die Pixelgleichheit gilt innerhalb derselben Blender-/Renderumgebung; sie ist
keine Zusage für identische Pixel auf jeder GPU oder über Blender-Versionen.
Objektbounds sind konservativ und können stark deformierte Geometrie eher
ablehnen als nötig; die Abhilfe ist ein begründeter Review, kein Auto-Fit.
Blender meldet beim Setup ungenutzte Factory-Brush-Asset-Pfadwarnungen. Sie
beeinflussen weder die benutzte Geometrie noch gespeichertes Studio/Renderings.

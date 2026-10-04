# Owli coarse blockout v01 — Issue #13

Datum: 2026-10-03. Blender 5.2.1 LTS. **Parametrischer grober Blockout geliefert;
Silhouettenfreigabe folgt in #14.** Abhängigkeit #12 ist gemergt.

## Ergebnis und überprüfbarer Abschluss

| Kriterium aus #13 | Nachweis |
|---|---|
| Wiederverwendbare Proportionen, Augenabstand/-tiefe, Schnabel, Flügel, Schwanz | `design/proportions.json`: benannte Formen und Maße; echte Parameteränderungen und uniforme 0,8-Skalierung am Blender-Modell geprüft und wiederhergestellt |
| Zwei separate volumetrische Augen; Maske und obere Silhouette | Separate kugelförmige `BLK_Eye_L/R`, Maskenloben/Bridge, Brow und je ein grober Tuft; Front und 3/4 visuell geprüft |
| Beide Füße exakt 3 Front + 1 Rear | Acht benannte Toe-Meshes; Rear-Centerlines strikt hinter der Stange, alle vier Zehen pro Fuß greifen unter die Stangenmitte; keine Guide-Vertices im Metallzylinder |
| Erneuter Aufbau ohne Fehler/Duplikate; vier Ansichten | Geometrie-Digest und Objekt-/Mesh-/Materialzahlen nach wiederholtem Aufbau identisch; vier 1024px-PNGs; frischer Reload-Prozess mit erneuter Anatomieprüfung und pixelgleichen Renderings |
| Gespeicherter LFS-Meilenstein und dauerhafte Nachweise | [owli_blockout_v01.blend](../../../blender/scene/owli_blockout_v01.blend), [Manifest](render_manifest.json), [Verifikation](verification.json), vier Originalbilder und Boards |

35 Geometrieobjekte und 9 Studioobjekte: insgesamt 44 Szenenobjekte, 4 Kameras,
5 Lichter. Minimale konservative Bildrandabstände: Front/Links/Rücken **3,214%**,
3/4 **17,660%**. Die Kameras/Lichter aus #12 bleiben gleich; kein Auto-Fit.
Alle neun Referenz-PNGs, Studio-, Design- und Skriptquellen sowie Blend/Renderings
sind gehasht. Die Farbflächen sind matte Debug-Swatches aus der bestehenden
Logo-Palette, keine fertigen Materialentscheidungen.

## Vergleich der vier festen Ansichten

| Ansicht | Original / Vergleich | Befund gegen freigegebene Quelle |
|---|---|---|
| Front | [Original](VAL_FRONT.png) / [Board](VAL_FRONT_comparison.png) | Turnaround 07 FRONT, Rang 2. Dominanter breiter Kopf, zwei große cyanfarbene Augen, creamfarbene Maske, orangefarbener Schnabel, symmetrische Büschel und gefaltete Flügel lesen als grobe Eule. Je drei Frontzehen sichtbar. Maskenloben und Bridge sind noch getrennte überlappende Volumen; Brow wirkt breiter und glatter als die Federpartien der Referenz. |
| Linksprofil | [Original](VAL_LEFT.png) / [Board](VAL_LEFT_comparison.png) | Turnaround 07 LEFT SIDE, Rang 2. Augen sind echte vorstehende Volumen, Schnabel projiziert nach vorn/unten. Flügel liegen am Körper, Schwanz läuft rückwärts abwärts. Front- und Rearguide greifen um die Stange. Maskentiefe, Schnabelprojektion und Schwanzlänge sind verstellbar und für #14 noch vorläufig. |
| Rücken | [Original](VAL_BACK.png) / [Board](VAL_BACK_comparison.png) | Turnaround 07 BACK, Rang 2. Zwei gefaltete Flügel, kompakter mittiger Schwanz und genau eine hintere Zehe pro Fuß erkennbar. Große glatte Kopf-/Körperflächen ersetzen hier noch alle Federlagen. Schwanz endet höher als die Referenz; sein Verhältnis zur Stange gehört in #14. |
| 3/4 vorne | [Original](VAL_3Q.png) / [Board](VAL_3Q_comparison.png) | Technisches Volumen aus 07, Rang 2; Beauty 01 unterstützt Stil, Rang 4. Breite Gesichtsfläche, räumliche Augen/Schnabel und Sitzgriff bleiben lesbar. Beauty-Licht, Federn und Gloss werden nicht übernommen. Technisches Panel zeigt die gegenüberliegende Seite zur festen Kamera; kein metrisches Overlay. |

[Übersicht aller vier Ansichten](contact_sheet.png). Zusätzlich wurden das
Original-Logo 00 für Gesicht/Farbe (Rang 1) und Parts/Lookdev 08 für Schnabel/Griff
(Rang 3) geprüft. Keine älteren Designs wurden eingemittelt. Die schriftliche
3+1-Regel entscheidet uneindeutige Krallendarstellungen. Das rückseitig gezeichnete
Kronenmotiv autorisiert kein zweites Stirnsymbol. Entscheidungen und Abweichungen:
[docs/decisions.md](../../../docs/decisions.md).

## Reproduktion und Prüfungen

```powershell
python scripts/project.py validate
python scripts/project.py blockout-review
python scripts/project.py setup-review
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
python scripts/project.py smoke --blender "C:/Program Files/Blender Foundation/Blender 5.0/blender.exe"
```

Vollständiger isolierter Blockout-Aufbau/Parameterprüfungen/1024px-Save/Reload unter
5.2.1 LTS bestanden; 9 Python-Tests und Syntax-/Referenzprüfungen bestanden.
Gerüst-Smoke unter Blender 5.2.1 und 5.0 bestanden. Studio-Clipping-Negativtests
weisen einen verschobenen Kopf und ungültige Clip-Distanz ab. Kontrollierte
Parameterprobes sind Tests und werden vor dem publizierten Stand wiederhergestellt.
Die neutrale Setup-Testszene wird aus demselben aktuellen Blockout neu erzeugt;
Produktionsdatei `owli.blend` bleibt unberührt.

## Bekannte Grenzen und nächste Arbeit

Keine Produktions- oder Silhouettenfreigabe. Übergänge Maske/Brow/Kopf und Hals
sind getrennte Volumen; Brust-/Schwanzenden zeigen Pinching. Die Augen-Caps sind
matte Positionierungsflächen ohne finale Iris, Cornea oder Lidtopologie. Schnabel
ist eine einzelne grobe Hook-Form; finale Ober-/Unterteilung folgt in #17. Zehen
sind anatomische Griffguides, finale separate Krallen/Deformation folgen in #5.

Kontrollierte orange Brustakzente und Cyan-Federlagen folgen in #6/#18, das
Stirn-Netzwerksymbol in #18, glossy Augen in #19, Rig erst in #21–#23.
Die Büschel sind breite Massen und noch keine finale Feder-Silhouette. #14 muss
Kopf/Körper-Verhältnis, Maske, Flügel, Schwanz und Schnabel über alle Ansichten
bewerten, bevor Detailmodellierung beginnt. Keine feinen Federn, Flugkomplexität
oder neue Konzeptkunst wurden hinzugefügt. Pixelgleichheit gilt für dieselbe
Blender-/GPU-Umgebung, nicht als Zusage über Versionen oder Rechner hinweg.

# Owli V0.1 — Vieransichten-Review und grober Silhouetten-Freeze (#14)

Datum: 2026-10-04. **Große Volumen, Gesichtsanordnung und Sitzhaltung freigegeben.**
Die Entscheidung ist an den aktuellen LFS-Blend, Parameterstand und vier Bilder
in [design/silhouette_freeze.json](../../../design/silhouette_freeze.json) gebunden.
Kein offener blockierender Silhouettenbefund; dies ist keine Freigabe von finaler
Topologie, Materialien, Deformation, Rig oder Animation.

Alle vier festen Ansichten wurden gleichzeitig gegen Turnaround 07 verglichen;
Logo 00 entscheidet Gesicht/Farbe, Parts 08 Schnabel-/Griffintention. Beauty 01
stützt die 3/4-Stillesbarkeit. Technisches 3/4-Panel und feste Kamera zeigen die
gegenüberliegenden lateralen Seiten; keine Spiegelung oder metrische Überlagerung.
Kamera-/Lichtrezept aus #12 ist unverändert. [Vieransichten-Übersicht](contact_sheet.png).

## Alle zwölf Checklistenbefunde

| Check aus validation/checklist.json | Ergebnis und Begründung | Sichtbarer Beleg / Referenz |
|---|---|---|
| 1. Owli immediately reads as the same mascot as the original logo | **Bestanden.** Große Navy/Cyan-Augen, creamfarbene Maske, orangefarbener Schnabel, kontrollierte warme Brustflanken und Stirn-Netzwerklandmarke erhalten die prägenden Logo-Merkmale. Die weichere Brow-Linie ergibt eine ruhige neutrale Lesbarkeit; Gloss und Federtextur sind Folgearbeit. | [FRONT](VAL_FRONT_comparison.png), [3Q](VAL_3Q_comparison.png); 00_original_logo.png (Rang 1), 07_turnaround_technical.png (Rang 2) |
| 2. Head is dominant but not baby-like | **Bestanden.** Kopf samt Büscheln bleibt breiter als der Rumpf; Kopf und Rumpf teilen die Sitzhöhe annähernd ausgewogen. Der vergrößerte Augenread wird durch tiefere Einbettung und kompaktere Unterkörpermasse ausgeglichen, statt einen Baby-Ballkopf zu erzeugen. | [FRONT](VAL_FRONT_comparison.png), [LEFT](VAL_LEFT_comparison.png); 07_turnaround_technical.png (Rang 2) |
| 3. Both eyes are separate spherical/volumetric objects | **Bestanden.** BLK_Eye_L und BLK_Eye_R sind getrennte kugelförmige Meshes mit je 0,098 m Durchmesser. Front/3/4 zeigen zwei unabhängige Volumen; deren Maße und Tiefe sind am gespeicherten Blender-Modell geprüft. | [FRONT](VAL_FRONT_comparison.png), [3Q](VAL_3Q_comparison.png); 08_parts_lookdev_technical.png (Rang 3) |
| 4. White facial mask remains strongly readable | **Bestanden.** Beide creamfarbenen Maskenloben und die schmalere zentrale Verbindung umrahmen die Augen und bleiben in Front sowie 3/4 deutlich gegen Navy abgesetzt. Kleine seitliche Temple-Nähte sind eine spätere Integrationsaufgabe. | [FRONT](VAL_FRONT_comparison.png), [3Q](VAL_3Q_comparison.png); 00_original_logo.png (Rang 1), 07_turnaround_technical.png (Rang 2) |
| 5. Beak size and projection agree across front and profile | **Bestanden.** Der orangefarbene Schnabel hat in Front eine breite Basis und verjüngte Spitze; im Profil projiziert dieselbe grobe Form nach vorn/unten. Breite, Höhe und Projektion bleiben gegenüber Augen und Maske kontrolliert. Ober-/Unterteilung und feinere Hook-Topologie folgen in #17. | [FRONT](VAL_FRONT_comparison.png), [LEFT](VAL_LEFT_comparison.png), [3Q](VAL_3Q_comparison.png); 00_original_logo.png (Rang 1), 08_parts_lookdev_technical.png (Rang 3) |
| 6. Folded wing masses read clearly in side and back views | **Bestanden.** Zwei lange geschlossene Flügelmassen liegen in Profil und Rücken am Rumpf an und laufen bis in die Sitzregion aus. Es gibt keine ausgebreiteten Flugflächen; die laterale Hülle ist in allen Ansichten konsistent. | [LEFT](VAL_LEFT_comparison.png), [BACK](VAL_BACK_comparison.png); 07_turnaround_technical.png (Rang 2) |
| 7. Tail is compact and centered | **Bestanden.** Der Schwanz liegt auf X=0, verjüngt sich symmetrisch und endet unterhalb der Stange. Das abgesenkte Ende korrigiert den zu hohen #13-Stand; der Rumpf bleibt die Hauptmasse. Er ist ein kompakter Einzelblock ohne Federfächer. | [BACK](VAL_BACK_comparison.png), [LEFT](VAL_LEFT_comparison.png); 07_turnaround_technical.png (Rang 2) |
| 8. Each foot has 3 forward toes and 1 rear toe | **Bestanden.** Front zeigt je drei vordere Zehenguides; Rücken zeigt je einen hinteren Guide neben dem Schwanz. Acht eindeutig benannte Meshes und die erneute Anatomieprüfung belegen exakt 3+1 je Fuß. | [FRONT](VAL_FRONT_comparison.png), [BACK](VAL_BACK_comparison.png); 07_turnaround_technical.png (Rang 2), 08_parts_lookdev_technical.png (Rang 3) |
| 9. Rear toe wraps behind the perch rather than duplicating a front claw | **Bestanden.** Profil und Rücken zeigen die hinteren Zehen auf der Rückseite der Stange. Centerlines liegen strikt hinter deren Achse und laufen unter deren Mitte; sie duplizieren keine Frontzehe. Ausgearbeitete Krallen und Griffmechanik bleiben #5. | [LEFT](VAL_LEFT_comparison.png), [BACK](VAL_BACK_comparison.png); 08_parts_lookdev_technical.png (Rang 3), 07_turnaround_technical.png (Rang 2) |
| 10. Perch is visually secondary | **Bestanden.** Stange und Basis bleiben dunkel und schlicht; die bar-Länge von 0,37 m rahmt die kompakte Eule, während Augen, Maske und Büschel die Hauptaufmerksamkeit tragen. Kameras, Licht und Maßstab wurden nicht für diesen Eindruck verschoben. | [FRONT](VAL_FRONT_comparison.png), [3Q](VAL_3Q_comparison.png); 07_turnaround_technical.png (Rang 2), 08_parts_lookdev_technical.png (Rang 3) |
| 11. No fine feather detailing hides a silhouette problem | **Bestanden.** Alle sichtbaren Federbereiche sind glatte Hauptvolumen; zwei Brustflanken sind grobe Farbmassen, keine feinen Federlagen. Front, Profil und Rücken zeigen die vollständige Außenhülle ohne Detailkaschierung. | [FRONT](VAL_FRONT_comparison.png), [LEFT](VAL_LEFT_comparison.png), [BACK](VAL_BACK_comparison.png); 07_turnaround_technical.png (Rang 2), 08_parts_lookdev_technical.png (Rang 3) |
| 12. No flight-specific complexity added | **Bestanden.** Gefaltete Flügel, zwei Füße auf der Stange und ein kompakter Schwanz bilden ausschließlich die Sitzversion. Es wurden weder Fluggeometrie noch Flug-Rig oder Feder-Simulation ergänzt. | [LEFT](VAL_LEFT_comparison.png), [BACK](VAL_BACK_comparison.png); 07_turnaround_technical.png (Rang 2) |

## Korrekturen, Abweichungen und Freeze-Grenzen

Der #13-Stand zeigte kleine Augen, eine schildförmige Brustfläche, sichtbare
Bein-Säulen und einen zu hoch endenden Schwanz. Der korrigierte Unterkörper deckt
die Beine stärker ab; Chest-V und zwei kontrollierte Orange-Massen erhalten die
Logo-Hierarchie. Augen wachsen von 0,086 auf 0,098 m und sitzen tiefer in der
Maske (Y von 0,096 auf 0,074 m). Die Schnabelbasis wird breiter, die Projektion
kürzer; Flügelspitzen rücken zur Sitzregion. Der mittige Schwanz endet bei Z=0,039 m
unter der Stangenachse Z=0,09 m. Büschel schwingen am Ende nach innen.

Iteration 01 wird wegen zu stark vorstehender Augen verworfen. Iteration 02 wird
wegen zu strenger Brow-Neigung und breiter Cream-Temple-Kanten verworfen. Die
finale Neigung beträgt 0,08 statt 0,20 rad; Maskenloben sind schmaler. Kleine
Randnähte, separate Volumenübergänge und glatte Hauptmassen bleiben für die spätere
Topologie-/Federintegration ausdrücklich zulässig; sie ändern die äußere Hülle
nicht. Alle Kandidaten mit vier Ansichten, Boards, Parametern und Prüfnachweisen
liegen unter [iterations/](iterations/), einschließlich des #13-Ausgangsstands.

Ein einzelner grober Cyan-Graph markiert die Stirnposition gemäß Logo/Parts. Seine
oberen Punkte dürfen oberhalb der Kopfmasse auch rückseitig sichtbar sein; es ist
kein zweites Rückensymbol. Endgültige Federintegration, Emission und Node-Styling
folgen in #18. Orange-Flanken sind große Volumen-/Farbführer, keine Feinbefiederung.
No-Flight und exakt 3+1 bleiben erhalten. Keine neuen Konzeptbilder wurden erzeugt.

Der Freeze gilt für Kopf-/Rumpf-/Flügel-/Schwanz-/Schnabelhülle, Sitzhaltung sowie
Augen-/Maskenanordnung. #15/#16 müssen saubere Topologie und integrierte Übergänge
innerhalb dieser Hülle bauen. Ober-/Unterschnabel #17, Krallen/Griff #5, Federgruppen
#6, Materialien/Tech #18/#19 und Rig #21–#23 bleiben spätere Arbeitsstände. Eine
wesentliche Änderung der Hülle benötigt einen neuen Vieransichten-Review.

## Technische Nachweise und Reproduktion

```powershell
python scripts/project.py validate
python scripts/project.py blockout-review
python scripts/project.py setup-review
python -m unittest discover -s tests -v
python -m compileall -q scripts
python scripts/project.py smoke
```

[Gespeicherter LFS-Blend](../../../blender/scene/owli_blockout_v01.blend),
[Render-Manifest](render_manifest.json), [Verifikation](verification.json).
Die isolierten Aufbauprüfungen kontrollieren echte Parameteränderungen, uniforme
Skalierung und wiederholten Aufbau ohne Objekt-/Mesh-/Material-Duplikate. Ein
frischer Blender-Prozess öffnet den gespeicherten Stand, prüft Studio/Geometrie/
Anatomie erneut und erzeugt vier pixelgleiche 1024px-Bilder. Bildrand-/Tiefen-Clipping
wird abgewiesen; Kameras bewegen sich dabei nicht. Produktionsdatei owli.blend
bleibt unberührt. Pixelgleichheit gilt innerhalb derselben Blender-/GPU-Umgebung.

Automatisches design_approval=false bedeutet, dass die technischen Tests keine
visuelle Freigabe erteilen. Die separat visuell verfasste Freeze-Datei enthält diese
Entscheidung und ihre Belege. Tests verwerfen unvollständige Checklisten, offene
Blocker, falsche Referenzränge oder nachträglich geänderte Bilder/Parameter/Blends.
Nach einem Neuaufbau kann der Datei-Hash abweichen; die Freigabe wird dann bewusst
nicht automatisch übernommen. Erst Bilder erneut beurteilen und Entscheidung
aktualisieren. Die neutrale Setup-Testszene wird mit den gleichen Hauptmassen
erneuert; ihr eigener Bericht bleibt ein technischer Studio-Check.

### Ausgeführte Ergebnisse

Blender 5.2.1 LTS: vollständiger 1024px-Aufbau und frischer Save/Reload bestanden;
alle vier Bilder pixelgleich. Auch die ausgelieferte Datei am endgültigen Pfad
wurde nochmals direkt geöffnet: Studio-, Geometrie- und Anatomie-Nachweis stimmen
mit der dauerhaften Verifikation überein. 46 Geometrieobjekte, 4 Kameras und 5
Lichter ergeben 55 Szenenobjekte. Minimale konservative Bildrandabstände:
Front **2,697%**, Links **2,393%**, Rücken **2,794%**, 3/4 **17,384%** — alle über
2%, ohne Kamerakorrektur. Repeated-build-/Datablock-, Parameter-/Skalierungs- und
3+1-Prüfungen bestanden. Alle **12 Python-Tests**, Syntax- und strikte
Referenzvalidierung sowie vollständiger **Blender-Gerüst-Smoke** bestanden.
Die CI überprüft dieselben Python-/Artefaktprüfungen unter Windows und Linux;
der vollständige Blender-Render/Reload-Nachweis stammt aus dem lokalen Lauf.

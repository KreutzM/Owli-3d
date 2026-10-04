"""Checks bind #15's actual Blender/topology and fixed-view evidence to current sources."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from setup_review import sha256
from head_body_review import silhouette_metrics


class PrimaryReviewTests(unittest.TestCase):
    def test_delivered_primary_meshes_and_deformations_have_current_evidence(self):
        folder=ROOT/'validation/reviews/head_body_v01'
        proof=json.loads((folder/'verification.json').read_text())
        decision=json.loads((folder/'review.json').read_text())
        self.assertEqual(decision['status'],'primary_topology_accepted')
        self.assertEqual(decision['blocking_findings'],[])
        self.assertEqual([item['id'] for item in decision['criteria']],
                         ['clean_symmetric_primary_topology','deformable_neck_and_wing_roots','four_view_freeze_preserved'])
        for item in decision['criteria']:
            self.assertEqual(item['result'],'pass')
            self.assertTrue(item['reason'].strip())
            self.assertTrue(item['evidence'])
            self.assertTrue(all(path in decision['evidence_sha256'] for path in item['evidence']))
        for path,digest in decision['evidence_sha256'].items(): self.assertEqual(sha256(folder/path),digest,path)
        self.assertEqual(sha256(ROOT/'blender/scene/owli_head_body_v01.blend'),proof['scene_sha256'])
        self.assertEqual(sha256(ROOT/'blender/scene/owli_blockout_v01.blend'),proof['frozen_scene_sha256'])
        for path,digest in proof['source_sha256'].items(): self.assertEqual(sha256(ROOT/path),digest,path)
        for path,digest in proof['evidence_sha256'].items(): self.assertEqual(sha256(folder/path),digest,path)
        self.assertTrue(proof['reload_identical'])
        baseline=proof['baseline']
        self.assertTrue(baseline['symmetry'])
        self.assertTrue(baseline['identity_transforms'])
        self.assertTrue(baseline['global_scale_probe'])
        self.assertTrue(baseline['repeated_build_identical'])
        self.assertTrue(baseline['toe_rule_3_plus_1'])
        self.assertTrue(baseline['no_rig'])
        self.assertGreaterEqual(baseline['neck_loops'],12)
        self.assertEqual(len(baseline['unchanged_part_sha256']),40)
        self.assertEqual(set(baseline['deformation_probes']),{'head_tilt','head_turn','wing_root_L','wing_root_R'})
        self.assertEqual(set(baseline['rejection_probes']),{'open_surface_rejected','reversed_face_rejected','disconnected_vertex_rejected','asymmetric_vertex_rejected'})
        self.assertTrue(all(baseline['rejection_probes'].values()))
        for item in baseline['primary_meshes'].values():
            self.assertTrue(item['connected_closed_shell'])
            self.assertEqual(item['duplicate_vertices'],0)
            self.assertEqual(item['self_intersections'],0)
            self.assertLessEqual(item['maximum_valence'],5)
        for item in baseline['frozen_envelope_deviation'].values():
            self.assertLessEqual(item['maximum_distance_m'],item['tolerance_m'])
        for key in proof['reloaded']: self.assertEqual(proof['reloaded'][key],baseline[key],key)
        cfg=json.loads((ROOT/'design/head_body.json').read_text())
        for scope in ('full','primary'):
            for view in ('VAL_FRONT','VAL_LEFT','VAL_BACK','VAL_3Q'):
                actual=silhouette_metrics(folder/'evidence/baseline'/scope/(view+'.png'),
                    folder/'evidence/candidate'/scope/(view+'.png'),cfg['silhouette_pixel_tolerance'],cfg['silhouette_iou_min'])
                self.assertEqual(actual,proof['silhouette_comparison'][scope+'/'+view])
                self.assertTrue(proof['render_metrics'][view]['reload_pixels_identical'])

    def test_silhouette_gate_rejects_displacement_and_volume_loss(self):
        with tempfile.TemporaryDirectory() as tmp:
            first,second=Path(tmp)/'a.png',Path(tmp)/'b.png'
            for path,box in ((first,(30,30,70,70)),(second,(38,30,78,70))):
                image=Image.new('RGBA',(100,100),(0,0,0,0))
                ImageDraw.Draw(image).rectangle(box,fill='white')
                image.save(path)
            with self.assertRaisesRegex(RuntimeError,'Silhouette changed'):
                silhouette_metrics(first,second,5,.99)
            image=Image.new('RGBA',(100,100),(0,0,0,0))
            ImageDraw.Draw(image).rectangle((32,32,68,68),fill='white')
            image.save(second)
            with self.assertRaisesRegex(RuntimeError,'Silhouette changed'):
                silhouette_metrics(first,second,5,.99)

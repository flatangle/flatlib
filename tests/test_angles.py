import unittest

from flatlib import angle


class AngleTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_norm(self):
        """Tests angle normalizations."""
        self.assertEqual(angle.norm(0), 0)
        self.assertEqual(angle.norm(360), 0)
        self.assertEqual(angle.norm(361), 1)
        self.assertEqual(angle.norm(-1), 359)

    def test_znorm(self):
        """Tests angle z-normalizations."""
        self.assertEqual(angle.znorm(0), 0)
        self.assertEqual(angle.znorm(90), 90)
        self.assertEqual(angle.znorm(180), 180)
        self.assertEqual(angle.znorm(181), -179)
        self.assertEqual(angle.znorm(270), -90)

    def test_distances(self):
        """Tests distances (counter-clockwise)"""
        self.assertEqual(angle.distance(0, 0), 0)
        self.assertEqual(angle.distance(0, 90), 90)
        self.assertEqual(angle.distance(0, 180), 180)
        self.assertEqual(angle.distance(0, -90), 270)
        self.assertEqual(angle.distance(0, -180), 180)

    def test_closest_distances(self):
        """Tests closest distances between two angles."""
        self.assertEqual(angle.closestdistance(0, 0), 0)
        self.assertEqual(angle.closestdistance(0, 90), 90)
        self.assertEqual(angle.closestdistance(0, 180), 180)
        self.assertEqual(angle.closestdistance(0, 270), -90)
        self.assertEqual(angle.closestdistance(0, 359), -1)

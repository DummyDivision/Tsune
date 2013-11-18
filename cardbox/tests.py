"""
.. module:: tests
    :platform: Unix, Windows
    :synopsis: A useful model indeed.

.. moduleauthor:: Andreas Waigand <awaigand@gmx.net>

"""

from django.test import TestCase


class SimpleTest(TestCase):
    """
     This is a simple testclass
    """

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

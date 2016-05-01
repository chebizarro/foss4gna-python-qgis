# coding=utf-8
"""libePop test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'chebizarro@gmail.com'
__date__ = '2016-04-30'
__copyright__ = 'Copyright 2016, Chris Daley'

import unittest

from libepop import libePop

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class libePopTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.libepop = libePop()

    def tearDown(self):
        """Runs after each test."""
        self.libepop = None

    def test_libepop_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(libePopTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


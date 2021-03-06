import os
import unittest
import shutil

import bcdata
import fiona

EMAIL = os.environ["BCDATA_EMAIL"]


def test_shapefile():
    out_wksp = bcdata.download('bc-airports',
                               EMAIL,
                               driver="ESRI Shapefile")
    # open and check downloaded data
    with fiona.drivers():
        layers = fiona.listlayers(out_wksp)
        assert len(layers) == 1
        with fiona.open(out_wksp, layer=0) as src:
            assert src.driver == 'ESRI Shapefile'
            assert len(src) == 425
    shutil.rmtree(out_wksp)


def test_gdb():
    out_wksp = bcdata.download('bc-airports',
                               EMAIL)
    with fiona.drivers():
        layers = fiona.listlayers(out_wksp)
        assert len(layers) == 1
        with fiona.open(out_wksp, layer=0) as src:
            assert src.driver == 'OpenFileGDB'
            assert len(src) == 425
    shutil.rmtree(out_wksp)


class URLTest(unittest.TestCase):
    def test_bad_url(self):
        self.assertRaises(ValueError, bcdata.download,
                          ('bad-url'), email_address=EMAIL)

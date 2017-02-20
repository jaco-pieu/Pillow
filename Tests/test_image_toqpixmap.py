from helper import unittest, PillowTestCase, hopper, distro
from test_imageqt import PillowQtTestCase, PillowQPixmapTestCase

from PIL import ImageQt

if ImageQt.qt_is_installed:
    from PIL.ImageQt import QPixmap


class TestToQPixmap(PillowQPixmapTestCase, PillowTestCase):

    @unittest.skipIf(ImageQt.qt_version == '5' and distro() == 'arch',
                     "Topixmap fails on Arch + QT5")
    def test_sanity(self):
        PillowQtTestCase.setUp(self)

        for mode in ('1', 'RGB', 'RGBA', 'L', 'P'):
            data = ImageQt.toqpixmap(hopper(mode))

            self.assertIsInstance(data, QPixmap)
            self.assertFalse(data.isNull())

            # Test saving the file
            tempfile = self.tempfile('temp_{}.png'.format(mode))
            data.save(tempfile)


if __name__ == '__main__':
    unittest.main()

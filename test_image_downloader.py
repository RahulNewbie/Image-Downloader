import unittest
import image_downloader
import url_reader
import os


class ImageDownloaderTests(unittest.TestCase):
    """
    unit tests for image downloader module
    """

    def setUp(self):
        """Test Fixture to create an input file for the image loader"""
        self.test_invalid_url = 'http://www.testserver.com/samplepic.htm'
        self.test_valid_jpg = 'http://www.testserver.com/samplepic.jpg'
        self.test_valid_png = 'http://www.testserver.com/samplepic.png'
        self.test_url_file = 'test_url.txt'
        with open(self.test_url_file, 'w') as file:
            file.write('https://p.bigstockphoto.com/GeFvQkBbSLaMdpKXF1Zv_bigstock-Aerial-View-Of-Blue-Lakes-And--227291596.jpg\n'
                       'https://image.shutterstock.com/image-photo/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')

    def tearDown(self):
        """
        Remove the test file
        """
        try:
            os.remove(self.test_url_file)
        except:
            pass

    def test_url_reader(self):
        url_reader.read_lines(self.test_url_file)

    def test_function_invalid_url(self):
        self.assertEqual(image_downloader.get_image_name(self.test_invalid_url), "")

    def test_function_valid_jpg(self):
        self.assertNotEqual(image_downloader.get_image_name(self.test_valid_jpg), "")

    def test_function_valid_png(self):
        self.assertNotEqual(image_downloader.get_image_name(self.test_valid_png), "")


if __name__ == '__main__':
    unittest.main()

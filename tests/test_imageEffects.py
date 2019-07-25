from src.ImageEffects import ImageEffects
import unittest
import os

from PIL import Image, ImageDraw



class TestImageEffects(unittest.TestCase):
    def test_add_circle_to_image(self):
        image = ImageEffects()
        path = os.getcwd()
        print(path)
        img1 = Image.open(path + "\\tests\\img\\celina-1.png", "r")
        img2 = Image.open(path + "\\tests\\img\\celina-2.png", "r")

        actual = image.add_circle_to_image(img1, 202, 225, 10, (255, 0, 0, 128))

        # actual.save("new.png", "PNG")

        for i in range(img2.width):
            for j in range(img2.height):
                self.assertEqual(img2.getpixel((i, j)), actual.getpixel((i, j)), "at position " + str(i) + " " + str(j))

    if __name__ == '__main__':
        unittest.main()

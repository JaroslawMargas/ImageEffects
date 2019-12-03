from PIL import Image, ImageDraw


class ImageEffects:
    def __init__(self):
        pass

    def add_circle_to_image(self, rgba_image, x_pos, y_pos, radius, fill) :
        ellipse_image = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))

        # draw ellipse there
        d = ImageDraw.Draw(ellipse_image)
        d.ellipse((x_pos - radius,
                   y_pos - radius,
                   x_pos + radius,
                   y_pos + radius),
                  fill=fill)

        # blend alpha screen shot with cursor point
        out = Image.alpha_composite(rgba_image, ellipse_image)
        return out

    def draw_images_difference(self, rgba_image, rgba_image_compared):
        result_image = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))

        px = rgba_image.load()
        px_com = rgba_image_compared.load()
        image_result = result_image.load()

        for i in range(result_image.width):
            for j in range(result_image.height):
                r_c, g_c, b_c, a_c = px_com[i, j]
                if px[i, j] == px_com[i, j]:
                    image_result[i, j] = (255, 255, 255, 0)
                else :
                    image_result[i, j] = (r_c, g_c, b_c, a_c)

        return result_image

from Vector3 import Vector3

Color = Vector3

def write_color(image_file, pixel_color):
    image_file.write('{} {} {}\n'.format(int(255.99 * pixel_color.x),
                                         int(255.99 * pixel_color.y),
                                         int(255.99 * pixel_color.z)))
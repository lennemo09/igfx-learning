#include "color.h"
#include "vec3.h"

#include <iostream>
#include <fstream>

int main() {

    // Image

    int image_width = 256;
    int image_height = 256;

    // Create a file to write the image to
    std::ofstream image_file;
    image_file.open("image.ppm");

    // Render

    image_file << "P3\n" << image_width << ' ' << image_height << "\n255\n";

    for (int j = 0; j < image_height; ++j) {
        // std::clog << "\rScanlines remaining: " << (image_height - j) << ' ' << std::flush;
        for (int i = 0; i < image_width; ++i) {
            auto pixel_color = color(double(i)/(image_width-1), double(j)/(image_height-1), 0);
            write_color(image_file, pixel_color);
        }
    }
    
    // std::clog << "\rDone.                 \n";
    image_file.close();
}
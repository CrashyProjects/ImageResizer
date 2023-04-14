# Image Resizer
Image Resizer is a versatile tool that can resize any image contained in a specified folder. By default it saves a copy of the resized image as "RESIZED_imageOriginalName.originalExtension" resized to a YouTube Short format; 1080x1920.

Looking for a Image Compressor? Try this one: https://github.com/CrashyProjects/ImageCompressor

### Requirements
-   Python 3.x
-   PIL Library

### Usage
Run it with the following command:
   ```
    python3 imageResizer.py
   ```

Alternatively, run it with a specified directory:
   ```
    python3 imageResizer.py photoDirectory
   ```

## Configuration
To use the image resizer tool, you can configure it by setting the following parameters in the config.py file:

`directory`: The default directory where the images to be resized are located. If not passed as argument, the default value is set to the current directory ".".

`destination`: Desired destination path, if set to "" will be the same as "directory". Default value is "", the same directory.

`saveCopy`: If True, a copy of the resized image will be saved as "RESIZED_filename.ext", if False, the original image will be overwritten. Default value is True.

`resizeRes`: Desired resize dimensions in pixels (width, height). Default value is (1080, 1920).

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

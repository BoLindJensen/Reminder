''' A module for dealing with BMP bitmap image files.'''

def write_grayscale(filename, pixels):



    '''Creates and writes a grayscale BMP file.

    Args:
        :param filename: The name of the BMP file to be created

        :param pixels:  A rectangular image stored as a sequence of rows.
        each row must be an iterable series of integers in the range 0-255
    Raises:
        OSError: if the file couldn't be written
    '''

    height = len(pixels)
    width = len(pixels)

    with open(filename, 'wb') as bmp:  # Encoding does not make sense when working with raw binary files.
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      #The next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little edian integer. Zero place holder for now

        bmp.write(b'\x00\x00') # unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00') # unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell() # The next four bytes hold the integer offset
        bmp.write(b'\x00\x00\x00\x00')     # to the pixel data. Zero placeholder for now


        # Image Header

        #Little-Endian = least significant byte is written first

        bmp.write(b'\x28\x00\x00\x00') # Image header size in bytes - 40 Decimal  (28 bytes = 40 decimal )
        bmp.write(_int32_to_bytes(width))   # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pxels


        missing


        # Color palette - a linear
        for c in range(256):  # gives 255
            bmp.write(bytes((c,c,c,0)))     # Blue, Green, Red, Zero



        # Pixel data
            missing



        # End of file
        eof_bookmark = bmp.tell()

        # Fill in pixel size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))



def _int32_to_bytes(i):
    '''Convert an integer to four byutes in little-endian format'''
    # 4 bytes sequence
    return bytes((i & 0xff,
                  i >> 8 & 0xff,            # >> shift right
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))

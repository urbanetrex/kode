def save_bmp(filename, matrix):
    """
    Save a 2D matrix of RGB values to a BMP file.
    :param filename: The name of the file to save to.
    :param matrix: A 2D matrix of RGB values, where each value is a tuple (R, G, B).
    """
    height = len(matrix)
    width = len(matrix[0])
    
    # BMP Header
    file_size = 54 + 3 * width * height  # 54-byte header + pixel data
    header = bytearray([
        0x42, 0x4D,             # Signature "BM"
        file_size & 0xFF, (file_size >> 8) & 0xFF, (file_size >> 16) & 0xFF, (file_size >> 24) & 0xFF,
        0, 0, 0, 0,             # Reserved
        54, 0, 0, 0,            # Offset to pixel data
        40, 0, 0, 0,            # DIB header size
        width & 0xFF, (width >> 8) & 0xFF, 0, 0,  # Width
        height & 0xFF, (height >> 8) & 0xFF, 0, 0, # Height
        1, 0,                   # Color planes
        24, 0,                  # Bits per pixel (RGB)
        0, 0, 0, 0,             # Compression
        0, 0, 0, 0,             # Image size (can be 0)
        0, 0, 0, 0,             # Horizontal resolution (not needed)
        0, 0, 0, 0,             # Vertical resolution (not needed)
        0, 0, 0, 0,             # Number of colors
        0, 0, 0, 0              # Important colors
    ])

    # Pixel Data (BMP stores pixels bottom to top)
    pixel_data = bytearray()
    for row in reversed(matrix):  # BMP stores bottom to top
        for r, g, b in row:
            pixel_data += bytes([b, g, r])  # BMP uses BGR format
        while len(pixel_data) % 4 != 0:  # BMP rows must be padded to 4-byte boundary
            pixel_data.append(0)

    # Write to file
    with open(filename, "wb") as f:
        f.write(header + pixel_data)


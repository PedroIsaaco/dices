from enum import Enum

def get_value(contents, offset, length):
    return int.from_bytes(contents[int(offset):int(offset + length)], byteorder='little')

def get_bytes(contents, offset):
    return contents[int(offset):]

class Value(Enum):
    ONE = 1,
    TWO = 2,
    THREE = 3,
    FOUR = 4,
    FIVE = 5,
    SIX = 6

class BmpImage:
    def __init__(self, file_path):
        #referring to https://de.wikipedia.org/wiki/Windows_Bitmap
        self.bmp_contents = self.load(file_path)
        self.data_offset = get_value(self.bmp_contents, 10, 4) #bfOffBits
        self.x_size = get_value(self.bmp_contents, 18, 4) #biWidth
        self.y_size = get_value(self.bmp_contents, 22, 4) #biHeight
        self.bit_count = get_value(self.bmp_contents, 28, 2) #bBitCount
        self.compression = get_value(self.bmp_contents, 30, 4) #biCompression
        self.data_size = get_value(self.bmp_contents, 34, 4) #biSizeImage

        if 'eins' in file_path:
            self.value = 1
        elif 'zwei' in file_path:
            self.value = 2
        elif 'drei' in file_path:
            self.value = 3
        elif 'vier' in file_path:
            self.value = 4
        elif 'fuenf' in file_path:
            self.value = 5
        elif 'sechs' in file_path:
            self.value = 6
        #if self.data_size == 0 and self.compression == 0:
        #    self.data_size = (self.x_size + (4 - self.x_size % 4)) * self.y_size * self.bit_count / 8
        #else:
        #    print("warning output -> not specified")
        self.bmp_data = get_bytes(self.bmp_contents, self.data_offset)
            
    def load(self, file_path):
        file_content = []
        with open(file_path, "rb") as f:
            while (byte := f.read(1)):
                file_content += byte
        return file_content

    def get_content(self):
        return self.bmp_contents

    def get_value(self):
        return self.value

    def output(self):
        print("test output")
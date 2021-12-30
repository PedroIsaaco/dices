import os
import glob
import csv
import numpy as np
from bmp_image import BmpImage

def create_random_dataset(max, bmp_dir, filename):
    header_written = False
    file_count = len(glob.glob(bmp_dir))
    rnd_numbers = np.random.randint(0, file_count, max)
    outfile = filename + "_rnd.csv"
    with open(outfile, mode='w', newline='') as diceroll_file:
        for file_index in rnd_numbers:
            bmp_file = glob.glob(bmp_dir)[file_index]
            #print("writing file '%s' (at index %d) to file '%s'" %(bmp_file, file_index, outfile))
            bmp_image_obj = BmpImage(bmp_file)
            file_bmp_data = [bmp_image_obj.value] + bmp_image_obj.bmp_data
            length = len(file_bmp_data)
            if not header_written:
                print("writing column headers ...")
                numbers = [str(x) for x in range(0, length - 1)]
                numbers.insert(0, "value")
                header_writer = csv.writer(diceroll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                header_writer.writerow(numbers)
                header_written = True
                print("writing row contents ...")
            dices_writer = csv.writer(diceroll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dices_writer.writerow(file_bmp_data)
                
    print("done. data written to '%s'" %(outfile))
    return outfile

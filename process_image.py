import os
import glob
import csv
import numpy as np
from bmp_image import BmpImage

def include_column_titles(file, max):
    numbers = [str(x) for x in range(0, max)]
    numbers.insert(0, "value")
    numbers_list = ",".join(numbers) + "\n"

    with open(file, "r") as f:
        contents = f.readlines()

    contents.insert(0, numbers_list)

    file_name, file_ext = os.path.splitext(file)
    file_new = file_name + "_new" + file_ext
    with open(file_new, "w") as f:
        f.write("".join(contents))

def create_random_dataset(max, bmp_dir, filename):
    file_count = len(glob.glob(bmp_dir))
    rnd_numbers = np.random.randint(0, file_count, max)
    outfile = filename + "_rnd.csv"
    with open(outfile, mode='w', newline='') as diceroll_file:
        for file_index in rnd_numbers:
            bmp_file = glob.glob(bmp_dir)[file_index]
            print("writing file '%s' (at index %d) to file '%s'" %(bmp_file, file_index, outfile))
            bmp_image_obj = BmpImage(bmp_file)
            dices_writer = csv.writer(diceroll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            dices_writer.writerow([bmp_image_obj.value] + bmp_image_obj.bmp_data)
            length = bmp_image_obj.data_size
    print("including column headers ...")
    include_column_titles(outfile, length) #will be 120000

bmp_dir = './Images/target_output/*.*'
debug = True #switch here
if (debug):
    filename = 'diceroll_reduced'
else:
    filename = 'diceroll'

include_column_titles("test.csv", 6)
#create_random_dataset(10, bmp_dir, filename)
#csv: https://realpython.com/python-csv/
print('done.')
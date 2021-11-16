import glob
import csv
from bmp_image import BmpImage

bmp_dir = './Images/target_output/*.*'
bmp_dir_slim = './Images/target_output/wuerfel_00036_b*.*'
filename = 'diceroll.csv'
filename_slim = 'diceroll_slim.csv'
filename_slim = 'diceroll_slim_short.csv'
i = 0
with open(filename_slim, mode='w', newline='') as diceroll_file:
    for bmp_file in glob.glob(bmp_dir):    
        bmp_image_obj = BmpImage(bmp_file)
        dices_writer = csv.writer(diceroll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dices_writer.writerow([bmp_image_obj.value] + bmp_image_obj.bmp_data)
        i += 1
        if i > 100:
            exit()
#csv: https://realpython.com/python-csv/
print('done.')
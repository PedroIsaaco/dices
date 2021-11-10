import glob
import csv
from bmp_image import BmpImage

bmp_dir = './Images/target_output/*.*'
with open('diceroll.csv', mode='w', newline='') as diceroll_file:
    for bmp_file in glob.glob(bmp_dir):    
        bmp_image_obj = BmpImage(bmp_file)
        dices_writer = csv.writer(diceroll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dices_writer.writerow([bmp_image_obj.value] + bmp_image_obj.bmp_data)
#csv: https://realpython.com/python-csv/
print('done.')
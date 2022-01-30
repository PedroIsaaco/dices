import os
import glob
from createcsv.image_db import get_xml_file
from createcsv.image_db import get_object_info
from createcsv.image_db import create_image

every_obj = []
base_dir = './Images/target/'
output_dir = './Images/target_output/'
file_filter = '*.jpg'
full_path = '%s%s' % (base_dir, file_filter)
total_max = 0
for jpg_file in glob.glob(full_path):
    xml_file = get_xml_file(jpg_file)
    result, total_max = get_object_info(jpg_file, xml_file, total_max)
    every_obj.extend(result)

if not(os.path.isdir(output_dir)):
    os.mkdir(output_dir)

for obj in every_obj:
    create_image(obj, output_dir, total_max)
    #obj.output()
print('Found %d objects in total' % len(every_obj))
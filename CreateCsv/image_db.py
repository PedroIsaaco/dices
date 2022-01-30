import os
import xml.dom.minidom
from xml.dom.minidom import parse
from jpg_data_object import ImgDataObject
from PIL import Image

def get_region(file_path, x1, y1, x2, y2):
    img = Image.open(file_path)
    return img.crop((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

def create_image(data_obj, base_outdir, total_max):
    img = get_region(data_obj.filename_jpg, data_obj.x1, data_obj.y1, data_obj.x2, data_obj.y2)
    img = img.resize((total_max, total_max), Image.ANTIALIAS)
    filename = get_new_filename(base_outdir, get_filename(data_obj.filename_jpg), data_obj.label)
    #check if filename exists
    img.save(filename, "BMP")

def get_filename(file_path):
    filename_jpg, file_ext = os.path.splitext(os.path.basename(file_path))
    return filename_jpg

def get_new_filename(base_outdir, filename, label):
    count = 1
    new_filename = '%s/%s_%s.bmp' % (base_outdir, filename, label)
    while os.path.isfile(new_filename):
        count += 1
        new_filename = '%s/%s_%s%d.bmp' % (base_outdir, filename, label, count)
    return new_filename

def get_xml_file(file_path_jpg):
    filename_jpg = get_filename(file_path_jpg)
    dirname_jpg = os.path.dirname(file_path_jpg)
    count_undrscr = filename_jpg.count('_')
    if (count_undrscr < 2) | (filename_jpg.endswith('flip')) | (filename_jpg.endswith('mirror')):
        new_file_name = file_path_jpg.replace('.jpg', '.xml')
    else:
        last_index = filename_jpg.rindex('_')
        new_file_name = "%s/%s%s" % (dirname_jpg, filename_jpg[0:last_index], '.xml')
    #print('Mapping %s to %s' % (file_path_jpg, new_file_name))
    return new_file_name

def get_object_info(file_path_img, file_path_xml, total_max):
    DOMTree = xml.dom.minidom.parse(file_path_xml)
    collection = DOMTree.documentElement
    result_arr = []
    #total_max = 0

    file_folder = collection.getElementsByTagName('folder')[0].childNodes[0].data
    file_name = collection.getElementsByTagName('filename')[0].childNodes[0].data
    objects = collection.getElementsByTagName('object')
    for obj in objects:
        label = obj.getElementsByTagName('name')[0].childNodes[0].data
        bnd_box_coll = obj.getElementsByTagName('bndbox')
        for s in bnd_box_coll:
            xmin = s.getElementsByTagName('xmin')[0].childNodes[0].data
            xmax = s.getElementsByTagName('xmax')[0].childNodes[0].data
            ymin = s.getElementsByTagName('ymin')[0].childNodes[0].data
            ymax = s.getElementsByTagName('ymax')[0].childNodes[0].data
            if abs(int(xmax) - int(xmin)) > total_max:
                total_max = abs(int(xmax) - int(xmin))
        
        jpg_data_obj = ImgDataObject(file_path_img, file_path_xml, xmin, ymin, xmax, ymax, label)
        result_arr.append(jpg_data_obj)
    return result_arr, total_max
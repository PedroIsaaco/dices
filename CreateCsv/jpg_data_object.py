class JpgDataObject:
    def __init__(self, filename_jpg, filename_xml, x1, y1, x2, y2, label):
        dist_x = abs(int(x2) - int(x1))
        dist_y = abs(int(y2) - int(y1))
        if dist_x < dist_y:
            offset = (dist_y - dist_x) / 2
            self.x1 = int(x1)
            self.y1 = int(y1) + offset
            self.x2 = int(x2)
            self.y2 = int(y2) - offset
        else:
            offset = (dist_x - dist_y) / 2
            self.x1 = int(x1) + offset
            self.y1 = int(y1)
            self.x2 = int(x2) - offset
            self.y2 = int(y2)

        self.filename_jpg = filename_jpg
        self.filename_xml = filename_xml
        self.label = label

    def output(self):
        print("Object found in '%s' referenced in '%s' at coordinates %s/%s -> %s/%s has label %s"
            %(self.filename_jpg, self.filename_xml, self.x1, self.y1, self.x2, self.y2, self.label))
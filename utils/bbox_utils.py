# def get_center_of_box(bbox):
#     x1, y1, x2, y2 = bbox
#     return int((x1+x2)/2),int((y1+y2)/2)

# def get_bbox_width(bbox):
#     return bbox[2]-bbox[0]
def get_center_of_box(bbox):
    x_center = int((bbox[0] + bbox[2]) / 2)
    y_center = int((bbox[1] + bbox[3]) / 2)
    return x_center, y_center

def get_bbox_width(bbox):
    width = int(bbox[2] - bbox[0])
    return width

def measure_distance(p1, p2):
    return((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def measure_xy_distance(p1,p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)
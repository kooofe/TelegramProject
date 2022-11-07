import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


def count_obj():
    # file read
    img = cv2.imread('static/image.jpg')
    # detected
    box, label, count = cv.detect_common_objects(img)
    output = draw_bbox(img, box, label, count)
    # write
    cv2.imwrite('static/result.jpg', output)
    # output
    return str(len(label))
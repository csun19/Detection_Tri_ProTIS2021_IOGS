import cv2


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):

        shape = "forme"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)


        if len(approx) == 3:
            shape = "triangle"


        elif len(approx) == 4:

            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            shape = "carre" if ar >= 0.9 and ar <= 1.1 else "rectangle"

        elif len(approx) > 4:
            shape = "cercle"
        

        return shape

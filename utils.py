import cv2

def show_image(window_name, image):
    cv2.imshow(window_name, image)

def close_window():
    cv2.waitKey(0)
    cv2.destroyAllWindows()
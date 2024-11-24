import cv2

img = cv2.imread("Rgb_Code.png")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Image", img)
print("The Shape of the image is: ", RGB_img.shape, "\n")

def getEventCoordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("The RGB color value at coordinates [Height = {0} and Width = {1}] is: {2}".format(y, x, RGB_img[y][x]))
        
cv2.setMouseCallback('Image', getEventCoordinates)


cv2.waitKey(0)
cv2.destroyAllWindows()

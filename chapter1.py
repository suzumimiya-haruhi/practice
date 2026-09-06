import cv2
print("Package Imported")

img1 = cv2.imread("./Resources/lena.png")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,100)

while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# cv2.imshow("Output", img1)
# cv2.waitKey(0)
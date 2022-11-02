from cvzone.FaceDetectionModule import FaceDetector
from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()
detector2 = PoseDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)


    img = detector2.findPose(img)
    lmList, bboxInfo = detector2.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
import cv2
import os

vidPath = r"C:\Users\daksh\Desktop\VSCode\SurveillanceBot\cnn_facial_reco\opencv_imutils\shopping_mall.mp4"

video = cv2.VideoCapture(vidPath)
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
i=0
while True:
    i+=1
    # Capture frame-by-frame
    ret, frame = video.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("frame_" + str(i) + ".jpg", gray)
    
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    
    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = frame[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite('frame_' + str(i) + '_' + str(w) + str(h) + '_faces.jpg', roi_color)

    status = cv2.imwrite('faces_detected.jpg', frame)
    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
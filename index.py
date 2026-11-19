import cv2 

face_cascade = cv2.CascadeClassifier(
  cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
video = cv2.VideoCapture(0)
if video.isOpened():
  validacao, frame = video.read()
  while validacao:
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = face_cascade.detectMultiScale(cinza, scaleFactor=1.2, minNeighbors=5)

    for(x, y,w, h) in rostos:

      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("camera", frame)
    validacao, frame = video.read()

    key = cv2.waitKey(5)
    if key == 27:
      break
cv2.imwrite("foto.png", frame)



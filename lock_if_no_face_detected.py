import cv2
import sys
import subprocess
import time

cascPath = 'cascades.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
SECONDS_TO_LOCK_SCREEN = 10
start = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(faces)==0:
      delta = time.time()
      if delta-start > SECONDS_TO_LOCK_SCREEN:
        subprocess.call('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend', shell=True)
    else:
      start = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
# import the opencv library
import cv2
import face_recognition

from config import *

# define a video capture object
vid = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(CASC_PATH)
import os

print(os.path.exists(CASC_PATH))


def take_image():
    ret, image = vid.read()
    return image


def cv2_face_recognition(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv_faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return cv_faces


def fr_face_recognition(image):
    return face_recognition.face_locations(image)


def main(*args, **kwargs):
    
    cv2.imshow(FRAME_NAME, take_image())

    while(True):

        if(cv2.getWindowProperty(FRAME_NAME, 1) < 0):
            break

        if cv2.waitKey(1) == ESCAPE_KEY:
            break
        # Capture the video frame
        # by frame
        image = take_image()
        # Detect faces in the image
        cv_faces = cv2_face_recognition(image)
        fr_faces = fr_face_recognition(image)

        if DEBUG:
            print(fr_faces)
            print(cv_faces)

        # Draw a rectangle around the faces
        for (x, y, w, h) in cv_faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 2)

        for (top, right, bottom, left) in fr_faces:
            cv2.rectangle(image, (left, top), (right, bottom), RED, 2)

        cv2.imshow(FRAME_NAME, image)

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

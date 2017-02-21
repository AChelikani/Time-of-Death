import picamera


class Photograph(object):
    def __init__(self):
        self.camera = picamera.PiCamera()

    def takePicture(self):
        camera.capture("image.jpg")

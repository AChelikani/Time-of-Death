from Tkinter import *
#import takePicture
import deathPrediction
import time

class CubeView(object):
    def __init__(self):
        self.root = Tk()
        #self.camera = takePicture.Photograph()
        self.engine = deathPrediction.DeathPredictor()
        self.root.wm_attributes("-fullscreen", True)
        self.dateVar = StringVar()
        self.label = Label(self.root, textvariable=self.dateVar, font=("Helvetica", 100), bg="black", fg="white", pady=100)
        self.root.bind('<Left>', self.run)
        self.root.bind('<Up>', self.photograph)
        self.root.configure(background="black")
        self.root.mainloop()

    def run(self, event):
        self.labelTest()
        #time.sleep(5)
        #self.setPhase2()
        #time.sleep(5)
        #self.setPhase3()

    def createLabel(self, prediction):
        lab = prediction["month"] + " " + prediction["day"] + ", " + prediction["year"]
        self.dateVar.set(lab)
        self.label.pack()

    def photograph(self, event):
        self.camera.takePicture()
        age = self.engine.agePredict("image.jpg")
        prediction = self.engine.deathPredict(age)
        self.createLabel(prediction)

    def labelTest(self):
        age = self.engine.agePredict("face1.jpg")
        prediction = self.engine.deathPredict(age)
        self.createLabel(prediction)

    def setPhase2(self):
        self.dateVar.set("Spend every moment of your life deliberately.")
        self.label.pack()

    def setPhase3(self):
        self.dateVar.set("You're still here. Is it because you want to be?")
        self.label.pack()


if __name__ == "__main__":
    cv = CubeView()

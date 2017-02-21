from Tkinter import *
import takePicture
import deathPrediction

class CubeView(object):
    def __init__(self):
        self.root = Tk()
        self.camera = takePicture.Photograph()
        self.engine = deathPrediction.DeathPredictor()
        self.root.wm_attributes("-fullscreen", True)
        self.dateVar = StringVar()
        self.label = Label(self.root, textvariable=self.dateVar, font=("Helvetica", 100), pady=100)
        self.root.bind('<Left>', self.run)
        self.root.bind('<Right>', self.refresh)
        self.root.mainloop()

    def run(self, event):
        self.dateVar.set("Hey")
        self.label.pack()

    def refresh(self, event):
        self.dateVar.set("Yo")
        self.label.pack()

    def createLabel(self, prediction):
        lab = prediction["month"] + " " + prediction["day"] + ", " + prediction["year"]
        self.dateVar.set(lab)
        self.label.pack()

    def photograph(self, event):
        self.camera.takePicture()
        age = self.engine.agePredict("image.jpg")
        prediction = self.engine.deathPredictNaive(age)
        self.createLabel(prediction)


if __name__ == "__main__":
    cv = CubeView()

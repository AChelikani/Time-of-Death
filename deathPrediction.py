import angus
from pprint import pprint
import constants
import random


class DeathPredictor(object):
    def __init__(self):
        conn = angus.connect()
        self.service = conn.services.get_service('age_and_gender_estimation', version=1)
        self.ageDist = self.parseAgeDict("ageDist.txt")

    # Predict the age of the person in a given picture
    def agePredict(self, imgPath):
        job = self.service.process({'image': open(imgPath, "rb")})
        return job.result["faces"][0]["age"]

    # Predict the time of death of a person given their current age
    def deathPredictNaive(self, age):
        prediction = {}
        yearsUntilDeath = int(constants.LIFE_EXPECTANCY - age)
        prediction["year"] = str(constants.TODAY_YEAR + yearsUntilDeath)
        prediction["month"] = constants.MONTHS[constants.TODAY_MONTH - 1]
        prediction["day"] = str(constants.TODAY_DAY)
        return prediction

    def parseAgeDict(self, fname):
        d = {}
        age = 1
        with open(fname, 'r') as f:
            for line in f:
                d[age] = float(line.rstrip())
                age += 1
        return d

    def deathPredict(self, age):
        prediction = {}
        if int(age) == age:
            yearsUntilDeath = int(self.ageDist[age])
        else:
            yearsUntilDeath = int(self.ageDist[int(age)] + (self.ageDist[int(age+1)]-self.ageDist[int(age)])*(age - int(age)))
        prediction["year"] = str(constants.TODAY_YEAR + yearsUntilDeath)
        prediction["month"] = constants.MONTHS[random.randint(0,11)]
        prediction["day"] = str((constants.TODAY_DAY + random.randint(0,31))%27 + 1)
        return prediction


if __name__ == "__main__":
    dp = DeathPredictor()
    age = dp.agePredict("face1.jpg")
    print dp.deathPredict(age)

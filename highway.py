import numpy as np
import copy
class car:
    def __init__(self,speed,pos,passing,passingCar):
        
        self.speed = speed
        self.pos = pos
        self.passing = passing
        self.passingCar = passingCar

class traffic:
    def __init__(self,cars):
        self.cars = cars

    def getLeader(self):

        maxPos = -1e20
        for i in range(len(self.cars)):
            if self.cars[i].pos > maxPos:
                maxPos = self.cars[i].pos
                leader = i

        return self.cars[i]

    def getSpeeds(self):
        speeds = np.zeros((len(self.cars)))
        for i in range(len(speeds)):
            speeds[i] = self.cars[i].speed

        return speeds

    def getPos(self):
        pos = np.zeros((len(self.cars)))
        for i in range(len(pos)):
            pos[i] = self.cars[i].pos

        return pos

        
def createTraffic(num,speed,std,spacing):
    posList = np.arange(0,spacing*(num+1),spacing)
    cars = []
    for i in range(num):
        cars.append(car(np.random.randn()*5+speed,posList[i],False,None))

    return traffic(cars)

def getNearestCar(carSpecial,traffic):
    dist = 1e20

    for car in traffic.cars:
        tmpDist = abs(car.pos-carSpecial.pos)
        if (car.pos > carSpecial.pos) and (tmpDist <= dist):
            dist = copy.copy(tmpDist)
            returnCar = car
    return returnCar

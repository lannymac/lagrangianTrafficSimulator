import numpy as np
import copy
class car:
    def __init__(self,speed,pos,name,lane,blocked):
        
        self.speed = speed
        self.pos = pos
        self.lane = lane
        self.name = name
        self.blocked = blocked
        self.initialSpeed = copy.copy(speed)
        
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

    def getNames(self):
        names = []
        for i in range(len(self.cars)):
            names.append(self.cars[i].name)

        return np.array(names)

    def getLanes(self):
        lanes = np.zeros((len(self.cars)),dtype=int)
        for i in range(len(lanes)):
            lanes[i] = self.cars[i].lane

        return lanes


        
def createTraffic(num,speed,std,spacing):
    posList = np.arange(0,spacing*(num+1),spacing)
    cars = []
    for i in range(num):
        name = 'Car%02d' % (i+1)
        cars.append(car(np.random.randn()*5+speed,posList[i],name,0,False))

    return traffic(cars)

def getNearestCar(carSpecial,traffic,lane):
    dist = 1e20
    returnCar = None
    for car in traffic.cars:
        tmpDist = abs(car.pos-carSpecial.pos)
        if (car != carSpecial) and (tmpDist < dist) and (lane == car.lane):
            dist = tmpDist
            returnCar = car
    return returnCar

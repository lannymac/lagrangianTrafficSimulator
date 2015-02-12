import highway
import ConfigParser
import sys
import numpy as np
import pylab as pl
config = ConfigParser.ConfigParser()
config.read('input.cfg')
numberOfCars = config.getint("OPTIONS","numberOfCars")
speedLimit = config.getfloat("OPTIONS","speedLimit")
passingSpeed= config.getfloat("OPTIONS","passingSpeed")
speedStd   = config.getfloat("OPTIONS","speedStd")
carSpacing   = config.getfloat("OPTIONS","carSpacing")
dt   = config.getfloat("OPTIONS","dt")
tFinal   = config.getfloat("OPTIONS","tFinal")
numberOfLanes  = config.getint("OPTIONS","numberOfLanes")
saveToFile  = config.getboolean("OPTIONS","saveToFile")

traffic = highway.createTraffic(numberOfCars,speedLimit,speedStd,carSpacing)

if saveToFile:
    fPos = open('pos.csv','w')
    fLane = open('lane.csv','w')

t = 0

while t < tFinal:
    for car in traffic.cars:

        car.pos += car.speed*dt

    
        nearestCarCurrentLane = highway.getNearestCar(car,traffic,car.lane)
        nearestCarNextLane = highway.getNearestCar(car,traffic,car.lane+1)
        nearestCarPreviousLane = highway.getNearestCar(car,traffic,car.lane-1)

        if (nearestCarCurrentLane != None)  and (nearestCarCurrentLane.speed < car.speed) and (car.lane < numberOfLanes) and (nearestCarCurrentLane.pos - car.pos  < 5) and (nearestCarCurrentLane.pos - car.pos  > 0.) and ((nearestCarNextLane == None) or abs(car.pos - nearestCarNextLane.pos) > 5) :
            car.lane +=1
            
        elif (nearestCarCurrentLane != None)  and (nearestCarCurrentLane.speed < car.speed) and (car.lane < numberOfLanes) and (nearestCarCurrentLane.pos - car.pos  < 5) and ((nearestCarNextLane != None) and abs(car.pos - nearestCarNextLane.pos) < 5) :
            car.speed = nearestCarCurrentLane.speed
            car.blocked = True

        elif (nearestCarCurrentLane != None)  and ((nearestCarNextLane == None) or abs(car.pos - nearestCarNextLane.pos) > 5) and car.blocked:
            car.speed = car.initialSpeed
            car.blocked = False

        elif car.lane > 0 and (nearestCarPreviousLane == None or (abs(car.pos - nearestCarPreviousLane.pos) > 5)):
            car.lane -=1
    for i in range(len(traffic.getPos())):
        fPos.write(str(traffic.getPos()[i])+'\t')
        fLane.write(str(traffic.getLanes()[i])+'\t')

        if i == len(traffic.getPos())-1:
            fPos.write('\n')
            fLane.write('\n')


    t += dt
fPos.close()
fLane.close()

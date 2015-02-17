import highway
import ConfigParser
import sys
import numpy as np
import pylab as pl

config = ConfigParser.ConfigParser()
config.read('input.cfg')

dt   = config.getfloat("OPTIONS","dt")
tFinal   = config.getfloat("OPTIONS","tFinal")
numberOfLanes  = config.getint("OPTIONS","numberOfLanes")
saveToFile  = config.getboolean("OPTIONS","saveToFile")

traffic = highway.createTraffic()


fPosition = open('pos.csv','w')
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
            car.blockedFromPassing = True

        elif (nearestCarCurrentLane != None)  and ((nearestCarNextLane == None) or abs(car.pos - nearestCarNextLane.pos) > 5) and car.blockedFromPassing:
            car.speed = car.initialSpeed
            car.blockedFromPassing = False

        elif car.lane > 0 and (nearestCarPreviousLane == None or (abs(car.pos - nearestCarPreviousLane.pos) > 10)):
            car.lane -=1
    
    traffic.savePosition(fPosition)
    traffic.saveLane(fLane)


    t += dt
fPosition.close()
fLane.close()

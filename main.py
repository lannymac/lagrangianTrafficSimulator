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

traffic = highway.createTraffic(numberOfCars,speedLimit,speedStd,carSpacing)

t = 0

while t < tFinal:

    fig = pl.figure(figsize=(1,10))
    ax = fig.add_subplot(111)

    for car in traffic.cars:

        car.pos += car.speed*dt

        if car.pos >= traffic.getLeader().pos:
            pass
        else:
            nearestCar = highway.getNearestCar(car,traffic)
            if (nearestCar.pos - car.pos <5) and (nearestCar.speed < car.speed):
                car.passing = True
                car.passingCar = nearestCar
                
        if car.passing and (car.pos - car.passingCar.pos) > 5:
            car.passing = False
            car.passingCar = None

        if car.passing:
            c='r'
            j = 0
        else:
            c='b'
            j = 1
        ax.scatter(j,car.pos,c=c)
        ax.set_xlim(-.5,1.5)
        ax.set_ylim(0,500)
    pl.savefig('plots/%.2f.png' % (t))
    pl.close('all')
    t += dt

from pylab import *

pos= genfromtxt('pos.csv',delimiter=',')
pos = ma.masked_invalid(pos)

lane = genfromtxt('lane.csv',delimiter=',')
lane *= -1.
lane = ma.masked_invalid(lane)
uniqueLanes = np.unique(lane)
dots = zeros((len(uniqueLanes)-1))
for i in range(len(dots)):
    dots[i] = np.mean((uniqueLanes[i],uniqueLanes[i+1]))
for i in range(len(pos)):
    fig = figure(figsize=(2,10))
    ax = fig.add_subplot(111)
    ax.scatter(lane[i],pos[i],)
    ax.set_xlim(lane.min()-.5,lane.max()+.5)
    ax.set_ylim(0,pos.max())
    for j in range(len(dots)):
        ax.plot([dots[j],dots[j]],ax.get_ylim(),'--b',lw=1)
    
    savefig('plots/%05d.png' % i)
    close('all')

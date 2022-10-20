import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from math import sqrt
from collections import namedtuple
import random

point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 'Point1 Point2')
coloured_point = namedtuple('ColouredPoint','Point Side')
coloured_points = set()
lines = {'AB':Line(point(0,0), point(0,1)),
         'BC':Line(point(0,1),point(1,1)),
         'CD':Line(point(1,1),point(1,0))}
         
trials = 1_000_000

def distance_to_line(point, line):
    x0, y0 = point
    x1, y1 = line.Point1
    x2, y2 = line.Point2
    return abs((x2-x1)*(y1-y0)-(x1-x0)*(y2-y1))/sqrt((x2-x1)**2 + (y2-y1)**2)

def closestline(point):
    return coloured_point(point, min(
        ((distance_to_line(point,c),l) for l,c in lines.items()), key=lambda x:x[0])[1])

for n in range(trials):
    pointxy = point(random.random(), random.random())
    coloured_points.add(closestline(pointxy))

#pprint([(cp.Point, cp.Side) for cp in coloured_points])

count = sum(1 for cp in coloured_points if cp.Side == "AB")
print(f'Probaility of random point being closest to line AB : {(count/trials):.3f}')

a = input('Do you want to see the area plot ? [Y/N]')
if a.upper() != 'Y':
    exit()
    

# Plot results
colours = {'AB':'#ff0000', 'BC':'#00FF00','CD':'#0000FF'}

fig, ax = plt.subplots()
ax.set_title(f'Regions closest to the various Edges\n{trials:,} Trials\nProbability of being closest to AB : {count/trials:0.3f}')
ax.scatter( x = [cp.Point.x for cp in coloured_points if cp.Side == 'AB'],
            y = [cp.Point.y for cp in coloured_points if cp.Side == 'AB'],
            color = colours['AB'],
            s = 1,
            label = f'Closest to AB')

ax.scatter( x = [cp.Point.x for cp in coloured_points if cp.Side == 'BC'],
            y = [cp.Point.y for cp in coloured_points if cp.Side == 'BC'],
            color = colours['BC'],
            s = 1,
            label = f'Closest to BC')

ax.scatter( x = [cp.Point.x for cp in coloured_points if cp.Side == 'CD'],
            y = [cp.Point.y for cp in coloured_points if cp.Side == 'CD'],
            color = colours['CD'],
            s = 1,
            label = f'Closest to CD')
plt.legend(loc='best', bbox_to_anchor=(0, 0), fontsize=10, markerscale=5)

for line, coordinate in lines.items():
    ax.annotate(text=line[0], size=15, xy = (0.01 if coordinate[0].x==0 else 0.99, 0.01 if coordinate[0].y==0 else 0.99) )
ax.annotate(text= 'D', xy = (0.99, 0.01),size=15)
plt.show()



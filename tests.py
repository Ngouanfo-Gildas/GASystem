from new_python import *

sol = [Point(1,1), Point(2,1), Point(3,1), Point(7,1), Point(8,1), 
    Point(2,2), Point(2,5), Point(2,6), Point(3,5), Point(3,6),
     Point(6,4), Point(6,5), Point(6,6)]
evt = [Point(1,2), Point(3,2), Point(0,6), Point(8,0), Point(2,0), Point(6,0)]

rs = 2.1
print(len(event_couvert(sol, evt, rs)), len(evt))
fft = fitnessFunction([sol], evt, rs)
for f in fft:
    print(f[1])
show_genome(rs, rs, sol, evt)

# check the composite return of index given random return rate
# also shows the effect of 3x index ETF
from numpy import *

r = random.random(1000)/10-0.05
print mean(r)

r3 = r*3

yr = exp(sum(log(r+1)))
yr3 = exp(sum(log(r3+1)))

ir = exp(sum(log(1-r)))
ir3 = exp(sum(log(1-r3)))

print yr,yr3,ir,ir3

import shower as sh
import numpy as np

x = [16,32,64,128,256,512,1024,2048]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for i in x:
    for j in y:
        a = sh.shower(L = i, p = j)
        a.run(1000000000)
        a.log_sum(7,100)
        a.save()

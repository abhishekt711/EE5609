import numpy as np
import math
Q=np.array([[-2/math.sqrt(5),-1/math.sqrt(5)],[-1/math.sqrt(5),2/math.sqrt(5)]])
R=np.array([[math.sqrt(5)/2,-math.sqrt(5)],[0,5*math.sqrt(5)/2]])
result=Q@R
print(result)

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt(fname="swc-python\data\inflammation-01.csv",delimiter=",")
plt.imshow(data, aspect='auto')
plt.colorbar()
plt.title('Inflammation Data')
plt.xlabel('Day')
plt.ylabel('Patient')
plt.show()


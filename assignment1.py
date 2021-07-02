import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import statistics
from collections import Counter

a = np.array([1, 4, 6, 32, 54, 23, 45, 67, 23, 1, 45, 56, 78, 1, 45, 67, 23, 90, 43, 76])
s = a.sum()
l = len(a)
mean = s/l
median = (a[int(len(a)/2)] + a[int((len(a)/2)+1)])/2
mode = statistics.mode(a)
print('mean = ', mean)
print('median = ', median)
print('mode = ', mode)

# Calculating Mean, Median without using nympy
s2 = 0
b = [1, 4, 6, 32, 54, 23, 45, 67, 23, 1, 45, 56, 78, 1, 45, 67, 23, 90, 43, 76]
for i in range(0, 20):
    s2 = s2 + b[i]
mean2 = s2/l
print('mean not using numpy = ', mean2)

#Calculating Mode

n = len(b)

data = Counter(b)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))

print('mode without libraries = ', get_mode)



#plotting line graph using matplotlib
style.use('ggplot')
x = [1, 2, 3, 4, 5, 6]
y = [6, 7, 2, 8, 4, 9]

x2 = [1, 2, 3, 4, 5, 6]
y2 = [6, 4, 5, 9, 2, 7]

plt.plot(x, y, 'g', label='line one', linewidth=4)
plt.plot(x2, y2, 'r', label='line two', linewidth=4)
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, color='k')
plt.show()

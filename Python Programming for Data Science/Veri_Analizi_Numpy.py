import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))

import numpy as np

a = np.random.randint(1, 10, [3, 3])
b = np.random.randint(1, 10, size=9).reshape(3, 3)

a.reshape(3, 3)

import numpy as np

a = np.random.randint(10, size=10)

a[0:5]

a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]

m[1, 1]

m[2, 3] = 999

m[2, 3] = 2.9

m[:, 2]

m[1, :]

m[0:2, 0:3]

import numpy as np

v = np.arange(0, 30, 3)

v[1]
v[4]

catch = [1, 2, 3]

v[catch]

import numpy as np

v = np.array([1, 2, 3, 4, 5])

p = []

for arr in v:
    if arr < 3:
        p.append(arr)

a = v < 3

v[v != 3]

import numpy as np

v = np.array([1, 2, 3, 4, 5])

v / 5

v * 5 / 10

v ** 2

np.fives(10)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7])

filter_array = array % 2 == 0

new_array = array[filter_array]

print(new_array)


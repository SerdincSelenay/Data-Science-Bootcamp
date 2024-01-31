# Kategorik değişken: stun grafik. countplot bar
# Sayısal değişen: hist, boxplot
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()


plt.boxplot(df["fare"])
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

y = np.array([13, 28, 11, 100])
plt.plot(y, marker = 'o')
plt.show()

plt.plot(y, marker = '*')
plt.show()

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed", color ='r')
plt.show()


x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()


x = np.array([80, 85, 90, 95, 100])
y = np.array([240, 250, 260, 270, 280])
plt.plot(x, y)

plt.title("Bu ana başlık")
plt.xlabel("X ekseni İsimilendirilmesi")

plt.title("Bu ana başlık")
plt.ylabel("Y ekseni İsimilendirilmesi")
plt.grid()
plt.show()

# Plot 1
x = np.array([80, 85, 90, 95, 100])
y = np.array([240, 250, 260, 270, 280])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# Plot 2
x = np.array([8, 9, 10, 15, 11, 15, 12])
y = np.array([24, 20, 26, 27, 280, 29, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# Plot 3
x = np.array([80, 85, 90, 95, 100])
y = np.array([240, 250, 260, 270, 280])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

df["sex"].value_counts().plot(kind="bar")
plt.show()


sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])

type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)


import pandas as pd

df = pd.read_csv("Datasets/advertising.csv")

df.head()

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()


df.index
df[0:13]
df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True) Kalıcı silem yapılmak istendiğinde

df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()

df.index

df["age"] = df.index

df.head()

df.reset_index().head()

df = df.reset_index().head()


import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()


"age" in df
df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())


df[["age"]].head()
type(df[["age"]].head())


df[["age", "alive"]]


col_names = ["age", "adult_male", "alive"]


df["age2"] = df["age"]**2

df["age3"] = df["age"] / df["age2"]

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()



import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
df.iloc[0, 0]


df.loc[0:3]


df.loc[0:3]

df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()
df.loc[df["age"] > 50, ["class", "age"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["class", "age"]].head()

df["embark_town"].value_counts

df_new = df.loc[(df["age"] > 50)& (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
        ["class", "age", "embark_town"]]

df_new["embark_town"].value_counts()


import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()


df.["age"].mean()
df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age" : "mean"})
df.groupby("sex").agg({"age" : ["mean", "sum"]})
df.groupby("sex").agg({"age" : ["mean", "sum"],
                       "survived": "mean"})
df.groupby(["sex","embark_town", "class"]).agg({"age" : ["mean", ],
                       "survived": "mean"})

df.groupby(["sex","embark_town", "class"]).agg({
    "age" : ["mean", ],
    "survived": "mean",
    "sex": "count"})

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df["new_age"] = pd.cut(df["age"], [0, 10 , 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option("display.width", 500)


import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
pd.set_option("display.width", 500)
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5


for col in df.columns:
    if "age" in col:
        print(col)


for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index= True)

df1 = pd.DataFrame({"employes": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employes": ["mark", "john", "dennis", "maria"],
                    "start_date" : [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employes")

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager" : ["Caner", " Mustafa", 'Berkcan']})

pd.merge(df3, df4)

import pandas as pd

from Mistake import gcheck

df = pd.read_csv("../Dataset/Dataset2.csv")

grammer_check = gcheck()

for i in range(137,len(df)) :
	df.loc[i,"Grammer mistakes"] = grammer_check.check(df.loc[i,"essay"])

	df.to_csv("../Dataset/Dataset2.csv")
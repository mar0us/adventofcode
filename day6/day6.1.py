import pandas as pd
import numpy as np
import time


start_time = time.time()

df = pd.read_csv("data.txt", sep="\n")
df = df.to_numpy()

df = np.reshape(df, -1)

sum = 0
for i in df:
	answers = i.split(" ")

	a = []
	for j in answers:
		a.extend(j)

	a = np.array(a)
	a = np.unique(a)
	sum += a.size

print(sum)


print("--- %s seconds ---" % (time.time() - start_time))
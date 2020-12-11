import pandas as pd
import numpy as np
import time

start_time = time.time()

df = pd.read_csv("data.txt", sep="\n")
count = 0
df = df.to_numpy()

df = np.reshape(df, -1)



for i in df:
	i = i.split(" ")
	c = 0
	for j in range(len(i)):
		if i[j].split(":")[0] != "cid":
			c += 1
	if c >= 7:
		count += 1
print(count)



print("--- %s seconds ---" % (time.time() - start_time))
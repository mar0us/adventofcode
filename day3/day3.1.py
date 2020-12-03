import pandas as pd
import numpy as np
import time

start_time = time.time()

df = pd.read_csv("data.txt", sep=':')
df = df.to_numpy()
df = np.reshape(df, -1)

index = 3
countTree = 0

for i in df:
	while len(i) < index:
		i += i

	if i[index] == "#":
		countTree += 1

	index +=3
	
print(countTree)

print("--- %s seconds ---" % (time.time() - start_time))
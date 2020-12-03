import pandas as pd
import numpy as np
import time

start_time = time.time()

df = pd.read_csv("data.txt", sep=':')
df = df.to_numpy()
df = np.reshape(df, -1)

index1, index2, index3, index4 = 1, 3, 5, 7
index5 = 1

countTree1, countTree2, countTree3, countTree4 = 0, 0, 0, 0
countTree5 = 0

mult = 1
j = 0

for i in df:
	while len(i) < index4:
		i += i

	if i[index1] == "#":
		countTree1 += 1
	if i[index2] == "#":
		countTree2 += 1
	if i[index3] == "#":
		countTree3 += 1
	if i[index4] == "#":
		countTree4 += 1

	df[j] = i
	index1 += 1
	index2 += 3
	index3 += 5
	index4 += 7
	j += 1



for i in range(1,df.size,2):
	if df[i][index5] == "#":
		countTree5 += 1
	index5 += 1

mult *= countTree1 * countTree2 * countTree3 * countTree4 * countTree5

print(mult)
print("--- %s seconds ---" % (time.time() - start_time))
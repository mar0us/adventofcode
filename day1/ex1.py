import numpy as np
import pandas as pd
import time

start_time = time.time()

df = pd.read_csv('data.txt', sep = '\n')
df = df.to_numpy()
df = np.reshape(df, -1)
exit = False

#для двух чисел
for i in range(df.size):
	for j in range(i, df.size):
		if df[i] + df[j] == 2020:
			print(df[i] * df[j])
			exit = True
	if exit:
		break
		
exit = False
#для 3х чисел
for i in range(df.size):
	for j in range(i, df.size):
		for k in range(j, df.size):
			if df[i] + df[j] + df[k]== 2020:
				print(df[i] * df[j] * df[k])
				exit = True
	if exit:
		break

#ДЫМА САСАТ
print("--- %s seconds ---" % (time.time() - start_time))


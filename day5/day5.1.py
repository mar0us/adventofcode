import pandas as pd
import numpy as np
import time


start_time = time.time()

df = pd.read_csv("data.txt", sep="\n")
df = df.to_numpy()

df = np.reshape(df, -1)
max = 0
for i in df:
	row = i[:7:]
	collum = i[7::]
	row = row.replace("F","0").replace("B","1")
	collum = collum.replace("R","1").replace("L","0")
	if int(row,2)*8+int(collum,2) > max:
		max = int(row,2)*8+int(collum,2)
print(max)
	


print("--- %s seconds ---" % (time.time() - start_time))
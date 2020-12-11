import pandas as pd
import numpy as np
import time
import collections

start_time = time.time()

df = pd.read_csv("data.txt", sep="\n")
df = df.to_numpy()

df = np.reshape(df, -1)

sum = 0

for i in df:
	answers = i.split(" ")
	s = collections.Counter(answers[0])
	for j in range(len(answers)):
		s = s & collections.Counter(answers[j])
	sum += len(list(s))

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))
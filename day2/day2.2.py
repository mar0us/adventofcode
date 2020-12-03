import pandas as pd
import numpy as np
import time

start_time = time.time()

df = pd.read_csv("data.txt", sep=':')
password = df.to_numpy().T[1::]
letter = df.to_numpy().T[:1:]
letter = np.reshape(letter, -1)
password = np.reshape(password, -1)

j = 0
countPassword = 0
print(password.size)
for i in letter:
	key = i.split(" ")
	count, let = key[0].split("-"), key[1]
	start, end = int(count[0]), int(count[1])
	condition1, condition2 = password[j][start] == let, password[j][end] == let
	if not (condition1 and condition2):
		if condition1 or condition2:
			countPassword += 1
	j += 1

print(countPassword)

print("--- %s seconds ---" % (time.time() - start_time))
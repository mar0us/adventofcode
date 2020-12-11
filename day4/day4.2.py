import pandas as pd
import numpy as np
import time


start_time = time.time()

df = pd.read_csv("data.txt", sep="\n")
count = 0
df = df.to_numpy()

df = np.reshape(df, -1)

ecl = "amb blu brn gry grn hzl oth"

for i in df:
	i = i.split(" ")
	c = 0
	for j in range(len(i)):
		i0 = i[j].split(":")[0]
		i1 = i[j].split(":")[1]
		# byr (Год рождения) - четыре цифры;минимум 1920 и максимум 2002.
		if i0 == "byr" and len(i1) == 4:
			if int(i1) >= 1920 and int(i1) <= 2002:
				c += 1
		#iyr (год выпуска) - четырехзначный; минимум 2010 и максимум 2020.
		if i0 == "iyr" and len(i1) == 4:
			if int(i1) >= 2010 and int(i1) <= 2020:
				c += 1
		# eyr (Expiration Year) - четыре цифры; не менее 2020 г. и не более 2030 г.
		if i0 == "eyr" and len(i1) == 4:
			if int(i1) >= 2020 and int(i1) <= 2030:
				c += 1
		# hgt (Высота) - число, за которым следует см или дюймы:
		# Если см, число должно быть от 150 до 193.
		# Если in, число должно быть от 59 до 76.
		if i0 == "hgt":
			if i1.find("cm") != -1 and int(i1[:-2:]) >= 150 and int(i1[:-2:]) <= 193:
				c += 1
			elif i1.find("in") != -1 and int(i1[:-2:]) >= 59 and int(i1[:-2:]) <= 76:
				c += 1
		# hcl (Цвет волос) -#, за которым следуют ровно шесть символов 0-9 или a-f.
		if i0 == "hcl" and i1[0] == "#" and i1[1::].isalnum:
			# print(int(i1[1::], 16))
			c += 1
		# ecl (Цвет глаз) - в точности одно из: amb blu brn gry grn hzl oth.
		if i0 == "ecl" and ecl.find(i1) != -1:
			c += 1
		# pid (Passport ID) - девятизначное число, включая ведущие нули.
		if i0 == "pid" and len(i1) == 9:
			c += 1
	if c == 7:
		count += 1
print(count)



print("--- %s seconds ---" % (time.time() - start_time))
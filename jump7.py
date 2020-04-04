#if (i % 7 == 0) or ((i % 10 != 0) and (i - i // 10 * 10) % 7 == 0) or ((i > 10) and (i // 10 % 7 == 0)):
for i in range(1, 101):
	if (i % 7 == 0) or ((i % 10 != 0) and (i % 10) % 7 == 0) or ((i > 10) and (i // 10 % 7 == 0)):
		continue
	else:
		print(i)

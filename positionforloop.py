# list init to hold position values

position = []
temp_pos = []
# initial values for position x and y
x_pos = [0, 6]
y_pos = [0, 6]

x = 0
y = 0

	#for loop to create a range of numbers for x while y is 0

for i in y_pos:
	for j in range(6):	
		temp_pos = (j, i)
		if temp_pos not in position:
			position.append(temp_pos)
		else:
			continue


for k in x_pos:
	for n in range(6):
		temp_pos = (k, n)
		if temp_pos not in position:
			position.append(temp_pos)
		else:
			continue

print position



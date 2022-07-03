student_heights = input("Input a list of student heights ").split()

count = 0
sum = 0

for n in range(0, len(student_heights)):
    # convert to int and fill it into list
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    count += 1

average = round(sum / count)

print(average)

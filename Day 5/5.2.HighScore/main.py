student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


max_num = 0

for m in student_scores:
    if m > max_num:
        max_num = m

print(max_num)

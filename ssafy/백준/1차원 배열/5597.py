# import sys
# input = sys.stdin.readline
# T = 28
# n = list(map(int, input().split()))
# n.sort()
# N = set(n)
# students = set(range(1, 31))

# minus_numbers = sorted(list(students - N))
# for number in minus_numbers:
#     print(number)


# import sys
# input = sys.stdin.readline

# T = 28
# students = list(range(1, 31))  
# attended = list(map(int, input().split()))  

# for student in students:
#     if student not in attended:
#         print(student)
#     else:
#         pass

import sys
input = sys.stdin.read

attended = list(map(int, input().split()))  

students = set(range(1, 31))

attended_set = set(attended)

absent_students = sorted(students - attended_set)

for student in absent_students:
    print(student)

# Coded by SpiderX360

arr = input("").split()

#sorting
arr.sort()

min_total = 0
max_total = 0

for i in range(0, (len(arr)-1)):
    min_total = min_total + int(arr[i])

for j in range(1, len(arr)):
    max_total = max_total + int(arr[j])

print(min_total, end=" ")
print(max_total)

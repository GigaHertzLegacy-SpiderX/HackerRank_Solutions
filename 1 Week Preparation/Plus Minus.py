# Coded by SpiderX360
# input

len_arr = int(input(""))
arr = input("").split()
arr = list(arr)


j = 0

def Dividing():
    for j in range(len_arr):
        if int(arr[j]) > 0:
            plus_arr.append(arr[j])

        elif int(arr[j]) == 0:
            zero_arr.append(arr[j])

        elif int(arr[j]) < 0:
            minus_arr.append(arr[j])

        else:
            exit()


# update list

plus_arr = []
minus_arr = []
zero_arr = []

# Function
Dividing()


div_plus = len(plus_arr) / len(arr)
div_min = len(minus_arr) / len(arr)
div_zero = len(zero_arr) / len(arr)

print("{:.6f}".format(div_plus))
print("{:.6f}".format(div_min))
print("{:.6f}".format(div_zero))

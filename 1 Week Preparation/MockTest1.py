def medi(nums):
    added2 = sorted(nums)
    # print(added2)
    if len(added2) % 2 == 0:
        x = float((added2[(len(added2)//2)-1] + added2[(len(added2)//2)]) / 2)
        return print(x)
    else:
        return print(added2[(len(added2))//2])


if __name__=="__main__":
    n = int(input())
    nums = map(int, input().split())
    nums = list(nums)
    if len(nums) == n:
        medi(nums)

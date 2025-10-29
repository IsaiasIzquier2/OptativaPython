
nums = [1,2,3,4,5,6,7,8,9]
sum = 0


for num in nums:
    if num %2 != 0:
        continue
    sum = sum + num

    print(sum)
else:
    print("Fin de la lista")
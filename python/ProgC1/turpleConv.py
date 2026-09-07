oddNumbers=[]
avg = 0
sum = 0
for i in range(10):

    num = int(input("enter num"))

    if num % 2 != 0:
            avg+=num
            sum+=1
            oddNumbers.append(num)

myturpl = (oddNumbers)
print(f"{myturpl} avarge : {(avg/sum):.2f}  total : {avg}")



sum=0
avg=0
c=0
while True:
    n = input("Enter a number or write 'done' to finish: ")
    if(n=="done"):
        break
    try:
        num = int(n)
    except:
        print("Invalid input")
        continue
    sum = sum+num
    c=c+1
    avg = sum/c
print("Sum = ",sum)
print("Avg = ",avg)
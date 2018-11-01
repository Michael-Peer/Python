num =   int(input("enter a number"))
print("your number is: ", num)
cnt=0
numbers_list = ['one', 'two','three','four','five','six','seven','eight','nine']
temp=num
temp2=num
while (temp > 0) :
     temp=temp//10
     cnt=cnt+1

if (cnt==1):
  print("your number is containing 1 digits\n")
  print("your number is: " + numbers_list[num-1])

if (cnt==2):
  print("your number is containing 2 digits\n")
  s = 0
  while (temp2):
        s += temp2 % 10
        temp2 //= 10
  print("the sum of the 2 digits is:", s)
if (cnt==3):
    print("your number is containing 3 digits\n")
    s3 = 1
    while (num):
       s3 = s3 * (num  % 10)
       num //= 10
    print("the sum of the 3 digits is:", s3)

 

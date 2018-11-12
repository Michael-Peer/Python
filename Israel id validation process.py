id_va=input("enter your id")
idvaList=list(id_va)
check_va=[1,2,1,2,1,2,1,2,1]
i=0
#convert list to int list
check_va = [int(i) for i in check_va]
idvaList = [int(i) for i in idvaList]
new_val=[None]*9
#multiple between lists
while i<9:
  new_val[i]=(idvaList[i])*(check_va[i])
  i+=1
new_val = [int(i) for i in new_val]
#Addition all numbers above 9
for x in range(len(new_val)):
  x=int(x)
  sumNum=0
  if new_val[x]> 9:
    while new_val[x]!=0:
      sumNum += new_val[x]%10;
      new_val[x] //=10
    new_val[x]=sumNum
#sum of all the numbers in the list
sumNum=0
for num in range(len(new_val)):
  sumNum+=new_val[num]
if sumNum%10==0:
  print("your id is correct!")
else:
  print("your id isn't correct!")
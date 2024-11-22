list1 = ["A" , "B"]
name = input("1 ve ya 2 secin: ")
if name == "1" or "2":
   if name =="1":
    list1.append("C")   
    print(list1)
   elif name == "2":
       name = input ("hansi deyiseni silirsiz: ")
       list1.remove(name)
       print(list1) 
   else:
       print("yoxdur")


c_list = ["T-shirt", "Sweater"]
c_list.insert(2,"Jeans")
print ("Welcome to our shop, what do you want?")
print ("Our items: ",end="")
for c in c_list:
    print ("{0}{1} ".format(c , ","), end ="")
print()

c_list[1] = "Skirt"
print ("Our items: ",end="")
for c in c_list:
    print ("{0}{1} ".format(c , ","), end ="")
print()

c_list.remove("Jeans")
print(c_list)

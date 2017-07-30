ss_list=[5,7,300,90,24,50,75]

print("Hello, my name is Hiep and these are my sheep sizes")
print(ss_list)
print("Now my biggest sheep has size", max (ss_list), "let's shear it")
ss_list.remove(max(ss_list))
print("After shearing, here is my flock")
print(ss_list)

for i in range (1,5):
    print(i, "month(s) has passed, now here is my flock")
    new_ss_list= [x+50*i for x in ss_list]
    print(new_ss_list)
print("My flock has size in total: ",end="")
s = sum(new_ss_list)
print(s)
print("I would get ",end="")
print ("$",s*2,sep="")

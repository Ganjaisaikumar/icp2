#!/usr/bin/env python
# coding: utf-8

# In[4]:


input11=str(input("Enter your first name"))
input2=str(input("Enter your last name"))
print("Your full name is",(input11+" "+input2))
#2
def string_alternative(s):
    return s[::2]

def main():
    s = "Good evening"
    print(string_alternative(s))

if __name__ == "__main__":
    main()


# In[2]:


file1=open("C:\\Users\\sai\\Desktop\\KOLLI\\input2.txt", 'r+')
linescount={}
for line in file1:
    line=line.split(" ")
    for i in line:
        if i in linescount:
            linescount[i]+=1
        else:
            linescount[i]=1
file1.close()
file2=open("C:\\Users\\sai\\Desktop\\KOLLI\\output1.txt","w")
file2.write("Word_count :\n")
for i,j in linescount.items():
    if i=="\n":
        pass
    else:
        file2.write(i+" : ")
        file2.write(str(j)+"\n")
file2.close()
file1=open("C:\\Users\\sai\\Desktop\\KOLLI\\input2.txt", 'r+')
file2=open("C:\\Users\\sai\\Desktop\\KOLLI\\output1.txt","r+")
print(file1.read())
print("\n")
print(file2.read())


# In[3]:


l=list(map(int,input("Enter the respective heights in inches : ").split(",")))
ans1,ans2=[],[]
for i in l:#using Interactive loop
    ans1.append(i*2.54)#to convert in to centi meters
print(ans1)
ans2=[(j*2.54) for j in l]
print(ans2)


# In[ ]:





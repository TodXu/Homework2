
# coding: utf-8

# In[29]:


import csv

with open('Random_Number_Generator.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

length=len(data)
mylist=[]
for i in range(length):
    mylist.append(int(data[i][0])*3+6)
mylist


# In[30]:


import numpy as np
np.savetxt("Equation_Number_Generator.csv", mylist, delimiter=",", fmt='%s')



# coding: utf-8

# In[9]:


import random

mylist = []

for i in range(0,1000):
    x = random.randint(0,100)
    mylist.append(x)

print(mylist)


# In[21]:


import numpy as np
np.savetxt("Random_Number_Generator.csv", mylist, delimiter=",", fmt='%s')


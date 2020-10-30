
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import csv

with open('Random_Number_Generator.csv', newline='') as f:
    reader = csv.reader(f)
    data1 = list(reader)
list1=[]
for i in range(len(data1)):
    list1.append(int(data1[i][0]))
list1

with open('Equation_Number_Generator.csv', newline='') as f:
    reader = csv.reader(f)
    data2 = list(reader)
list2=[]
for i in range(len(data1)):
    list2.append(int(data2[i][0]))
list2


# In[11]:


plt.plot(list1, list2)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Visualizing 1000 numbers from 0-100 by the equation y=3x+6')
plt.savefig('Visualization.png')
plt.show()


# In[10]:





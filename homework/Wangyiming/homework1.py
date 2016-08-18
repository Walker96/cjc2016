
# coding: utf-8

# # homework1
# ## 王亦茗
# ## 15210130082 

# In[1]:

import random, datetime
import numpy as np
import pylab as plt
import statsmodels.api as sm
from scipy.stats import norm
from scipy.stats.stats import pearsonr


# In[2]:

str(3)


# In[3]:

int('5')


# In[4]:

float('7.1')


# In[5]:

range(10)


# In[6]:

range(1,10)


# In[7]:

dir


# In[8]:

dir(str)[-5:]


# In[9]:

x = ' Hello WorlD  '
dir(x)[-10:]


# In[10]:

x.lower()


# In[11]:

x.upper()


# In[12]:

x.rstrip()


# In[13]:

x.strip()


# In[14]:

x = 'hello world'
type(x)


# In[16]:

l = [1,2,3,3]
t = (1,2,3,3)
s = set([1,2,3,3])
d = {'a':1,'b':2,'c':3}
a = np.array(1)
print l,t,s,d,a


# In[17]:

l=[1,2,3,3]
l.append(4)
l


# In[18]:

d = {'a':1,'b':2,'c':3}
d.keys()


# In[19]:

d = {'a':1,'b':2,'c':3}
d.values()


# In[20]:

d = {'a':1,'b':2,'c':3}
d['b']


# In[21]:

d = {'a':1,'b':2,'c':3}
d.items()


# In[22]:

def devidePlus(m,n):
    return float(m)/n+1


# In[23]:

devidePlus(1,2)


# In[24]:

range(10)


# In[25]:

range(1,10)


# In[26]:

for i in range(10):
    print i, i*10, i**2 


# In[27]:

for i in range(10):
    print i*10


# In[28]:

r = [devidePlus(i,2) for i in range(10)]
r


# In[30]:

map(devidePlus,[4,2],[2,1])


# In[31]:

j = 3
if j%2 == 1:
    print r'余数是1'
elif j%2 ==2:
    print r'余数是2'
else:
    print r'余数既不是1也不是2'


# In[35]:

x = 5
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z)


# In[36]:

j = 0
while j <10:
    print j
    j+=1


# In[38]:

j = 0
while j < 10:
    if j%2 != 0:
        print j**2
    j+=1


# In[39]:

j = 0
while j <50:
    if j == 30:
        break
    if j%2 != 0: 
        print j**2
    j+=1


# In[40]:

for i in [2, 0, 5]:
    try:
        print devidePlus(4, i)
    except Exception, e:
        print e
        pass


# In[43]:

data = [[i, i**2, i**3] for i in range (10)]
data


# In[44]:

for i in data:
    print '\t'.join(map(str,i))


# In[45]:

type(data)


# In[46]:

len(data)


# In[47]:

data[0]


# In[63]:

data =[[i, i**2, i**3] for i in range(10000)] 

f = open("C:/Users/admin/Desktop/homework/data_write_to_file.txt", "wb")
for i in data:
    f.write('\t'.join(map(str,i)) + '\n')
f.close()


# In[51]:

with open('C:/Users/admin/Desktop/homework/data_write_to_file.txt','r') as f:
    data = f.readlines()
data[:5]


# In[59]:

with open('C:/Users/admin/Desktop/homework/data_write_to_file.txt','r') as f:
    data = f.readlines(1000)
len(data)


# In[64]:

with open('C:/Users/admin/Desktop/homework/data_write_to_file.txt','r') as f:
    print f.readline()


# In[66]:

with open('C:/Users/admin/Desktop/homework/data_write_to_file.txt','r') as f:
    for k, i in enumerate(f):
        if k%2000 ==0:
            print i


# In[67]:

data = []
with open('C:/Users/admin/Desktop/homework/data_write_to_file.txt','r') as f:
    for line in f:
        line = line.replace('\n', '').split('\t')
        line = [int(i) for i in line]
        data.append(line)
data


# In[68]:

import json
data_dict = {'a':1, 'b':2, 'c':3}
with open('C:/Users/admin/Desktop/homework/save_dict.json', 'w') as f:
    json.dump(data_dict, f)


# In[69]:

dd = json.load(open("C:/Users/admin/Desktop/homework/save_dict.json"))
dd


# In[70]:

data_list = range(10)
with open('C:/Users/admin/Desktop/homework/save_list.json', 'w') as f:
    json.dump(data_list, f)


# In[71]:

dl = json.load(open("C:/Users/admin/Desktop/homework/save_list.json"))
dl


# In[72]:

import dill
def myFunction(num):
    return num,num

with open('C:/Users/admin/Desktop/homework/data.pkl', 'wb') as f:
    dill.dump(myFunction, f)


# In[73]:

with open('C:/Users/admin/Desktop/homework/data.pkl', 'r') as f:
    newFunction = dill.load(f)#, strictio=strictio))
newFunction('hello')


# In[ ]:




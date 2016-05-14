
# coding: utf-8

# # Homework1
# # 卢家希
# ## 学号：15210130070

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

x='Hello WorlD'
dir(x)[-10:]


# In[10]:

x.lower()


# In[11]:

x.upper()


# In[12]:

x=' Hello WorlD '


# In[13]:

x.lower()


# In[14]:

x.upper()


# In[15]:

x.rstrip()


# In[16]:

x.strip()


# In[17]:

x='hello world'
type(x)


# In[18]:

l = [1,2,3,3]
t = (1, 2, 3, 3) 
s = set([1,2,3,3]) 
d = {'a':1,'b':2,'c':3} 
a = np.array(l) 
print l, t, s, d, a


# In[19]:

l=[1,2,3,3]
l.append(4)
l


# In[20]:

d = {'a':1,'b':2,'c':3}
d.keys()


# In[21]:

d = {'a':1,'b':2,'c':3}
d.values()


# In[22]:

d = {'a':1,'b':2,'c':3}
d['b']


# In[23]:

d = {'a':1,'b':2,'c':3}
d.items()


# In[24]:

def devideplus(m,n):
    return float (m)/n+1


# In[25]:

devideplus(2,3)


# In[26]:

range(10)


# In[27]:

range(1,10)


# In[28]:

for i in range(10):
    print i,i*10, i**2


# In[29]:

for i in range (10):
    print i*10


# In[30]:

r=[devideplus(i,2) for i in range(10)]
r


# In[31]:

map(devideplus,[4,2],[2,1])


# In[32]:

j = 3
if j%2 == 1:
    print r'余数是1'
elif j%2 ==2:
    print r'余数是2'
else:
    print r'余数既不是1也不是2'


# In[34]:

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


# In[35]:

j = 0
while j <10:
    print j
    j+=1 


# In[36]:

j = 0
while j <10:
    if j%2 != 0: 
        print j**2
    j+=1


# In[37]:

j = 0
while j <50:
    if j == 30:
        break
    if j%2 != 0: 
        print j**2
    j+=1


# In[39]:

for i in [2, 0, 5]:
    try:
        print devideplus(4, i)
    except Exception, e:
        print e
        pass


# In[40]:

data =[[i, i**2, i**3] for i in range(10)] 
data


# In[41]:

for i in data:
    print '\t'.join(map(str, i))


# In[42]:

type(data)


# In[43]:

len(data)


# In[44]:

data[0]


# In[45]:

data =[[i, i**2, i**3] for i in range(10000)] 
f = open("/Users/lenovo/Desktop/homework/data_write_to_file.txt", "wb")
for i in data:
    f.write('\t'.join(map(str,i)) + '\n')
f.close()


# In[46]:

with open('/Users/lenovo/Desktop/homework/data_write_to_file.txt','r') as f:
    data = f.readlines()
data[:5]


# In[47]:

with open('/Users/lenovo/Desktop/homework/data_write_to_file.txt','r') as f:
    data = f.readlines(1000)
len(data)


# In[48]:

with open('/Users/lenovo/Desktop/homework/data_write_to_file.txt','r') as f:
    print f.readline()


# In[52]:

with open('/Users/lenovo/Desktop/homework/data_write_to_file.txt','r') as f:
    for k, i in enumerate(f):
        if k%2000 ==0:
            print i


# In[53]:

data = []
with open('/Users/lenovo/Desktop/homework/data_write_to_file.txt','r') as f:
    for line in f:
        line = line.replace('\n', '').split('\t')
        line = [int(i) for i in line]
        data.append(line)
data


# In[55]:

import json
data_dict = {'a':1, 'b':2, 'c':3}
with open('/Users/lenovo/Desktop/homework/save_dict.json', 'w') as f:
    json.dump(data_dict, f)


# In[56]:

dd = json.load(open("/Users/lenovo/Desktop/homework/save_dict.json"))
dd


# In[58]:

data_list = range(10)
with open('/Users/lenovo/Desktop/homework/save_dict.json', 'w') as f:
    json.dump(data_list, f)


# In[59]:

dl = json.load(open("/Users/lenovo/Desktop/homework/save_dict.json"))
dl


# In[60]:

import dill
# http://trac.mystic.cacr.caltech.edu/project/pathos/wiki/dill
def myFunction(num):
    return num,num

with open('/Users/lenovo/Desktop/homework/data.pkl', 'wb') as f:
    dill.dump(myFunction, f)


# In[61]:

with open('/Users/lenovo/Desktop/homework/data.pkl', 'r') as f:
    newFunction = dill.load(f)#, strictio=strictio))
newFunction('hello')


# In[64]:

get_ipython().magic(u'matplotlib inline')

import matplotlib.pyplot as plt
x = range(1, 100)
y = [i**-3 for i in x]
plt.plot(x, y, 'b-s')
plt.ylabel('$p(k)$', fontsize = 20)
plt.xlabel('$k$', fontsize = 20)
plt.xscale('log')
plt.yscale('log')
plt.title('Degree Distribution')
plt.show()


# In[ ]:




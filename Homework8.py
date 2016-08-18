
# coding: utf-8

# # 构建networkx的网络对象g（提示：有向网络），将www数据添加到g当中
# # 计算节点数量和连接数量

# In[29]:

get_ipython().magic(u'matplotlib inline')
import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt


# In[30]:

import networkx as nx

G = nx.DiGraph()
n = 0
with open ('C:/Users/admin/Desktop/homework8/data.txt') as f:
    for line in f:
        n += 1
        x, y = line.rstrip().split(' ')
        G.add_edge(x,y)


# In[31]:

nx.info(G)


# In[32]:

len(G)


# In[33]:

len(G.edges())


# # 计算www网络的网络密度

# In[12]:

nx.density(G)


# In[13]:

nodeNum = len(G.nodes())
edgeNum = len(G.edges())

2.0*edgeNum/(nodeNum * (nodeNum - 1))


# # 计算出度分布、入度分布

# In[35]:

from collections import defaultdict
import numpy as np

def plotDegreeDistribution(G):
    degs = defaultdict(int)
    for i in G.out_degree().values(): degs[i]+=1
    items = sorted ( degs.items () )
    x, y = np.array(items).T
    plt.plot(x, y, 'b-o')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(['Degree'])
    plt.xlabel('$K$', fontsize = 20)
    plt.ylabel('$P_K$', fontsize = 20)
    plt.title('$Degree\,Distribution$', fontsize = 20)
    plt.show() 
plotDegreeDistribution(G)


# In[36]:

def plotDegreeDistribution(G):
    degs = defaultdict(int)
    for i in G.in_degree().values(): degs[i]+=1
    items = sorted ( degs.items () )
    x, y = np.array(items).T
    plt.plot(x, y, 'b-o')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(['Degree'])
    plt.xlabel('$K$', fontsize = 20)
    plt.ylabel('$P_K$', fontsize = 20)
    plt.title('$Degree\,Distribution$', fontsize = 20)
    plt.show() 
plotDegreeDistribution(G)


# In[24]:

Ns = [i*10 for i in [1, 10, 100, 1000]]
ds = []
for N in Ns:
    print N
    BA= nx.random_graphs.barabasi_albert_graph(N,2)
    d = nx.average_shortest_path_length(BA)
    ds.append(d)


# In[21]:

plt.plot(Ns, ds, 'r-o')
plt.xlabel('$N$', fontsize = 20)
plt.ylabel('$<d>$', fontsize = 20)
plt.xscale('log')
plt.show()


# In[ ]:





# coding: utf-8

# In[9]:

import graphlab
graphlab.canvas.set_target("ipynb")
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[10]:

data = graphlab.SFrame.read_csv('C:/Users/admin/Desktop/homework7/ml-1m/ratings.dat', delimiter='\n', 
                                header=False)['X1'].apply(lambda x: x.split('::')).unpack()
for col in data.column_names():
    data[col] = data[col].astype(int)
data.rename({'X.0': 'user_id', 'X.1': 'movie_id', 'X.2': 'rating', 'X.3': 'timestamp'})
data.save('ratings')

users = graphlab.SFrame.read_csv('C:/Users/admin/Desktop/homework7/ml-1m/users.dat', delimiter='\n', 
                                 header=False)['X1'].apply(lambda x: x.split('::')).unpack()
users.rename({'X.0': 'user_id', 'X.1': 'gender', 'X.2': 'age', 'X.3': 'occupation', 'X.4': 'zip-code'})
users['user_id'] = users['user_id'].astype(int)
users.save('users')

items = graphlab.SFrame.read_csv('C:/Users/admin/Desktop/homework7/ml-1m/movies.dat', delimiter='\n', 
                                 header=False)['X1'].apply(lambda x: x.split('::')).unpack()
items.rename({'X.0': 'movie_id', 'X.1': 'title', 'X.2': 'genre'})
items['movie_id'] = items['movie_id'].astype(int)
items.save('items')


# In[11]:

data.show()


# In[12]:

items.head()


# In[13]:

data = data.join(items, on='movie_id')


# In[14]:

data


# In[15]:

(train_set, test_set) = data.random_split(0.95, seed=1)


# In[16]:

m = graphlab.recommender.create(train_set, 'user_id', 'movie_id', 'rating')


# In[17]:

m


# In[18]:

m2 = graphlab.item_similarity_recommender.create(train_set, 'user_id', 'movie_id', 'rating',
                                 similarity_type='pearson')


# In[19]:

m2


# In[20]:

result = graphlab.recommender.util.compare_models(test_set, [m, m2],
                                            user_sample=.1, skip_set=train_set)


# In[22]:

m.get_similar_items([1287])  


# In[23]:

m.get_similar_items([1287]).join(items, on={'similar': 'movie_id'}).sort('rank')


# In[25]:

recs = m.recommend()


# In[26]:

recs


# In[27]:

data[data['user_id'] == 4].join(items, on='movie_id')


# In[28]:

m.recommend(users=[4], k=20).join(items, on='movie_id')


# In[29]:

get_ipython().magic(u'pinfo m.recommend')


# In[30]:

recent_data = graphlab.SFrame()
recent_data['movie_id'] = [1291] 
recent_data['user_id'] = 99999


# In[31]:

m2.recommend(users=[99999], new_observation_data=recent_data).join(items, on='movie_id').sort('rank')


# In[32]:

m.save('my_model')


# In[33]:

m_again = graphlab.load_model('my_model')


# In[34]:

m_again


# In[ ]:




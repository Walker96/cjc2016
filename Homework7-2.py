
# coding: utf-8

# In[1]:

import graphlab as gl
gl.canvas.set_target('ipynb')
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[3]:

train_file = 'C:/Users/admin/Desktop/homework7/10000.txt'
sf = gl.SFrame.read_csv(train_file, header=False, delimiter='\t', verbose=False)
sf.rename({'X1':'user_id', 'X2':'music_id', 'X3':'rating'}).show()


# In[4]:

(train_set, test_set) = sf.random_split(0.8, seed=1)


# In[5]:

popularity_model = gl.popularity_recommender.create(train_set, 'user_id', 'music_id', target = 'rating')


# In[6]:

item_sim_model = gl.item_similarity_recommender.create(train_set, 'user_id', 'music_id', target = 'rating', 
                                                       similarity_type='cosine')


# In[7]:

factorization_machine_model = gl.recommender.factorization_recommender.create(train_set, 'user_id', 'music_id',
                                                                              target='rating')


# In[8]:

result = gl.recommender.util.compare_models(test_set, [popularity_model, item_sim_model, factorization_machine_model],
                                            user_sample=.1, skip_set=train_set)


# In[9]:

K = 10
users = gl.SArray(sf['user_id'].unique().head(100))


# In[10]:

recs = item_sim_model.recommend(users=users, k=K)
recs.head()


# In[ ]:




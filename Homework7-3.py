
# coding: utf-8

# In[1]:

import graphlab
graphlab.canvas.set_target("ipynb")
rating_sf = graphlab.SFrame('ratings')
users = graphlab.SFrame('users')
items = graphlab.SFrame('items')


# In[2]:

rating_sf.show()


# In[3]:

dir(graphlab.recommender)


# In[4]:

(train, test) = graphlab.recommender.util.random_split_by_user(rating_sf, 'user_id', 'movie_id')


# In[5]:

from graphlab import item_similarity_recommender
itemcf = item_similarity_recommender.create(train[train['rating'] > 4], 'user_id', 'movie_id')


# In[6]:

pop    = graphlab.popularity_recommender.create(train[train['rating'] > 4], 'user_id', 'movie_id')


# In[7]:

m = graphlab.recommender.create(train, 'user_id', 'movie_id', 'rating')


# In[8]:

m


# In[9]:

m['coefficients']


# In[10]:

graphlab.recommender.util.compare_models(test[test['rating'] > 4], 
                                    [pop, itemcf, m], 
                                    user_sample=0.2, 
                                    metric='precision_recall')


# In[11]:

m_rank = graphlab.recommender.ranking_factorization_recommender.create(train, 'user_id', 'movie_id', 'rating', 
                                     unobserved_rating_value=3)


# In[12]:

results = graphlab.recommender.util.compare_models(test[test['rating'] > 4], 
                                              [pop, itemcf, m, m_rank], 
                                              user_sample=0.2, 
                                              metric='precision_recall')


# In[13]:

results[3]['precision_recall_overall']


# In[14]:

user_sf = graphlab.SFrame('users')
item_sf = graphlab.SFrame('items')


# In[15]:

m_user = graphlab.recommender.create(train, 'user_id', 'movie_id', 'rating', 
                                     user_data=user_sf)
m_item = graphlab.recommender.create(train, 'user_id', 'movie_id', 'rating', 
                                     item_data=item_sf)
m_both = graphlab.recommender.create(train, 'user_id', 'movie_id', 'rating', 
                                     user_data=user_sf, item_data=item_sf)


# In[18]:

m_both


# In[19]:

results = graphlab.recommender.util.compare_models(test, [m, m_user, m_item, m_both], user_sample=0.2)


# In[20]:

[results[i]['rmse_overall'] for i in range(len(results))]


# In[21]:

results[0]['rmse_by_item'].show()


# In[22]:

graphlab.recommender.util.compare_models(test[test['rating'] > 4], 
                                    [m_rank, m_both], 
                                    user_sample=0.2, 
                                    metric='precision_recall')


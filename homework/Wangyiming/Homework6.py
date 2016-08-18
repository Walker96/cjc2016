
# coding: utf-8

# # Topic Modeling Using Graphlab

# In[1]:

import graphlab
graphlab.product_key.set_product_key('4972-65DF-8E02-816C-AB15-021C-EC1B-0367')


# In[2]:

import graphlab
graphlab.canvas.set_target("ipynb")


# In[4]:

sf = graphlab.SFrame.read_csv("C:/Users/admin/Desktop/homework6/w15.txt", header=False)


# In[5]:

sf


# In[6]:

dir(sf['X1'])


# In[7]:

bow = sf['X1']._count_words()


# In[8]:

type(sf['X1'])


# In[9]:

type(bow)


# In[10]:

bow.dict_has_any_keys(['limited'])


# In[11]:

bow.dict_values()[0][:20]


# In[12]:

sf['bow'] = bow


# In[13]:

type(sf['bow'])


# In[14]:

len(sf['bow'])


# In[15]:

sf['bow'][0].items()[:5]


# In[16]:

sf['tfidf'] = graphlab.text_analytics.tf_idf(sf['X1'])


# In[17]:

sf['tfidf'][0].items()[:5]


# In[18]:

sf.show()


# In[19]:

sf


# In[20]:

docs = sf['bow'].dict_trim_by_values(2)


# In[21]:

docs = docs.dict_trim_by_keys(graphlab.text_analytics.stopwords(), exclude=True)


# In[22]:

m = graphlab.topic_model.create(docs)


# In[23]:

m


# In[24]:

m.get_topics()


# In[25]:

topics = m.get_topics().unstack(['word','score'], new_column_name='topic_words')['topic_words'].apply(lambda x: x.keys())
for topic in topics:
    print topic


# In[26]:

pred = m.predict(docs)


# In[27]:

pred.show()


# In[28]:

pred = m.predict(docs, output_type='probabilities')


# In[29]:

m['vocabulary']


# In[30]:

m['topics']


# In[34]:

def print_topics(m):
    topics = m.get_topics(num_words=5)
    topics = topics.unstack(['word','score'], new_column_name='topic_words')['topic_words']
    topics = topics.apply(lambda x: x.keys())
    for topic in topics:
        print topic
print_topics(m)


# In[42]:

m2 = graphlab.topic_model.create(docs,
                                 num_topics=10,
                                 initial_topics=m['topics'])


# In[36]:

associations = graphlab.SFrame()
associations['word'] = ['recognition']
associations['topic'] = [0]


# In[37]:

m2 = graphlab.topic_model.create(docs,
                                 num_topics=20,
                                 num_iterations=50,
                                 associations=associations, 
                                 verbose=False)


# In[ ]:

m2.get_topics(num_words=10)


# In[ ]:

print_topics(m2)


# In[ ]:




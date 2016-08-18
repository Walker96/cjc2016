
# coding: utf-8

# # sentiment_classifier

# In[1]:

import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


# In[4]:

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_tweet(tweet):
    return         classifier.classify(extract_features(nltk.word_tokenize(tweet)))


# In[6]:

pos_tweets = read_tweets('C:/Users/admin/Desktop/homework5/Twitter-Sentimental-Analysis-master/happy.txt', 'positive')
neg_tweets = read_tweets('C:/Users/admin/Desktop/homework5/Twitter-Sentimental-Analysis-master/sad.txt', 'negative')


# In[7]:

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


# In[8]:

word_features = get_word_features(                    get_words_in_tweets(tweets))


# In[9]:

training_set = nltk.classify.util.apply_features(extract_features, tweets)
classifier = NaiveBayesClassifier.train(training_set)


# In[10]:

test_tweets = read_tweets('C:/Users/admin/Desktop/homework5/Twitter-Sentimental-Analysis-master/happy_test.txt', 'positive')
test_tweets.extend(read_tweets('C:/Users/admin/Desktop/homework5/Twitter-Sentimental-Analysis-master/sad_test.txt', 'negative'))
total = accuracy = float(len(test_tweets))


# In[11]:

for tweet in test_tweets:
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1


# In[12]:

print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Alla Topp
# Connecting to PSQL and running quesriws to do muli-processing


# In[1]:


get_ipython().system('pip install psycopg2')


# In[2]:


get_ipython().system('pip install pygresql')


# In[5]:


import psycopg2
import pandas as pd
import sqlalchemy
import matplotlib as plt


# In[6]:


conn = psycopg2.connect(host = "192.168.200.194", port = "5432", user = "postgres", database = "yelpdb")
cur = conn.cursor()


# In[8]:


get_ipython().run_cell_magic('time', '', '\n#Count number of rows in largest table\ncur.execute("""SELECT COUNT(*) FROM review;""")\nquery_results = cur.fetchall()\nprint(query_results)')


# In[9]:


get_ipython().run_cell_magic('time', '', '\n#Select all distinc names in the user table\ncur.execute("""SELECT DISTINCT(user_name) FROM y_user;""")\nquery_results = cur.fetchall()\nprint(query_results)')


# In[10]:


get_ipython().run_cell_magic('time', '', '\n#Count occurrence of each name in the user tabel\ncur.execute("""SELECT user_name, COUNT(*) FROM y_user GROUP BY user_name;""")\nquery_results = cur.fetchall()\nprint(query_results)')


# In[11]:


get_ipython().run_cell_magic('time', '', '\n#Count number of reviews by each user\ncur.execute("""SELECT y_user.user_name, COUNT(review.text) AS Number FROM y_user INNER JOIN review\n            ON y_user.user_id = review.user_id GROUP BY y_user.user_name LIMIT 100""")\nquery_results = cur.fetchall()\nprint(query_results)')


# In[ ]:


#Multiple joins including all the tables ?


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


pets = pd.DataFrame({'sex': np.array(['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M']),
                   'age': np.array([21, 45, 23, 56, 47, 70, 34, 30, 19, 62]),
                   'pets': np.array([['cat', 'dog'],
                                    ['hamster'],
                                    ['cat', 'gerbil'],
                                    ['fish', 'hamster', 'gerbil'],
                                    ['cat'],
                                    ['dog'],
                                    ['dog'],
                                    ['cat'],
                                    ['rabbit', 'cat'],
                                    ['dog']])})


# ### We have been asked to analyse the survey responses. In particular, we have been given the questions
# ### What sex was the youngest respondent?
# ### What age was the person with the most pets?
# ### What was the most popular pet?
# ### What was the average age of dog owners?

# In[46]:


pets


# ### What sex was the youngest respondent?

# In[10]:


pets.iloc[pets["age"].idxmin(),0]


# ### <span style="color:blue"> *Note: Pls check if there is any shorter way of doing this in one single line using true boolean* text</span>

# ### What age was the person with the most pets?

# In[17]:


pets['num_pets']=pets.pets.map(len)
pets


# In[18]:


del pets['Length']
pets


# ### What age was the person with the most pets?

# In[19]:


pets.iloc[pets["num_pets"].idxmax(),1]


# In[20]:


pets.loc[pets['num_pets'] == max(pets['num_pets']), 'age']


# ### What was the most popular pet?

# In[21]:


pet_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)
pet_series


# In[28]:


pet_series.value_counts()


# In[27]:


pet_series.value_counts()


# ### What was the average age of dog owners?

# In[30]:


pets['dog_owner'] = pets['pets'].apply(lambda x: True if 'dog' in x else False)
pets


# In[43]:


pets_new=pets.loc[pets['dog_owner'] == True]


# In[44]:


pets_new['age'].mean()


# In[ ]:





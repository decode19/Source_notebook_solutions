#!/usr/bin/env python
# coding: utf-8

# # Springboard Apps project - Tier 3 - Sourcing and Loading
# 
# Welcome to the final project of this Springboard prep course!! To give you a taste of your future career, we're going to walk through exactly the kind of notebook that you'd write as a data scientist. In the process, we'll be sure to signpost the general framework for our investigation - the Data Science Pipeline - as well as give reasons for why we're doing what we're doing.
# 
# **Brief**
# 
# Did Apple Store apps receive better reviews than Google Play apps?
# 
# ## Stages of the project
# 
# 1. Sourcing and loading 
#     * Load the two datasets
#     * Pick the columns that we are going to work with 
#     * Subsetting the data on this basis 
#  
#  
# 2. Cleaning, transforming and visualizing
#     * Check the data types and fix them
#     * Add a `platform` column to both the `Apple` and the `Google` dataframes
#     * Changing the column names to prepare for a join 
#     * Join the two data sets
#     * Eliminate the `NaN` values
#     * Filter only those apps that have been reviewed at least once
#     * Summarize the data visually and analytically (by the column `platform`)  
#   
#   
# 3. Modelling 
#     * Hypothesis formulation
#     * Getting the distribution of the data
#     * Permutation test 
# 
# 
# 4. Evaluating and concluding 
#     * What is our conclusion?
#     * What is our decision?
#     * Other models we could have used. 
#     

# ## Importing the libraries
# 
# In this case we are going to import pandas, numpy, scipy, random and matplotlib.pyplot

# In[ ]:


import _ _ _ as pd
import _ _ _ as np
import _ _ _ as plt
# scipi is a library for statistical tests and visualizations 
from scipy import stats
# random enables us to generate random numbers
import random


# ## Stage 1 -  Sourcing and loading data

# ### 1a. Source and load the data
# Let's download the data from Kaggle. Kaggle is a fantastic resource: a kind of social medium for data scientists, it boasts projects, datasets and news on the freshest libraries and technologies all in one place. The data from the Apple Store can be found [here](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) and the data from Google Store can be found [here](https://www.kaggle.com/lava18/google-play-store-apps).
# Download the datasets and save them in your working directory.

# In[5]:


# Now that the files are saved, we want to load them into Python using read_csv and pandas.

# Create a variable called google, and store in it the path of the csv file that contains your google dataset. 
# If your dataset is in the same folder as this notebook, the path will simply be the name of the file. 

# Read the csv file into a data frame called Google using the read_csv() pandas method.

# Using the head() pandas method, observe the first three entries.

import os
import pandas as pd

google =pd.read_csv('/Users/Shweta/Documents/googleplaystore.csv')


google.head(3)


# In[10]:


# Create a variable called apple, and store in it the path of the csv file that contains your apple dataset. 


# Read the csv file into a pandas DataFrame object called Apple.
apple=pd.read_csv('/Users/Shweta/Documents/applestoreuserreview.csv')

# Observe the first three entries like you did with your other data. 
apple.head(3)


# ### 1b. Pick the columns we'll work with
# 
# From the documentation of these datasets, we can infer that the most appropriate columns to answer the brief are:
# 
# 1. Google:
#     * `Category` # Do we need this?
#     * `Rating`
#     * `Reviews`
#     * `Price` (maybe)
# 2. Apple:    
#     * `prime_genre` # Do we need this?
#     * `user_rating` 
#     * `rating_count_tot`
#     * `price` (maybe)

# ### 1c. Subsetting accordingly
# 
# Let's select only those columns that we want to work with from both datasets. We'll overwrite the subsets in the original variables.

# In[13]:


# Subset our DataFrame object Google by selecting just the variables ['Category', 'Rating', 'Reviews', 'Price']
googlesubset=google[['Category', 'Rating', 'Reviews', 'Price']]

# Check the first three entries
googlesubset.head(3)


# In[14]:


# Do the same with our Apple object, selecting just the variables ['prime_genre', 'user_rating', 'rating_count_tot', 'price']
applesubset=apple[['prime_genre', 'user_rating', 'rating_count_tot', 'price']]

# Let's check the first three entries
applesubset.head(3)


# In[ ]:





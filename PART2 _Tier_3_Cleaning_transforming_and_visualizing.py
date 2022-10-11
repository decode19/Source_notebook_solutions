#!/usr/bin/env python
# coding: utf-8

# # Springboard Apps project - Tier 3 - Cleaning, transforming and visualizing
# 
# Welcome to the final project of this Springboard prep course! To give you a taste of your future career, we're going to walk through exactly the kind of notebook that you'd write as a data scientist. In the process, we'll be sure to signpost the general framework for our investigation - the Data Science Pipeline - as well as give reasons for why we're doing what we're doing.
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

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# scipi is a library for statistical tests and visualizations 
from scipy import stats
# random enables us to generate random numbers
import random


# ## Stage 1 -  Sourcing and loading data

# ### 1a. Source and load the data
# Let's download the data from Kaggle. Kaggle is a fantastic resource: a kind of social medium for data scientists, it boasts projects, datasets and news on the freshest libraries and technologies all in one place. The data from the Apple Store can be found [here](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) and the data from Google Store can be found [here](https://www.kaggle.com/lava18/google-play-store-apps).
# Download the datasets and save them in your working directory.

# In[4]:


# Now that the files are saved, we want to load them into Python using read_csv and pandas.

# Create a variable called google, and store in it the path of the csv file that contains your google dataset. 
# If your dataset is in the same folder as this notebook, the path will simply be the name of the file. 
# Read the csv file into a data frame called Google using the read_csv() pandas method.
# Using the head() pandas method, observe the first three entries.
google =pd.read_csv('/Users/Shweta/Documents/googleplaystore.csv')
google.head(3)


# In[5]:


# Create a variable called apple, and store in it the path of the csv file that contains your apple dataset. 
# Read the csv file into a pandas DataFrame object called Apple.
apple=pd.read_csv('/Users/Shweta/Documents/applestoreuserreview.csv')
apple.head(3)
# Observe the first three entries like you did with your other data. 


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

# In[6]:


# Subset our DataFrame object Google by selecting just the variables ['Category', 'Rating', 'Reviews', 'Price']
googlesubset=google[['Category', 'Rating', 'Reviews', 'Price']]

# Check the first three entries
googlesubset.head(3)


# In[7]:


# Do the same with our Apple object, selecting just the variables ['prime_genre', 'user_rating', 'rating_count_tot', 'price']
applesubset=apple[['prime_genre', 'user_rating', 'rating_count_tot', 'price']]

# Let's check the first three entries
applesubset.head(3)


# ## Stage 2 -  Cleaning, transforming and visualizing

# ### 2a. Check the data types for both Apple and Google, and fix them
# 
# Types are crucial for data science in Python. Let's determine whether the variables we selected in the previous section belong to the types they should do, or whether there are any errors here. 

# In[8]:


# Using the dtypes feature of pandas DataFrame objects, check out the data types within our Apple dataframe.
# Are they what you expect?
applesubset.dtypes


# This is looking healthy. But what about our Google data frame?

# In[9]:


# Using the same dtypes feature, check out the data types of our Google dataframe. 
googlesubset.dtypes


# Weird. The data type for the column 'Price' is 'object', not a numeric data type like a float or an integer. Let's investigate the unique values of this column. 

# In[14]:


# Use the unique() pandas method on the Price column to check its unique values. 
googlesubset.Price.unique()


# Aha! Fascinating. There are actually two issues here. 
# 
# - Firstly, there's a price called `Everyone`. That is a massive mistake! 
# - Secondly, there are dollar symbols everywhere! 
# 
# 
# Let's address the first issue first. Let's check the datapoints that have the price value `Everyone`

# In[15]:


# Let's check which data points have the value 'Everyone' for the 'Price' column by subsetting our Google dataframe.

# Subset the Google dataframe on the price column. 
# To be sure: you want to pick out just those rows whose value for the 'Price' column is just 'Everyone'. 
googlesubset[googlesubset['Price']=='Everyone']


# Thankfully, it's just one row. We've gotta get rid of it. 

# In[16]:


# Let's eliminate that row. 

# Subset our Google dataframe to pick out just those rows whose value for the 'Price' column is NOT 'Everyone'. 
# Reassign that subset to the Google variable. 
# You can do this in two lines or one. Your choice! 
Google=googlesubset[googlesubset['Price']!= 'Everyone']

# Check again the unique values of Google
Google.Price.unique()


# Our second problem remains: I'm seeing dollar symbols when I close my eyes! (And not in a good way). 
# 
# This is a problem because Python actually considers these values strings. So we can't do mathematical and statistical operations on them until we've made them into numbers. 

# In[23]:


# Let's create a variable called nosymb.
# This variable will take the Price column of Google and apply the str.replace() method. 
# Remember: we want to find '$' and replace it with nothing, so we'll have to write approrpiate arguments to the method to achieve this. 
nosymb = Google['Price'].str.replace('$','0')

# Now we need to do two things:
# i. Make the values in the nosymb variable numeric using the to_numeric() pandas method.
# ii. Assign this new set of numeric, dollar-sign-less values to Google['Price']. 
# You can do this in one line if you wish.
Google['Price']=pd.to_numeric(nosymb)


# Now let's check the data types for our Google dataframe again, to verify that the 'Price' column really is numeric now.

# In[24]:


# Use the function dtypes. 
Google.dtypes


# Notice that the column `Reviews` is still an object column. We actually need this column to be a numeric column, too. 

# In[26]:


# Convert the 'Reviews' column to a numeric data type. 
# Use the method pd.to_numeric(), and save the result in the same column.
Google['Reviews']=pd.to_numeric(Google['Reviews'])


# In[27]:


# Let's check the data types of Google again
Google.dtypes


# ### 2b. Add a `platform` column to both the `Apple` and the `Google` dataframes
# Let's add a new column to both dataframe objects called `platform`: all of its values in the Google dataframe will be just 'google', and all of its values for the Apple dataframe will be just 'apple'. 
# 
# The reason we're making this column is so that we can ultimately join our Apple and Google data together, and actually test out some hypotheses to solve the problem in our brief. 

# In[37]:


# Create a column called 'platform' in both the Apple and Google dataframes. 
# Add the value 'apple' and the value 'google' as appropriate. 
applesubset['platform'] = 'apple'
Google['platform'] = 'Google'


# ### 2c. Changing the column names to prepare for our join of the two datasets 
# Since the easiest way to join two datasets is if they have both:
# - the same number of columns
# - the same column names
# we need to rename the columns of `Apple` so that they're the same as the ones of `Google`, or vice versa.
# 
# In this case, we're going to change the `Apple` columns names to the names of the `Google` columns. 
# 
# This is an important step to unify the two datasets!

# In[41]:


# Create a variable called old_names where you'll store the column names of the Apple dataframe. 
# Use the feature .columns.
old_names = applesubset.columns

# Create a variable called new_names where you'll store the column names of the Google dataframe. 
new_names = Google.columns

# Use the rename() DataFrame method to change the columns names. 
# In the columns parameter of the rename() method, use this construction: dict(zip(old_names,new_names)).
applesubset.rename(columns={i:j for i,j in zip(old_names,new_names)}, inplace=True)
applesubset.head()


# ### 2d. Join the two datasets 
# Let's combine the two datasets into a single data frame called `df`.

# In[42]:


# Let's use the append() method to append Apple to Google. 
# Make Apple the first parameter of append(), and make the second parameter just: ignore_index = True.
df = Google.append(applesubset, ignore_index= True)

# Using the sample() method with the number 12 passed to it, check 12 random points of your dataset.
df.sample(12)


# ### 2e. Eliminate the NaN values
# 
# As you can see there are some `NaN` values. We want to eliminate all these `NaN` values from the table.

# In[48]:


# Lets check first the dimesions of df before droping `NaN` values. Use the .shape feature. 
df.shape

# Use the dropna() method to eliminate all the NaN values, and overwrite the same dataframe with the result. 
# Note: dropna() by default removes all rows containing at least one NaN. 
df.dropna(inplace=True)

# Check the new dimesions of our dataframe.
df.shape


# ### 2f. Filter the data so that we only see whose apps that have been reviewed at least once
# 
# Apps that haven't been reviewed yet can't help us solve our brief. 
# 
# So let's check to see if any apps have no reviews at all. 

# In[50]:


# Subset your df to pick out just those rows whose value for 'Reviews' is equal to 0. 
# Do a count() on the result. 
df[df['Reviews'] == 0].count()


# 929 apps do not have reviews, we need to eliminate these points!

# In[58]:


# Eliminate the points that have 0 reviews.
# An elegant way to do this is to assign df the result of picking out just those rows in df whose value for 'Reviews' is NOT 0.
df[df['Reviews']!= 0]
df.shape


# ### 2g. Summarize the data visually and analytically (by the column `platform`)

# What we need to solve our brief is a summary of the `Rating` column, but separated by the different platforms.

# In[71]:


# To summarize analytically, let's use the groupby() method on our df.
# For its parameters, let's assign its 'by' parameter 'platform', and then make sure we're seeing 'Rating' too. 
# Finally, call describe() on the result. We can do this in one line, but this isn't necessary. 
df1=df.groupby(['platform','Rating'])


# Interesting! Our means of 4.049697 and 4.191757 don't **seem** all that different! Perhaps we've solved our brief already: there's no significant difference between Google Play app reviews and Apple Store app reviews. We have an ***observed difference*** here: which is simply (4.191757 - 4.049697) = 0.14206. This is just the actual difference that we observed between the mean rating for apps from Google Play, and the mean rating for apps from the Apple Store. Let's look at how we're going to use this observed difference to solve our problem using a statistical test. 
# 
# **Outline of our method:**
# 1. We'll assume that platform (i.e, whether the app was Google or Apple) really doesn’t impact on ratings. 
# 
# 
# 2. Given this assumption, we should actually be able to get a difference in mean rating for Apple apps and mean rating for Google apps that's pretty similar to the one we actually got (0.14206) just by: 
# a. shuffling the ratings column, 
# b. keeping the platform column the same,
# c. calculating the difference between the mean rating for Apple and the mean rating for Google. 
# 
# 
# 3. We can make the shuffle more useful by doing it many times, each time calculating the mean rating for Apple apps and the mean rating for Google apps, and the difference between these means. 
# 
# 
# 4. We can then take the mean of all these differences, and this will be called our permutation difference. This permutation difference will be great indicator of what the difference would be if our initial assumption were true and platform really doesn’t impact on ratings. 
# 
# 
# 5. Now we do a comparison. If the observed difference looks just like the permutation difference, then we stick with the claim that actually, platform doesn’t impact on ratings. If instead, however, the permutation difference differs significantly from the observed difference, we'll conclude: something's going on; the platform does in fact impact on ratings. 
# 
# 
# 6. As for what the definition of *significantly* is, we'll get to that. But there’s a brief summary of what we're going to do. Exciting!
# 
# If you want to look more deeply at the statistics behind this project, check out [this resource](https://www.springboard.com/archeio/download/4ea4d453b0b84014bcef287c50f47f00/).

# Let's also get a **visual summary** of the `Rating` column, separated by the different platforms. 
# 
# A good tool to use here is the boxplot!

# In[ ]:


# Call the boxplot() method on our df.
# Set the parameters: by = 'platform' and column = ['Rating'].
df._ _ _(by=_ _ _, column =_ _ _, grid=False, rot=45, fontsize=15)


# Here we see the same information as in the analytical summary, but with a boxplot. Can you see how the boxplot is working here? If you need to revise your boxplots, check out this this [link](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps). 

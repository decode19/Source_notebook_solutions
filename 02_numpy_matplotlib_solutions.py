#!/usr/bin/env python
# coding: utf-8

# # Introduction to numpy and matplotlib
# You should already be familiar with the standard python types such as lists and dictionaries.
# In this notebook we will demonstrate how numpy provides arrays (matrices) and convenient ways to perform operations on them.

# Recall the equation for a straight line $y = mx+c$, where $m$ denotes the slope and $c$ the intercept. Note, as you come to encounter linear regression, where $m$ and $c$ are unknown parameters to be determined from data, you will see $m$ typically replaced with $\beta_1$ and $c$ with $\beta_0$, where $\beta_i$ denotes a parameter to be determined. Thus the straight line formula will be written $y = \beta_1x + \beta_0$ or $y = \beta_0 + \beta_1x$. These two forms, of course, being mathematically equivalent.

# The basic task we set ourselves here is to take an input sequence of numbers (multiple $x$ values) and create an output sequence (multiple $y$ values). We'll take the desired slope of the line to be 5 and the intercept -1.

# In[7]:


m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]


# Here we hold our multiple $x$ values in a python list.

# In[8]:


y = [(item * m) + c for item in x]


# In[9]:


print(y)


# Although list comprehensions are very "pythonic", they are more cumbersome than we'd like for performing lots of numeric, or matrix, operations.

# ## numpy
# Let's now perform the above using numpy.

# In[12]:


import numpy as np


# In[13]:


X = np.array(x)
Y = m*X + c


# In[14]:


print(Y)


# Notice how we can now write the code in a much more mathematical way.

# ## matplotlib
# Now we have our matching input and output values, X and Y, wouldn't it be nice to see them in a graph. Although the plot function is very useful for sequences, in our case here we have a sequence of points that all lie on a straight line. This means it will be impossible in a plain line plot to tell whether there is one straight line between two endpoints, or a series of points. It can be more informative to show the individual points, and so here we will use a scatter plot rather than a line plot.

# In[16]:


import matplotlib.pyplot as plt


# In[17]:


plt.scatter(X,Y)
plt.show()


# # Conclusion
# Great! In these few simple examples, you've already come a long way. You're using a notebook to develop a sequence of data manipulations, which can include descriptive, formatted text. Although we won't be using numpy directly in this short course, we've seen how it provides data types and operations that allow us to succinctly perform data operations. This kind of convenience and succinctness is what makes python and its ecosystem a great choice for data science. Pandas, which we'll come to shortly, is built on top of numpy. We've also seen how we can add visualizations of our data to our notebook.

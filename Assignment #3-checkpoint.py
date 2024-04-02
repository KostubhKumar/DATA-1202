#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine
import pymysql


# In[3]:


engine = create_engine('mysql+pymysql://<Username>:<Password>@localhost/data1202')


# In[4]:


con_1 = engine.connect()


# In[10]:


#Create a new column that labels records before 2005 as 'pre-2005' and after 2005 as 'post-2005'
labels = pd.read_sql ('''SELECT Platform, Year_of_Release, Publisher, Global_Sales, 
    CASE
        WHEN Year_of_Release <= 2005 THEN 'pre-2005'
        ELSE 'post-2005'
    END AS period
FROM data1202.`vgsales-2016`;''', con_1)
print(labels)


# In[11]:


# Was the average of global sales higher before or after 2005 ?
avg_2005 = pd.read_sql ('''SELECT 
    CASE
        WHEN Year_of_Release <= 2005 THEN 'pre-2005'
        ELSE 'post-2005'
    END AS period, avg(Global_Sales) as 'Global_Sales'
FROM data1202.`vgsales-2016`
group by period;''', con_1)
print(avg_2005)


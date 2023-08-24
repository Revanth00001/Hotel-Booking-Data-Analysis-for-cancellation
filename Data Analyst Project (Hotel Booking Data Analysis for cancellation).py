#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importing all the necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[7]:


df = pd.read_csv('hotel_bookings.csv')


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.shape


# In[7]:


df.columns


# In[11]:


df.info()


# In[32]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[10]:


df.info()


# In[12]:


df.describe(include = 'object')


# In[13]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[14]:


df.isnull().sum()


# In[15]:


df.drop(['company','agent'],axis = 1,inplace = True)
df.dropna(inplace = True)


# In[16]:


df.isnull().sum()


# In[17]:


#summary statistics of numerical columns
df.describe()


# In[18]:


#this step is used to plot adr column as box plot to find the irregularities and remove outliers in the column


df['adr'].plot(kind = 'box')


# In[19]:


#found the outlier and removed removed one.
df = df[df['adr']<5000]


# In[20]:


#Data analysis and Visualization.


#this is about knowing how many people cancelled the hotels and how many have not in percentage!
cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print('cancelled_perc')

#plotting the reservation status

plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor = 'k', width = 0.7)
plt.show()


# In[21]:


# cancelation rate depending on the hotels using count plot

plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'hotel',hue = 'is_canceled',data = df,palette = 'Blues')
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(handles=legend_labels, bbox_to_anchor=(1, 1))
plt.title('Reservation status in different hotels',size = 20)
plt.xlabel('hotel')
plt.ylabel('Number of reservations')


# In[22]:


#find the percentage of cancellation in resort and city hotels

resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[23]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[24]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[41]:


plt.figure(figsize = (20,8))
plt.title("Average Daily Rate in City and resort Hotel(Price) ",fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label = 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[33]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month',hue = 'is_canceled',data = df,palette = "bright")
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(handles=legend_labels, bbox_to_anchor=(1, 1))
plt.title('Reservation status per month ',size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[35]:


plt.figure(figsize = (15,8))
plt.title('ADR Per Month',fontsize = 30)
sns.barplot('month','adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[36]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservations cancelled')
plt.pie(top_10_country,autopct = '%.2f',labels = top_10_country.index)
plt.show()


# In[38]:


df['market_segment'].value_counts()


# In[39]:


df['market_segment'].value_counts(normalize=True)

#Here our hypothesis is failed as only 20% of population is of offline as we expected offline to be the most.
# this step is for where the bookings of the hotels are happening.


# In[40]:


#this step is for the us to know that the majority of the people cancelling the hotels by what means.
cancelled_data['market_segment'].value_counts(normalize=True)


# In[ ]:





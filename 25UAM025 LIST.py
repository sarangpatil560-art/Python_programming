#!/usr/bin/env python
# coding: utf-8

# list

# In[2]:


fruits =["apple","mango","banana"]
print (fruits)


# In[3]:


print(fruits[1])


# In[4]:


print (fruits[1:3])


# In[5]:


print(len(fruits))


# In[6]:


fruits[1]="orange"
print(fruits)


# In[10]:


fruits =["apple","mango","banana"]
fruits.append("papaya")
print(fruits)


# In[11]:


print(type(fruits))


# In[17]:


fruits =["apple","mango","banana"]
fruits.remove("mango")
print(fruits)


# In[19]:


fruits.sort()
print(fruits)


# In[21]:


fruits.sort(reverse=True)
print(fruits)


# In[25]:


fruits =["apple","mango","banana"]
fruits.extend(["chery","orange"])
print(fruits)


# In[26]:


fruits.insert(1,"chery")
print(fruits)


# In[ ]:





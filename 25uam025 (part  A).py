#!/usr/bin/env python
# coding: utf-8

# In[13]:


empty_dict= {}
print("Empty dictionary:",empty_dict)
print("type of empty_dict:", type(empty_dict))

empty_dict2=dict()
print("Empty dictionary using dict():", 
empty_dict2)


# In[5]:





# In[14]:



empty_set = set()
print("Empty set:", empty_set)
print("Type of empty_set:", type(empty_set))


# In[7]:


fruits = {"apple", "banana", "cherry"}
print("Set of fruits:", fruits) 
mixed_set = {1, "A", 3.14, True}
print("Mixed set:", mixed_set)


# In[15]:


list_set = set([1, 2, 3, 4])
print("Set from list:", list_set)
string_set = set("hello")
print("Set from string:", string_set)
tuple_set = set((10, 20, 30))
print("Set from tuple:", tuple_set)


# In[16]:


fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("Set after adding 'orange':", fruits)


# In[17]:


fruits = {"apple", "banana", "cherry"}
fruits.update(["mango", "grapes"])
print("Set after update:", fruits)


# In[18]:


original_set = {"apple", "banana", "cherry"}
copied_set = original_set.copy()
print("Copied set:", copied_set)


# In[19]:


fruits = {"apple", "banana", "cherry"} 
popped_element = fruits.pop()
print("Popped element:", popped_element)
print("Set after pop:", fruits)


# In[20]:


fruits = {"apple", "banana", "cherry"} 
fruits.remove("banana")
print("Set after removing 'banana':", fruits)


# In[22]:


fruits = {"apple", "banana", "cherry"} 
fruits.discard("banana")
print("Set after discarding 'banana':", fruits)
fruits.discard("orange")
print("Set after discarding 'orange':", fruits)


# In[23]:


fruits = {"apple", "banana", "cherry"} 
fruits.clear()
print("Set after clear:", fruits)


# In[26]:


set1 = {"apple", "banana", "cherry"}
set2 = {"mango", "grapes", "banana"}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)


# In[28]:


set1 = {"apple", "banana", "cherry"}
set2 = {"mango", "grapes", "banana"} 
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set) 
 


# In[29]:


set1 = {"apple", "banana", "cherry"}
set2 = {"mango", "grapes", "banana"} 
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)
difference_set_operator = set1 - set2
print("Difference using - operator:", difference_set_operator)


# In[ ]:





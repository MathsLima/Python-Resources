#!/usr/bin/env python
# coding: utf-8

# ### Função normal

# In[1]:


def somaquadrado(a, b):
    somaq = a**2 + b**2
    return somaq


# In[2]:


somaquadrado(2,3)


# ### Funçao lambda

# In[3]:


somaquadrado2 = lambda a, b: a**2 + b**2


# In[4]:


somaquadrado2(2,3)


# In[5]:


x = lambda f: f/2
x(10)


# ### Funçao map( )

# In[6]:


# Uma lista simples de velocidade, por exemplo
kmh = [5, 8, 10, 15, 22, 24, 27, 30, 32]


# In[7]:


# maneira normal de conversão
mph =[]
for i in kmh:
    mph.append(i/1.61)


# In[8]:


# maneira usando map
mph2 = list(map(lambda x: x/1.61, kmh))
print(mph2)


# ###  Funçao List Comprehension
# 

# In[9]:


caracter = [i for i in 'Python Language']
print(caracter)


# In[10]:


caracter = [i for i in 'Python Language']
print(caracter)


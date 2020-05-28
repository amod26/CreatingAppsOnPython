#!/usr/bin/env python
# coding: utf-8

# In[2]:


import kivy
from kivy.app import App
from kivy.uix.label import Label


# In[3]:


kivy.require("1.11.0")


# In[7]:


class Dhaasu(App):
    def built(self):
        return Label('Kya re bidu!')
    
if __name__=='__main__':
    Dhaasu().run()


# In[ ]:





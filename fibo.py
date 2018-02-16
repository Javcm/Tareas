
# coding: utf-8

# In[58]:


def fibop(n):
    
    a, b, s = 0, 1, 1
    
    while b <= n:
        a, b = b, a + b
        if (b % 2) == 1:
            s += b
        
    return(s)
fibop(100000)


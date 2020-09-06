#!/usr/bin/env python
# coding: utf-8

# In[17]:


lower=1
upper=100
print("prime number between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
     if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
            else:
                print(num)


# In[21]:


altitude=1400
if altitude<=1000:
    print("safe to land");
    else if altitude>1000&&altitude<5000:
      print("come down to 1000ft")
    else if altitude>5000:
        print("go around and try again")
        else:
            print("don't land")


# In[ ]:





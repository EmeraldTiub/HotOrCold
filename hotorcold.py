#!/usr/bin/env python
# coding: utf-8

# In[1]:


example = [1,2,3,4,5,6,7]


# In[2]:


from random import shuffle


# In[3]:


shuffle(example)


# In[4]:


example


# In[5]:


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# In[6]:


result =  shuffle_list(example)


# In[7]:


result


# In[8]:


mylist = (['_']*10)+['O']+(['_']*10)


# In[9]:


for i in shuffle_list(mylist):
    print(i, end='')


# In[10]:


from IPython.display import clear_output
def player_guess():
    guess = ''
    while guess not in list(range(1, 21)):
        guess = int(input('pick a damn stupid number, 1,2...19,20 : '))
        clear_output()
    return guess


# In[11]:


player_guess()


# In[12]:


mylist[20]


# In[13]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        return True
    else:
        return False


# In[14]:


def startgame(mylist):
    guess = player_guess()
    gotit = check_guess(mylist, guess)
    while not gotit:
        if guess < mylist.index('O'):
            print(guess, "Cold")
        if guess > mylist.index('O'):
            print(guess, "Hot")
        guess = player_guess()
        gotit = check_guess(mylist, guess)
    print("You got it!")
    print(mylist)


# In[19]:


mylist = (['_']*10)+['O']+(['_']*10)
mixedup_list = shuffle_list(mylist)
startgame(mixedup_list)


# In[ ]:





# In[ ]:





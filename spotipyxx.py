
# coding: utf-8

# In[ ]:


import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username=sys.argv[1]

# USerID: crfv73qfpinw7aq923mh3h6jv

try:
    token=util.prompt_for_user_token(username)
    
except:
    os.remove(f".cache-{username}")
    token=util.prompt_for_user_token(username)

spotifyObject=spotipy.spotify(auth=token)
    


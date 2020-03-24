#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Alla Topp
# JSON to CSV conversion

import json
import csv

#2 Write a generalized JSON->CSV converter function.
csvfile = ''
jsonfile = ''

def json_to_csv(jsonfile):
    with open(jsonfile, 'r') as f:
        data = json.load(f)
    
    with open(csvfile, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

json_to_csv(jsonfile)


# In[ ]:





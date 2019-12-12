#!/usr/bin/env python
# coding: utf-8

# In[4]:


from seoanalyzer import analyze
import sys
import json

site = sys.argv[1]

if len(sys.argv) > 2:
    sitemap = sys.argv[2]
    output = analyze(site, sitemap)
else:
    output = analyze(site)
    
data = []

for item in output['pages']:
    url_arr = item['url'].split('.')
    
    if url_arr[len(url_arr) - 1] != 'xml':
        warnings_arr = []
        
        for warning in item['warnings']:
            warning_separate = warning.split(':')
            
            
            if warning_separate[0] == 'Image missing alt tag':
                src_separate = warning.split('src')
                facebook_isolate = src_separate[1].split('/')
                
                if facebook_isolate[2] != 'www.facebook.com':
                    warnings_arr.append(warning.replace("\"", "'"))
                
        if len(warnings_arr) > 0:
            data.append({"url": item['url'], "warnings": warnings_arr})

with open(site.split('/')[2]+'_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


# In[ ]:





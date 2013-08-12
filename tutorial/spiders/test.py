import json
import urllib
from urlparse import urlparse
  
def solution():
   json_data=open(r'C:\Users\rakesh viyak\Google Drive\GoogleApp\Scrappy\tutorial\states.json')
   data = json.load(json_data)
   s_url=[]
   for d in data:
       s_url.append(urlparse(''.join([str(x) for x in d['link']])).hostname)
     
   print s_url
   print "\n"
   s=list(set(s_url))
   print len(s)
   print "\n"
    
   j_data=open(r'C:\Users\rakesh viyak\Google Drive\GoogleApp\Scrappy\tutorial\candidate_a.json')
   c_data = json.load(j_data)
   c_url=[]
   for c in c_data:
       c_url.append(urlparse(''.join([str(y) for y in c['source_link']])).hostname)
     
   total=list(set(c_url))
    
   print len(total)
#    print total
    
   print (list(set(s)-set(total)))
   print len(list(set(s)-set(total)))
    
   print (list(set(total)-set(s)))   
   print len(list(set(total)-set(s)))   
    
 
solution()
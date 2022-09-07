#import library 
from googlesearch import search

query = "order pizza southeast london"

# displaying 10 results from the search
for i in search(query, num_results=10):
    print(i)
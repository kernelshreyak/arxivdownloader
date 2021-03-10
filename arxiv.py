"""
    Simple python script to download Arxiv papers using either abstract URLs or PDF URLs directly

    Author: Shreyak Chakraborty (C) 2021

"""


import urllib.request
import requests
import sys

def strToFilename(text:str,fileformat:str):
    filename = "none"
    try:
        text = text.replace("[","(")
        text = text.replace("]",")")
        text = text.replace(".","_")
        text = text.replace(":","_")

        filename = text + fileformat
    except:
       pass
    finally:
        return filename
 
try:
    url = sys.argv[1]
except:
    print("INVALID ARGUMENT. Use arxiv.py <arxiv_url>")
    exit()    

# Parse Arxiv URL and get arxiv paper ID
title = url.replace(".pdf","")
url = url.replace("https://arxiv.org/abs/","")
url = url.replace("https://arxiv.org/pdf/","")
arxiv_id = url
downloadURL = "https://arxiv.org/pdf/" + arxiv_id + ".pdf"

# Get title of paper and download the PDF
hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
n = requests.get( "https://arxiv.org/abs/" + arxiv_id, headers=hearders)
al = n.text
paper_title = al[al.find('<title>') + 7 : al.find('</title>')]
print("Downloading Arxiv Paper: " + paper_title)

# convert to valid filename
filename = strToFilename(paper_title,"pdf")
urllib.request.urlretrieve(downloadURL, filename)
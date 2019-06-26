import requests
from bs4 import BeautifulSoup

def GetThreads():
     
    homeurl = 'https://www.reddit.com/r/AskReddit/'

    page = requests.get(homeurl, verify = False, headers = {'User-Agent':'Dr. Tiger Santiga'})
    soup = BeautifulSoup(page.text, 'html.parser')
    list = soup.find_all('a')
    
    outputList = []
    
    for item in list:
        if "hours" in item.text:
            outputList.append(item.get("href"))

    return outputList




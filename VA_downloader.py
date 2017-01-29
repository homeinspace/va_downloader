#! python3
#VA_downloader.py this scrips downloads all images from my thread


import os, requests, bs4

os.makedirs('C:\\Python_scripts\\visual_art', exist_ok=True)
initUrl='http://www.visualart.ro/forum/threads/24773-Despre-inceput/page1'
res=requests.get(initUrl)
initSoup=bs4.BeautifulSoup(res.text, 'html.parser')
lastPage=int(initSoup.findAll('a', {'class':'popupctrl'})[2].text[-2:])
print('The blog has %s pages.'%lastPage)
pageNum=1

while pageNum in range(lastPage+1):
    url=initUrl+str(pageNum)
    print('Downloading page %s ...'%url)
    res=requests.get(url)
    if res.raise_for_status()!=None:
        print('Error on page or you reached the end of blog.')
        break
    
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    
    postNum=1
    
    for post in soup.findAll('blockquote'):
        fileNum=0
        for img in post.findAll('img'):
            fileName='page'+str(pageNum)+'-post'+str(postNum)+'-image'+str(fileNum)+'.jpeg'
            if r'http://www.visualart.ro/forum/' in str(img.get('src')):
                print('Saving '+fileName+'...')
                url=img.get('src')
                imgFile = open('C:\\Python_scripts\\visual_art\\'+fileName, 'wb')
                res=requests.get(url)
                for chunk in res.iter_content(100000):
                    imgFile.write(chunk)
                imgFile.close()
                fileNum+=1
        postNum+=1
    pageNum+=1

print('Done!')


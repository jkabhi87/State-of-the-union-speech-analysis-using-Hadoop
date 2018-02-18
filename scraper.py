from bs4 import BeautifulSoup

import requests

with open('links.txt') as fp:
    for line in fp:
        url = "http://stateoftheunion.onetwothree.net/texts/"+line.strip()
#        print(url)
        linkfile = open(line[:-5]+".txt" , "w")
        page = requests.get(url)
        pagedata = page.text
        pagesoup = BeautifulSoup(pagedata, "html.parser")
#        linkfile.write(pagesoup.find_all('p').getText())
#        print(paragraph.get_text())
#        while((paragraph = pagesoup.find_next('p')) != null)
#            print(paragraph.get_text())
#        while(find())
#        for pa in pagesoup.find_all('p')
        linkfile.write(pagesoup.get_text())
#        print(pagesoup)
        linkfile.close()
        print(url)
#        print(pagesoup.get_text())

#r  = requests.get(url+"index.html")

#data = r.text


#soup = BeautifulSoup(data)

#for link in soup.find('a'):
    #print(link.get('href'))
#    file = open(link.get('href')+".txt" , "w")
#    page = requests.get(url+link.get('href'))
#    pagedata = page.text
#    pagesoup = BeautifulSoup(pagedata)

#    file.write(print(pagesoup))

#    for paragraph in pagesoup.find_all('p')
#        file.write(paragraph.get)

#    file.close()

#print(soup)

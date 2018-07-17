import urllib.request
from urllib.request import urlretrieve
import urllib.parse

from bs4 import BeautifulSoup
outfile = open(r'D:\pythonOM\github\top_ai2.txt', 'w') #output file on same directory

try:
    
    url='https://github.com/mbadry1/Top-Deep-Learning/blob/master/readme.md' #list url

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    print("connection ok")
    respData = resp.read()
    resp.close()
    print('Done')
    soup = BeautifulSoup(respData, "lxml")

    links = soup.find_all('a')

    for i in range(200, 201): #range to fetch the repo links from the above list

        try:
            url_now = links[i].get('href') #holds the current repo link

            headers_now = {}
            headers_now['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
            req_now = urllib.request.Request(url_now, headers = headers_now)
            resp_now = urllib.request.urlopen(req_now)
            respData_now = resp_now.read()
            resp_now.close()
            soup_now = BeautifulSoup(respData_now, "lxml")

            tmp = url_now[19:len(url_now)]
            watch = soup_now.select_one("a[href*="+tmp+"/watchers]")
            star = soup_now.select_one("a[href*="+tmp+"/stargazers]")
            desc = soup_now.find("span",itemprop="about").get_text()
            desc_ok = desc.encode('ascii', 'ignore').decode('ascii', 'ignore')
            official = soup_now.find("span", itemprop="url")
            download = soup_now.find("a", class_="get-repo-btn")
            download2 = download.find_next_siblings('a')
            star_n = star.get_text() #fetch no. of stars from star object
            watch_n = watch.get_text() #fetch no. of watch from star object
            if (official):
                ok_data = '<div class="p-3 rounded shadowDepthB" align="justify"><b> <h2>'+str(i-41)+': <a href="'+str(url_now)+'" target="_blank" rel="noopener">'+str(links[i].get_text())+'</a></h2></b><p class="pl-4">'+str(desc_ok.strip())+'</p><br><ul class="list-inline text-center"><li class="list-inline-item"><a href="'+str(url_now)+'" target="_blank" rel="noopener"><span class="fa fa-github"></span></a></li><li class="list-inline-item"><span class="fa fa-star"></span> '+str(star_n.strip())+'</li><li class="list-inline-item"><span class="fa fa-eye"></span> '+str(watch_n.strip())+'</li><li class="list-inline-item"><a href="'+str(official.a.get('href'))+'" target="_blank" rel="noopener"><span class="fa fa-globe"></span></a></li></ul></div><br><br>'
            else:
                ok_data = '<div class="p-3 rounded shadowDepthB" align="justify"><b> <h2>'+str(i-41)+': <a href="'+str(url_now)+'" target="_blank" rel="noopener">'+str(links[i].get_text())+'</a></h2></b><p class="pl-4">'+str(desc_ok.strip())+'</p><br><ul class="list-inline text-center"><li class="list-inline-item"><a href="'+str(url_now)+'" target="_blank" rel="noopener"><span class="fa fa-github"></span></a></li><li class="list-inline-item"><span class="fa fa-star"></span> '+str(star_n.strip())+'</li><li class="list-inline-item"><span class="fa fa-eye"></span> '+str(star_n.strip())+'</li></ul></div><br><br>'
            outfile.write(ok_data + '\n')
            print(str(i-41)+' : '+ str(links[i].get_text()))
            print(str(download2[0].get('href')))

        except Exception as e:
            raise e
    outfile.close()
 
except Exception as e:
    print(str(e))
    
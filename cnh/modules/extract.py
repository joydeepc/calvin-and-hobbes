import requests
from bs4 import BeautifulSoup as bs
from tempfile import NamedTemporaryFile

def get_calvin(url):
    session = requests.Session()
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36"}
    session.headers = headers
    content = session.get(url).content
    soup = bs(content, "lxml")
    cont = soup.find(attrs={'class':'item-comic-image'}).img['src']
    resp = session.get(cont).content
    session.close()
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(resp)
    img_temp.flush()

    cal_dict = {
        'img_temp' : img_temp,
        'url' : cont
    }

    return cal_dict

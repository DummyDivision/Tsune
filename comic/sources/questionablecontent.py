from bs4 import BeautifulSoup
from requests.api import get
from comic.sources.base_source import BaseSource


class QuestionableContent(BaseSource):
    def scrape_page(self, url):
        r = get(url, timeout=0.7)
        soup = BeautifulSoup(r.text)
        img = soup.find("img", id="strip")
        self.url = img["src"].replace("./", "http://questionablecontent.net/")
        self.alt = soup.find("div", id="news").text
        self.title = self.alt

    def get_random_url(self):
        r = get("http://questionablecontent.net/", timeout=0.7)
        self.valid = True
        soup = BeautifulSoup(r.text)
        ul = soup.find("ul", id="comicnav")
        lis = ul.find_all("li")
        a = lis[4].find("a", text="Random")
        return a["href"]
from bs4 import BeautifulSoup
from comic.sources.base_source import BaseSource
from requests.api import get


class XKCD(BaseSource):
    url = "http://imgs.xkcd.com/comics/tape_measure.png"
    title = "This sequence was later reproduced in the International Tape-Extending Federation archives, retitled 'The Founding of the Sport'."
    alt = "Tape Measure"

    def scrape_page(self, url):
        """Get a comic from XKCD

        The determined values are written to self.valid, self.url, self.title and self.alt

        """
        r = get(url, timeout=0.7)
        self.valid = True
        soup = BeautifulSoup(r.text)
        div = soup.find("div", id="comic")
        image = div.find("img")
        self.url = image["src"]
        self.title = image["title"]
        self.alt = image["alt"]

    def get_random_url(self):
        return "http://c.xkcd.com/random/comic/"
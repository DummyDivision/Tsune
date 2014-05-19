from django.views.generic.base import TemplateView
from requests import get
from bs4 import BeautifulSoup
from threading import Thread


class ComicView(TemplateView):
    _valid = False
    _url = "http://imgs.xkcd.com/comics/tape_measure.png"
    _title = "This sequence was later reproduced in the International Tape-Extending Federation archives, retitled 'The Founding of the Sport'."
    _alt = "Tape Measure"

    def scrape_xkcd(self):
        r = get("http://c.xkcd.com/random/comic/", timeout=0.7)
        soup = BeautifulSoup(r.text)
        div = soup.find("div", id="comic")
        image = div.find("img")
        self._valid = True
        self._url = image["src"]
        self._title = image["title"]
        self._alt = image["alt"]

    def get_comic(self):
        t = Thread(target=self.scrape_xkcd)
        t.start()
        t.join(1)
        if t.is_alive():
            if self._valid:
                t.join()
            else:
                t._Thread__stop()
        return self._url, self._title, self._alt

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['comic_url'], context['comic_title'], context['comic_alt'] = self.get_comic()
        return context
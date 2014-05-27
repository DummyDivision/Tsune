from threading import Thread


class BaseSource:
    valid = False
    url = None
    title = None
    alt = None

    def scrape_page(self, url):
        pass

    def scrape(self):
        self.scrape_page(self.get_random_url())

    def get_random_url(self):
        pass

    def get_comic(self):
        """Run scrape in a separate thread and kill it after a one second timeout if necessary.

        Returns url, title, alt of the scraped comic

        """
        t = Thread(target=self.scrape)
        t.start()
        t.join(2)
        if t.is_alive():
            if self.valid:
                t.join()
            else:
                t._Thread__stop()
        return self.url, self.title, self.alt
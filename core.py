import requests
import re
from bs4 import BeautifulSoup
from utils.liveStreamer import ChartStreamer


class AuthorProbe:
    def __init__(self, query, results_per_page=15, page=1, max_pages=False):
        self.url_template = (
            'https://ssearch.oreilly.com/?'
            'i=1;'
            'page={0};'
            'q={1};'
            'q1=Books;'
            'x1=t1'
        )
        self.data_url = self.url_template.format(page, query)
        self.query = query
        self.session = requests.Session()
        self.params = {}
        self.page = page
        self.results_per_page = results_per_page
        self.max_pages = max_pages
        self.authors = {}

        # Fetch initial data
        self.pull_data()
        self.get_total_results()
        self.get_all()

    def pull_data(self):
        self.data = self.session.get(self.data_url, params=self.params).text
        self.soup = BeautifulSoup(self.data, "lxml")

    def get_total_results(self):
        results_regex = re.compile('of (.*?)\n')
        self.total_results = int(re.findall(
            results_regex,
            self.soup.select('h1.bread_crumb')[0].text)[0])
        self.total_pages = int(
            round(self.total_results / self.results_per_page)
        )
        print('Total pages:', self.total_pages)

    def increment_page(self):
        self.page += 1
        self.data_url = self.url_template.format(self.page, self.query)

    def get_all(self):
        for page in range(self.page, self.total_pages):
            print('Processing page', self.page, '...')
            self.get_authors()

            self.increment_page()
            if self.max_pages and self.page > self.max_pages:
                break

            # Load data for next page
            self.pull_data()

    def get_authors(self):
        for book in self.soup.find_all('article'):
            for tag in book.find_all('p', attrs={'class': 'note'}):
                # We need to limit to instances of solely the "note" class
                if len(tag.attrs['class']) == 1 and 'Language' not in tag.text:
                    authors = tag.text.split('By ')[1].split(', ')
                    for author in authors:
                        friends = [a for a in authors if a != author]
                        self.add_update_author(author, friends)

    def add_update_author(self, author, friends):
        if author not in self.authors.keys():
            self.authors[author] = {'friends': []}
        for friend in friends:
            if friend not in self.authors[author]['friends']:
                self.authors[author]['friends'].append(friend)


def init(hostname, port, query, max_pages=False):
    a = AuthorProbe(query=query, max_pages=max_pages)

    # generate chart
    stream = ChartStreamer(hostname=hostname,
                           port=port,
                           workspace="workspace1")

    for author, value in a.authors.items():
        print('Adding nodes for', author, 'to stream...')
        stream.addnodes(author, value['friends'])

import codecs

from scraping.parsers import *

parsers = ((work,'https://www.work.ua/jobs-python/'),
           (jooble,'https://ua.jooble.org/SearchResult?sps=True&ukw=%D0%B7%20%D0%BF%D1%80%D0%BE%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%D0%BC'),
           )

errors, jobs = [], []
for func, url in parsers:
    e, j = func(url)
    jobs += j
    errors += e
if __name__ == '__main__':
    h = codecs.open('../work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
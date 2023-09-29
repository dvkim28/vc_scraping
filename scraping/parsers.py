import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint
__all__ = ('work', 'jooble')

headers = [
    {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    },
    {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/102.0.0.0'
    },
    {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
    },
]


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    resp = requests.get(url, headers=headers[randint(0,2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'id': 'pjax-job-list'})
        div_list = main_div.find_all('div', attrs={'class': 'card card-hover card-visited wordwrap job-link'})
        for div in div_list:
            title = div.find('h2')
            url = title.a['href']
            description = div.p.text
            company = 'No name'
            logo = div.find('img')
            if logo:
                company = logo['alt']
            jobs.append({
                'title': title.text,
                'url': domain + url,
                'company': company,
                'description': description})
        else:
            errors.append({'url': domain + url, 'title': "Page not found"})
    return errors, jobs


def jooble(url):
    jobs = []
    errors = []
    domain = 'https://ua.jooble.org'
    resp = requests.get(url, headers=headers[randint(0,2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
        article = main_div.find_all('article')
        for div in article:
            title = div.find('a').text
            url = str(div.find('a', attrs={
                'class': 'jkit_Efecu jkit_ff9zU hyperlink_appearance_undefined jkit__gDKk g2JQMz'})['href'])
            description = div.find('div', attrs={'class': 'PAM72f'}).text
            company = div.find('div', attrs={'class': 'heru4z'}).text
            jobs.append({
                'title': title,
                'url': domain + url,
                'company': company,
                'description': description})
        else:
            errors.append({'url': domain + url, 'title': "Page not found"})

    return errors, jobs


if __name__ == '__main__':
    url = 'https://www.work.ua/jobs-python/'
    errors, jobs = work(url)
    h = codecs.open('../workua.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()

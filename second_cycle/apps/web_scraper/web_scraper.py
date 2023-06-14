from bs4 import BeautifulSoup
import requests

class WebScraper(object):
    def web_scraper_movie(self, movie):
        website = 'https://subslikescript.com/%s'%movie
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
        return (title, transcript)
            
    def web_scraper_page(self, page):
        website = 'https://subslikescript.com/movies?page=%s'%page
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        ul = soup.find('ul', class_='scripts-list')
        list_data = ul.find_all("a", href=True)
        movies = dict()
        for data in list_data:
            movies[data['href']] = data.text
        return movies
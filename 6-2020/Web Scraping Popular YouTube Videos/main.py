from selenium import webdriver
from bs4 import BeautifulSoup

urls = [
    'https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ',
    'https://www.youtube.com/user/thenewboston',
    'https://www.youtube.com/user/gotreehouse',
    'https://www.youtube.com/user/derekbanas',
    'https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ',
    'https://www.youtube.com/user/ProgrammingKnowledge'
]

def main():
    driver = webdriver.Chrome()
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a',id='video-title')
        views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a',id='video-title')
        print('Channel: {}'.format(url))
        i = 0 # views and time
        j = 0 # urls
        for title in titles[:10]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
            i+=2
            j+=1

main()
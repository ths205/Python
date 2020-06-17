                                                                                           

from bs4 import BeautifulSoup
import requests
import urllib2


def scrape_times_article(url):

    """
    This function takes in an url and saves it as an html document.
    It scrapes for the title, name, and date.
    """

    if type(url) != str:
       raise TypeError("This is not a type string")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    #div_meta = soup.find('div', id="story-meta")
    h_1 = soup.find('h1').text

    span_class = soup.find('span', class_="byline")
    span_name = span_class.find('span',class_="byline-author").text
    time_class = soup.find('time', class_="dateline").text
    paragraphs = soup.find_all('p', attrs={'class':['story-body-text', 'story-content']})

    print(h_1)
    print(span_name)
    print(time_class)
    #print(paragraph)

    for p in paragraphs:
       print(p.get_text())

    #f = open('virt_reality_car.html', 'w')
    #f.write(h_1)
    #f.write(span_name)
    #f.write(time_class)
    #for p in paragraphs:
       #f.write(p.get_text())

def main():

    web_address='https://www.nytimes.com/2017/10/29/business/virtual-reality-driverless-cars.html'
    scrape_times_article(web_address)


if __name__=="__main__":
    main()

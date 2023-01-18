import requests
import pandas as pd
from bs4 import BeautifulSoup

URL= "https://www.amazon.in/product-reviews/B08FB2LNSZ/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&filterByStar=all_stars&reviewerType=all_reviews&pageNumber="

class WebScraper:
  def __init__(self,url,total_pages):
    self.url = url
    self.response = None
    self.total_pages = total_pages

  def check_status_code(self):
    try:
      self.response = requests.get(self.url)
      status_code= self.response.status_code
      if int(status_code) == 200:
        print(f'Successful request! Status Code: {status_code}')        
      elif int(status_code) == 404:
        print(f'Page not found Status Code: {status_code}')
      elif int(status_code) == 408:
        print(f'Connection time out! Status Code: {status_code}')
    except Exception as e:
      print(e)

  def scrape_review(self):

    body = []
    title = []
    rating = []
    for page in range(self.total_pages):

      response = requests.get(f"{self.url}+{page+1}")
      soup = BeautifulSoup(response.text,'html.parser')
      reviews = soup.find_all('div',{'data-hook':'review'})

      for review in reviews:
        body.append(review.find('a',{'data-hook':'review-title'}).text.strip())
        title.append(review.find('span',{'data-hook':'review-body'}).text.strip())
        rating.append(float(review.find('i',{'data-hook':"review-star-rating"}).text.replace('out of 5 stars','').strip()))


    return body,title,rating


  def annotate_sentiment(self,rating):
    sentiment = []
    for star in rating:
      if(float(star)>=4):
        sentiment.append("Positive")
      elif (float(star) >= 2 and float(star)<4):
        sentiment.append("Neural")
      else:
        sentiment.append("Negative")
    return sentiment

  def makeDataFrame(self,title,body,rating,sentiment):
    temp_dict = {
        "Title" : title,
        "Content" : body,
        "rating" : rating,
        "sentiment" : sentiment
    }
    return pd.DataFrame(temp_dict)

  def saveData(self,dataframe):
    dataframe.to_csv(f"data.csv",index=False)

  def initialize_scraper(self):
    scraper.check_status_code()
    body,title,rating = scraper.scrape_review()
    sentiment = scraper.annotate_sentiment(rating)
    dataframe = scraper.makeDataFrame(title,body,rating,sentiment)
    scraper.saveData(dataframe)
    
    
scraper = WebScraper(URL,500)
scraper.initialize_scraper()

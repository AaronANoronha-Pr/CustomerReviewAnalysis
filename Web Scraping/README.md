# Data Collection - Web Scraping
Web scraping is the process of extracting data from websites. It is typically done using a web scraping tool or a web scraping library, which sends an HTTP request to a website's server to retrieve the HTML content of the page. The HTML is then parsed and the desired information is extracted.


To perform web-scraping add the url, create an instance of the WebScraper class and pass in the URL and total number of pages to be scraped as argument and calls the **initialize_scraper** method to start the scraping process.

```ruby
URL= "https://www.amazon.in/product-reviews/B08FB2LNSZ/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&filterByStar=all_stars&reviewerType=all_reviews&pageNumber="
scraper = WebScraper(URL,500)
scraper.initialize_scraper()
```

**Note** - Scraped data is in [Data Dump](https://github.com/AaronANoronha/CustomerReviewAnalysis/tree/main/Data/Data%20Dump)

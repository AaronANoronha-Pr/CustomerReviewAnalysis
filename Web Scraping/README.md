# Data Collection - Web Scraping
Web scraping is the process of extracting data from websites. It is typically done using a web scraping tool or a web scraping library, which sends an HTTP request to a website's server to retrieve the HTML content of the page. The HTML is then parsed and the desired information is extracted.

## Changes Made

- The code has been updated to include multithreading, which greatly improves the performance and efficiency of the scraping process. With multithreading, the scraper is able to scrape multiple pages simultaneously, reducing the overall scraping time.
- Using multithreading, we are able to take full advantage of the computer's resources, such as CPU and memory, to scrape data at a faster rate.
- With multithreading, it also became harder for the website to detect and block the IP address.
- Scaling became much easier with multithreading, which makes it useful for scraping large amounts of data.

## Usage

- Initialize the WebScraper class with the URL of the website to be scraped and the total number of pages to be scraped.
- Use the `scrape_review` method to extract the title, body, and rating of reviews from the scraped HTML.
- Use the `annotate_sentiment` method to take the rating of the reviews and annotate them as Positive, Negative or Neutral.
- Use the `makeDataFrame` method to take the title, body, rating, sentiment, and make a pandas dataframe.
- Use the `saveData` method to save the dataframe to a CSV file.

## Time Taken
- Wihtout multithreading - 207 seconds
- 2 core multithreading - 57 seconds
- 32 core multithreading - 32 seconds

To perform web-scraping add the url, create an instance of the WebScraper class and pass in the URL and total number of pages to be scraped as argument and calls the **initialize_scraper** method to start the scraping process.

```ruby
URL= "https://www.amazon.in/product-reviews/B08FB2LNSZ/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&filterByStar=all_stars&reviewerType=all_reviews&pageNumber="
scraper = WebScraper(URL,500)
scraper.initialize_scraper()
```

**Note** - Scraped data is in [Data Dump](https://github.com/AaronANoronha/CustomerReviewAnalysis/tree/main/Data/Data%20Dump)

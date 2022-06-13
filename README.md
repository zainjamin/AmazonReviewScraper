# AmazonReviewScraper
A web scraper that retrieves all Amazon.ca reviewer's name and review for a given ASIN. The data can be exported to a .csv file for analysis.
## Usage
### Create a Scraper
In Python 3, import the module. Once imported, create a new AmazonReviewScraper object by specifying the [ASIN](https://www.nchannel.com/blog/amazon-asin-what-is-an-asin-number/). 
For example, to create a review object of the 2020 Macbook Air, use the ASIN of `B08N5LNQCX`
```
macbook_review_scraper = AmazonReviewScraper('B08N5LNQCX')
```
### Scrape
To perform the web scraping, use the `scrape()` function. 
```
macbook_review_scraper.scrape()
```
This will populate the list of names and reviews in the object.

### Export as CSV
To export as a CSV, use the `.to_csv()` function.
```
macbook_review_scraper.to_csv()
```
This will create `reviews.csv` in the project directory. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_quotes(url,tag_type,attribute_type,attribute_value):
    # Set up the Selenium WebDriver
    driver = (
        webdriver.Chrome()
    )  # Make sure you have chromedriver installed and in your PATH
    # open chromedriver to the specified url
    driver.get(url)


    # Wait until the page contains a tag with an attribute = attribute_type, with a value of attribute_value (or 10 seconds if flare is not found)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((attribute_type,attribute_value))
    )


    # Extract the whole html
    initial_html = driver.page_source
    # parse html for easier scraping
    initial_soup = BeautifulSoup(initial_html, "html.parser")
    # find all tag corresponding with the research attributes (tag_type,attribute_type,attribute_value)
    if attribute_type == By.CLASS_NAME:
        initial_quotes = initial_soup.find_all(tag_type, class_=attribute_value)
    elif attribute_type == By.ID:
        initial_quotes = initial_soup.find_all(tag_type, id=attribute_value)
    # print values
    extract_and_print_quotes(initial_quotes)


#    # Simulate scroll events to load additional content
#    #for scroll_count in range(5):  # Assuming there are 5 scroll events in total
#    # Scroll down using JavaScript
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#    # Wait for the dynamically loaded content to appear
#    WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((attribute_type,attribute_value))
#    )


#   # Extract and print the newly loaded quotes
#   scroll_html = driver.page_source
#   scroll_soup = BeautifulSoup(scroll_html, "html.parser")
#   if attribute_type == By.CLASS_NAME:
#       initial_quotes = initial_soup.find_all(tag_type, class_=attribute_value)
#   elif attribute_type == By.ID:
#       initial_quotes = initial_soup.find_all(tag_type, id=attribute_value)
    # print values
#   extract_and_print_quotes(scroll_quotes)


    # Close the WebDriver
    driver.quit()

def extract_and_print_quotes(quotes):
 
    for quote in quotes:
        for content in quote.contents:
            print(content)
    #print(quote)

if __name__ == "__main__":
   #website to scrape
   target_url = "http://localhost:8080"
   #type of tag to find
   tag_type = "div" #"span"
   #attribute to look inside tag_type tags
   attribute_type= By.CLASS_NAME #By.ID
   #value of the attribute_type attribute
   attribute_value = "test"
   #look inside the whole html, searching for a tag = tag_type that has an attribute of type attribute_type that has a value = attribute_value
   scrape_quotes(target_url,tag_type,attribute_type,attribute_value)
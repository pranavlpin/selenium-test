from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to Google's homepage
    driver.get("https://www.google.com")

    # Find the search box element
    search_box = driver.find_element_by_name("q")

    # Type "OpenAI" into the search box
    search_box.send_keys("OpenAI")

    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Check if "OpenAI" appears in the search results
    assert "OpenAI" in driver.page_source

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_google_search()

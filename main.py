from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup


# Set up the Selenium browser (using Edge in this example)
options = webdriver.EdgeOptions()

driver = webdriver.Edge(options=options)

# Navigate to the Epic Games Store page
driver.minimize_window()
driver.get('https://store.epicgames.com/en-US/')

# Get the page source after JavaScript has loaded
page_source = driver.page_source

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Search for content that includes "Free Games"
free_games_section = soup.find_all(string=lambda text: 'Free Games' in text)

# Output the results
if free_games_section:
    for section in free_games_section:
        parent_tag = section.find_parent().find_parent().find_parent()
        
        section_tag = soup.find_all("section")
    
        for i, section in enumerate(section_tag, 1):
            h6_tag = section.find_all("h6")
            if h6_tag:
                for h6 in h6_tag:
                    print(h6.text)
                    print(h6.find_parent().find("p").find("span").text)
                    print()
else:
    print("No section containing 'Free Games' found.")

# Close the browser
driver.quit()

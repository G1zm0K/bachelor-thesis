from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from find_banner import find_banner

def crawl(driver, selectors, sites, accept_words_list):
    for index, site in enumerate(sites):
        driver.get(site)
        sleep(5)
        banner_data = {"potential_elements": []}
        elements = driver.find_elements(By.CSS_SELECTOR, selectors)

        #Find the element that contains accept word
        find_banner(driver,elements,accept_words_list,banner_data)

        #If not found, switch to iframes and try again
        if not "element_found" in banner_data:
            iframe_contents = driver.find_elements(By.CSS_SELECTOR, "iframe")
            for content in iframe_contents:
                print("Switching to iframe: {}".format(content.id))
                driver.switch_to.frame(content)
                find_banner(driver,elements,accept_words_list,banner_data)
                driver.switch_to.default_content()

        if "element_found" in banner_data:
            print(banner_data["element_found"])

        driver.save_screenshot('screenshots/' + str(index) + '.png')
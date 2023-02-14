from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from find_banner import find_banner

def crawl(driver, selectors, sites, accept_words_list):
    for index, site in enumerate(sites):
        print("--------------------------------------------------------------")
        print("Getting site: " + str(site))
        driver.get(site)
        print("Sleeping for 3 seconds")
        sleep(3)
        banner_data = {"potential_elements": []}

        #Find the element that contains accept word
        print("Finding banner...")
        find_banner(driver,selectors,accept_words_list,banner_data)

        #If not found, switch to iframes and try again
        if not "element_found" in banner_data:
            iframes = driver.find_elements(By.CSS_SELECTOR, "iframe")
            print("No initial element found, now looking in iframes")
            for iframe in iframes:
                driver.switch_to.frame(iframe)
                print("Finding banner...")
                find_banner(driver,selectors,accept_words_list,banner_data)
                driver.switch_to.default_content()

        if not "element_found" in banner_data:
            print("No element found")

        sleep(1)
        print("Making screenshot")
        driver.save_screenshot('screenshots/' + str(index) + '.png')
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from find_banner import find_banner
import logging

def crawl(driver, selectors, sites, accept_words_list, deny_words_list):
    for index, site in enumerate(sites):
        try:
            logging.info('Trying site: ' + site)
            driver.get(site)
            logging.info('Sleeping for 3 seconds')
            sleep(3)
            banner_data = {"potential_elements": []}

            #Find the element that contains accept word
            logging.info('Finding consent element...')
            find_banner(driver,selectors,accept_words_list,banner_data)

            #If not found, switch to iframes and try again
            if not "element_found" in banner_data:
                iframes = driver.find_elements(By.CSS_SELECTOR, "iframe")
                logging.info('No initial consent element found, now looking in iframes...')
                for iframe in iframes:
                    driver.switch_to.frame(iframe)
                    logging.info('Switched to iframe: ' + iframe)
                    find_banner(driver,selectors,accept_words_list,banner_data)
                    driver.switch_to.default_content()

            if not "element_found" in banner_data:
                logging.info('No consent element could be found')

            banner_data = {"potential_elements": []}

            #Find the element that contains the reject word
            logging.info('Finding reject element...')
            find_banner(driver,selectors,deny_words_list,banner_data)

            #If not found, switch to iframes and try again
            if not "element_found" in banner_data:
                iframes = driver.find_elements(By.CSS_SELECTOR, "iframe")
                logging.info('No initial reject element found, now looking in iframes...')
                for iframe in iframes:
                    driver.switch_to.frame(iframe)
                    logging.info('Switched to iframe: ' + iframe)
                    find_banner(driver,selectors,deny_words_list,banner_data)
                    driver.switch_to.default_content()

            if not "element_found" in banner_data:
                logging.info('No reject element could be found')

            logging.info('Sleeping for one second')
            sleep(1)
            logging.info('Making screenshot')
            driver.save_screenshot('screenshots/' + str(index) + '.png')
        except:
            logging.error('Something went wrong, trying next site')

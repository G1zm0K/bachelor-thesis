from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def crawl(driver, selectors, sites, accept_words_list):
    for index, site in enumerate(sites):
        driver.get(site)
        sleep(5)
        banner_data = {"candidate_elements": []}
        contents = driver.find_elements(By.CSS_SELECTOR, selectors)

        for c in contents:
            try:
                if c.text.lower().strip(" ✓›!\n") in accept_words_list:
                    banner_data["candidate_elements"].append({"tag_name": c.tag_name,
                                                                "text": c.text,
                                                                "size": c.size,
                                                                })
                    driver.execute_script("arguments[0].style.border='4px solid red'", c)
                    break
            except:
                break

        driver.save_screenshot('screenshots/' + str(index) + '.png')

        if banner_data:
            print(str(index) + str(banner_data))
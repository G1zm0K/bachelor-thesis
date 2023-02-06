from selenium import webdriver
from selenium.webdriver.common.by import By
from make_list import make_wordlist

sites = [
    "http://www.bbc.co.uk",
    "http://www.dailymail.co.uk",
    "http://www.theguardian.com/",
    "http://www.yahoo.com/",
    "http://www.bbc.com/",
]

GLOBAL_SELECTOR = "a, button, div, span, form, p"
driver = webdriver.Firefox()
print("Driver started successfully")

make_wordlist("accept_words.txt")
print("Wordlist created successfully, now starting crawl")

for index, site in enumerate(sites):
    driver.implicitly_wait(10) # seconds
    driver.get(site)
    banner_data = {"matched_containers": [], "candidate_elements": []}
    contents = driver.find_elements(By.CSS_SELECTOR, GLOBAL_SELECTOR)

    for c in contents:
        print(c.tag_name)
        try:
            if c.text.lower().strip(" ✓›!\n") in accept_words_list:
                banner_data["candidate_elements"].append({"id": c.id,
                                                            "tag_name": c.tag_name,
                                                            "text": c.text,
                                                            "size": c.size,
                                                            })
                driver.execute_script("arguments[0].style.border='4px solid red'", c)
                break
        except:
            break

    driver.save_screenshot('screenshots/' + str(index) + '.png')

    print(banner_data)



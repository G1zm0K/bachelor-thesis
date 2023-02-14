from selenium.webdriver.common.by import By

def find_banner(driver,selectors,accept_words_list,banner_data):
    print("Selecting elements...")
    elements = driver.find_elements(By.CSS_SELECTOR, selectors)
    print("Searching elements...")
    for e in elements:
        if e.text.lower().strip(" ✓›!\n") in accept_words_list:
            banner_data["potential_elements"].append({"tag_name": e.tag_name,
                                                        "text": e.text,
                                                        "size": e.size,
                                                        })
            banner_data["element_found"] = e.tag_name
            driver.execute_script("arguments[0].style.border='4px solid red'", e)
            print("Element found!: " + str(e.tag_name) + " with text: " + str(e.text))
            break
            
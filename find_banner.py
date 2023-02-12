def find_banner(driver,elements,accept_words_list,banner_data):
    for e in elements:
        if e.text.lower().strip(" ✓›!\n") in accept_words_list:
            banner_data["potential_elements"].append({"tag_name": e.tag_name,
                                                        "text": e.text,
                                                        "size": e.size,
                                                        })
            banner_data["element_found"] = e.id
            driver.execute_script("arguments[0].style.border='4px solid red'", e)
            print("Element found!: " + str(e.text))
            break
            
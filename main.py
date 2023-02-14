from selenium import webdriver
from make_list import make_wordlist
from crawler import crawl

SITES = [
    "http://www.theguardian.com/",
    "http://www.yahoo.com/",
    "http://www.bbc.com/",
    "https://www.thesun.co.uk/",
    "https://www.mirror.co.uk/",
    "https://www.manchestereveningnews.co.uk/",
    "https://www.telegraph.co.uk/"
]
GLOBAL_SELECTOR = "a, button, div, span, form, p"
ACCEPT_WORDS_LIST = "wordlists/accept_all.txt"

accept_words_list = make_wordlist(ACCEPT_WORDS_LIST)
print("Wordlist created")

driver = webdriver.Firefox()
print("Driver started")

print("Starting crawl...")
crawl(driver, GLOBAL_SELECTOR, SITES, accept_words_list)

print("Crawl finished, shutting down")
driver.quit()

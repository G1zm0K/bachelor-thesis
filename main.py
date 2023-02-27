from selenium import webdriver
from make_list import make_wordlist
from crawler import crawl


GLOBAL_SELECTOR = "a, button, div, span, form, p"
ACCEPT_WORDS_LIST = "wordlists/consent_nl.txt"
DENY_WORDS_LIST = "wordlists/reject_nl.txt"
WEBSITE_LIST = "websites/nl.txt"

sites = make_wordlist(WEBSITE_LIST)
accept_words_list = make_wordlist(ACCEPT_WORDS_LIST)
deny_words_list = make_wordlist(DENY_WORDS_LIST)
print("Wordlist created")

driver = webdriver.Firefox()
print("Driver started")

print("Starting crawl...")
crawl(driver, GLOBAL_SELECTOR, sites, accept_words_list, deny_words_list)

print("Crawl finished, shutting down")
driver.quit()

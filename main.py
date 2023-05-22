from selenium import webdriver
from make_list import make_wordlist
from crawler import crawl
import logging
import pandas as pd

GLOBAL_SELECTOR = "button, a, p, div, span, form"
ACCEPT_WORDS_LIST = "wordlists/consent_nl.txt"
REJECT_WORDS_LIST = "wordlists/reject_nl.txt"
WEBSITE_LIST = "websites/test.txt"

data = {}

logging.basicConfig(filename='info_log.log', encoding='utf-8', level=logging.INFO)

logging.info('Starting program...')

logging.info('Making wordlists...')
sites = make_wordlist(WEBSITE_LIST)
accept_words_list = make_wordlist(ACCEPT_WORDS_LIST)
reject_words_list = make_wordlist(REJECT_WORDS_LIST)
logging.info('Wordlists created')

logging.info('Starting driver...')
driver = webdriver.Firefox()
logging.info('Driver started')

logging.info('Starting crawl...')
data = crawl(driver, GLOBAL_SELECTOR, sites, accept_words_list, reject_words_list, data)
logging.info('Finished crawl')

logging.info('Shutting down driver...')
driver.quit()
logging.info('Driver shut down')

logging.info('Sending data to file...')
data.to_csv('data.csv', index=False)
logging.info('Data sent to file')
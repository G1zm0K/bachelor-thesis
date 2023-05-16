from selenium import webdriver
from make_list import make_wordlist
from crawler import crawl
import logging

GLOBAL_SELECTOR = "a, button, div, span, form, p"
ACCEPT_WORDS_LIST = "wordlists/consent_nl.txt"
REJECT_WORDS_LIST = "wordlists/reject_nl.txt"
WEBSITE_LIST = "websites/nl_minus_nl_original.txt"

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
crawl(driver, GLOBAL_SELECTOR, sites, accept_words_list, reject_words_list)
logging.info('Finished crawl')

logging.info('Shutting down driver...')
driver.quit()
logging.info('Driver shut down')

import os
import re
import sys
import time
from itertools import groupby
from urllib.parse import urlparse

import newspaper
import requests
from newspaper import Article, Config, Source

protocol = "http"
host = "www.theguardian.com"
domain = "profile"
name = "markkermode"


def main(data_dir):
    print(" ***  STARTING  *** ")
    # 1. visit page
    # 2. parse, extract links to MK articles
    # 3a. fetch each MK article
    # 3b. extract article metadata (title, date, etc)
    # 4. persist article
    article_url_path = os.path.join(data_dir, "all_article_urls.txt")
    category_pages_dir = os.path.join(data_dir, "category_pages")
    os.makedirs(category_pages_dir, exist_ok=True)

    all_articles = run_category_page_scraper(article_url_path)

    print(f"Found {len(all_articles)} articles (Grand Total)")
    master_url_path = os.path.join(data_dir, "master_article_urls.txt")
    persist_article_urls(all_articles, master_url_path)
    print(" ***  DONE  *** ")


def run_category_page_scraper(article_url_path, category_pages_dir):
    master_article_urls = []
    count = 0
    for i in range(2):
        page = i + 1
        url = build_url(page)
        print(f"parsing page: {page}")
        article_urls, html = parse_category_page(url)
        category_html_path = os.path.join(category_pages_dir, url)
        persist_page(html, category_html_path)
        count += len(article_urls)
        print(f"Found total {count} articles")
        master_article_urls.extend(article_urls)
        persist_article_urls(article_urls, article_url_path)
        # be polite and sleep between calls
        time.sleep(10)
    return unique(master_article_urls)


def build_url(page):
    return f"{protocol}://{host}/{domain}/{name}?page={page}"


def parse_category_page(url):
    print(f"parsing url: {url}")
    config = Config()
    config.memoize_articles = False
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124  Safari/537.36"
    config.browser_user_agent = user_agent
    paper = newspaper.build(url, config=config)
    article_urls = paper.article_urls()
    return unique([url for url in article_urls if _is_film_review_url(url)]), paper.html


def unique(items):
    # strip off hashtag locations:
    items = [re.sub("#[a-zA-Z_]+$", "", item) for item in items]
    # return items while preserving original order
    return sorted(set(items), key=items.index)


def _is_film_review_url(url):
    path = urlparse(url).path
    if path.startswith("/film"):
        return True
    return False


def persist_article_urls(article_urls, article_url_path):
    with open(article_url_path, "a") as fo:
        fo.write("\n".join(article_urls))


def persist_page(html, category_html_path):
    with open(category_html_path, "w") as fo:
        fo.write(html)


# def fetch_category_page(url):

#     article = Article(url)
#     article.download()
#     html = article.html
#     article.parse()
#     # authors = article.authors
#     pub_date = article.publish_date
#     text = article.text
#     article.nlp()
#     keywords = article.keywords
#     summary = article.summary


if __name__ == "__main__":
    # data_dir = DevData().data_dir
    if len(sys.argv) != 2:
        print("ERROR. data_directory must be passed in as an argument")
        print("USAGE: \n\t$ python podcast_downloader /path/to/data_dir")
    if len(sys.argv) == 2:
        data_dir = sys.argv[1]
        os.makedirs(data_dir, exist_ok=True)
        main(data_dir)


"""
EXAMPLE USAGE
$ python kermode_downloader.py ../data/kermode/

"""

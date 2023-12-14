
"""
Use Case
- collect all historic podcasts
"""

import os
from bs4 import BeautifulSoup 
import sys
from collections import defaultdict
import json
import re
import traceback
import shutil
import logging
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.INFO)
import requests
import time

############################################################
# Decorator
############################################################
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        duration = (te-ts)
        duration = float(f"{duration:.2f}")
        logging.info(f"timit: {method.__name__} running time: {duration} sec ")
        return result
    return timed

############################################################
# Driver functions
############################################################
def main(data_dir):
    _clean_up()
    podcast_dir, jsonl_dir = _define_data_dirs(data_dir)
    full_feed_dict = _prep_feed_list(podcast_dir, jsonl_dir)
    retrieved_list_path = os.path.join(data_dir, "retrieved_list.txt")
    if not os.path.exists(retrieved_list_path):
      open(retrieved_list_path, "a").close()
    processed_feeds = [x.strip().replace("_", "/") for x in open(os.path.join(data_dir, "retrieved_list.txt"))]
    feed_list = _filter_feed_list(full_feed_dict, processed_feeds)
    print("*** Executing ***")
    execute(feed_list, podcast_dir)
    print("*** Done ***")
    _clean_up()

def execute(feed_list, podcast_dir):
  # iterate over feed list, download each mp3 file to podcast dir and then sleep to be a polite scraper
  num_feeds = len(feed_list)
  for idx, feed in enumerate(feed_list):
    cnt = f"{idx}/{num_feeds}"
    handle_content(feed["pub_date"], feed["url"], podcast_dir, cnt)


@timeit
def handle_content(date, url, podcast_dir, cnt):
  print(f"count: {cnt}\tprocessing {date} ...")
  date = f'{date.replace("/", "_")}'
  outpath = os.path.join(podcast_dir, f"{date}.mp3")
  # content = _download_mp3(url)
  # _save_mp3(content, outpath)
  _fetch_and_save_mp3(url, outpath)
  logging.info(f"retrieved: {date}")
  time.sleep(5)


def _clean_up():
  print("Cleaning up load and retrieved_list files...")
  log_path = "log.txt"
  retrieved_path = os.path.join(data_dir, "retrieved_list.txt")
  retrieved = [x.strip() for x in open(retrieved_path)]
  log = [x.strip() for x in open(log_path) if x.startswith("INFO") and "retrieved" in x]
  dates = [re.sub("^.*retrieved: ", "", x) for x in log]
  data = retrieved + dates
  data = sorted(list(set(data)))
  with open(retrieved_path, "w") as fo:
    fo.write("\n".join(data))




############################################################
# MP3 handling functions
############################################################


def _fetch_and_save_mp3(url, outpath):
  if "www.bbc.co.uk" in url:
    url = _parse_bbc(url)
  if "megaphone.fm" in url:
    url = _parse_the_take(url)
  download_and_save_file(url, outpath)


def _parse_bbc(url):
  print("\tparsing BBC 5 Live url...")
  # get html
  html = _download_content(url)
  data = BeautifulSoup(html, 'html.parser') 
  # finding parent <ul> tag 
  # parent = data.find("body").find("ul") 
  links = data.findAll('a',attrs={'class':'link-complex'})
  tag = [x for x in links if "Higher quality" in x.text][0]
  href = tag["href"]
  href = f"http:{href}"
  print(f"url: {href}")
  return href


def _download_content(url):
  user_agent = {'User-agent': 'Mozilla/5.0'}
  r = requests.get(url,  headers=user_agent)
  return r.content


def _parse_the_take(url):
  print("\tparsing the take url...")
  url = re.sub("^https:.*traffic.megaphone.fm", "https://traffic.megaphone.fm", url )
  user_agent = {'User-agent': 'Mozilla/5.0'}
  r = requests.head(url,  headers=user_agent, allow_redirects=False)
  while r.status_code == 302:
    url = r.headers["Location"]
    print(f"\t302 url: {r.url}")
    r = requests.head(url, headers=user_agent, allow_redirects=False)
  if r.status_code == 200:
    print(f"\t200: url: {r.url}")
    return r.url
  else:
    print(f"Unknown status code: {r.status_code}")
    raise Exception("quitting due to unknown status code")





def download_and_save_file(url, outpath):
  user_agent = {'User-agent': 'Mozilla/5.0'}
  try:
    with requests.get(url, headers=user_agent, stream=True) as r:
        print(f"saving file to {outpath} ...")
        with open(outpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
  except Exception as e:
    msg = traceback.format_exception(*sys.exc_info())
    logging.ERROR(traceback.format_exception(*sys.exc_info()))
    print("AN ERROR OCCURRED")
    print(msg)



############################################################
# Pre-Process feed list, create list of feeds to download
############################################################

def _define_data_dirs(data_dir):
    podcast_dir = os.path.join(data_dir, "podcasts")
    os.makedirs(podcast_dir, exist_ok=True) 
    jsonl_dir = os.path.join(data_dir, "jsonl_files")
    if not os.path.exists(jsonl_dir):
      raise Exception(f"jsonl directory {jsonl_dir} does not exist")
    return podcast_dir, jsonl_dir

def _prep_feed_list(podcast_dir, jsonl_dir):
    # bbc_path = os.path.join(jsonl_dir, "bbc.jsonl")
    # the_take_path = os.path.join(jsonl_dir, "take.jsonl")
    # fouble_path = os.path.join(jsonl_dir, "fouble_feed.jsonl")
    fouble_path_1 = os.path.join(jsonl_dir, "fouble_feed_1.jsonl")
    
    raw_feed_list = _merge_jsonl(fouble_path_1)
    # raw_feed_list = _merge_jsonl(bbc_path, the_take_path)
    new_feed_list = _dictify_feed_list(raw_feed_list)
    # load any existing feed list file    
    feed_list_path = os.path.join(data_dir, "full_feed_list.json")
    if os.path.exists(feed_list_path):
      cur_feed_list = json.load(open(feed_list_path))
    else:
      cur_feed_list = {}
    # merge existing and new feed list data
    feed_list = cur_feed_list | new_feed_list

    with open(feed_list_path, "w") as fo:
      fo.write(json.dumps(feed_list))
    return feed_list


def _merge_jsonl(*paths):
  dd = defaultdict(dict) 
  for path in paths:
    lines = (json.loads(x) for x in open(path))
    for d in lines:
      timestamp = int(d["pub_date"].replace("/", ""))
      dd[timestamp] = d
  sorted_dict = dict(sorted(dd.items()))
  return list(reversed(sorted_dict.values()))


def _dictify_feed_list(feed_list):
  d = dict()
  for item in feed_list:
    k = item["pub_date"]
    d[k] = item
  return d


def _filter_feed_list(full_feed_dict, processed_feeds):
  d = {k: v for k, v in full_feed_dict.items() if not k in processed_feeds}
  return d.values()



if __name__ == "__main__":
  # data_dir = DevData().data_dir
  if len(sys.argv) != 2:
    print("ERROR. data_directory must be passed in as an argument")
    print("USAGE: \n\t$ python podcast_downloader /path/to/data_dir")
  if len(sys.argv) == 2:
    data_dir = sys.argv[1]
    if os.path.exists(data_dir):
      print(f"data_dir: {data_dir}")
      main(data_dir)
    else:
      print(f"ERROR: out directory does not exist: {data_dir}")

"""
EXAMPLE USAGE
$ python podcast_downloader.py ~/Wittertainment/data

"""
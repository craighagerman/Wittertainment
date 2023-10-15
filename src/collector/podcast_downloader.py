
# from dotenv import find_dotenv
# from dotenv import dotenv_values
# config = dotenv_values(find_dotenv())
# # NOTE: empty `.env` file was added beneath `src` directory. Ignored by gitignore rules.
import os
import sys
# sys.path.append(os.path.dirname(find_dotenv()))
# from notebooks.notebook_utils import DevData
# --------------------------------------------------
from collections import defaultdict
import json
import requests
import time


def merge_jsonl(*paths):
  dd = defaultdict(dict) 
  for path in paths:
    lines = (json.loads(x) for x in open(path))
    for d in lines:
      timestamp = int(d["pub_date"].replace("/", ""))
      dd[timestamp] = d
  sorted_dict = dict(sorted(dd.items()))
  return list(reversed(sorted_dict.values()))

def download_mp3(url):
  return requests.get(url, stream=True).content

def save_mp3(content, outpath):
  with open(outpath, "wb") as fo:
    fo.write(content)

def execute(feed_list, podcast_dir):
  # iterate over feed list, download each mp3 file to podcast dir and then sleep to be a polite scraper
  for feed in feed_list:
    date = feed["pub_date"]
    file_name = f'{date.replace("/", "_")}.mp3'
    outpath = os.path.join(podcast_dir, file_name)
    if not os.path.exists(outpath):
      print(f"processing {date} ...")
      ts = time.time()
      content = download_mp3(feed["url"])
      save_mp3(content, outpath)
      te = time.time()
      duration = te-ts
      print(f'\tduration: {float(f"{duration:.2f}")} sec')
      time.sleep(5)


def main(data_dir):
    podcast_dir = os.path.join(data_dir, "podcasts")
    os.makedirs(podcast_dir, exist_ok=True) 
  
    jsonl_dir = os.path.join(data_dir, "jsonl_files")
    if not os.path.exists(jsonl_dir):
      raise Exception(f"jsonl directory {jsonl_dir} does not exist")
    
    bbc_path = os.path.join(jsonl_dir, "bbc.jsonl")
    the_take_path = os.path.join(jsonl_dir, "take.jsonl")
    fouble_path = os.path.join(jsonl_dir, "fouble_feed.jsonl")

    feed_list = merge_jsonl(fouble_path, bbc_path, the_take_path)
    print("*** Executing ***")
    execute(feed_list, podcast_dir)
    print("*** Done ***")


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

    
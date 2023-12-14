# Imports
from dotenv import find_dotenv
from dotenv import dotenv_values
config = dotenv_values(find_dotenv())
# NOTE: empty `.env` file was added beneath `src` directory. Ignored by gitignore rules.
import os
import sys
sys.path.append(os.path.dirname(find_dotenv()))
from notebooks.notebook_utils import DevData
# --------------------------------------------------
import json
import feedparser
from datetime import datetime
from dateutil.parser import parse as dt_parse


def _get_YMD_date(date_string):
    dt = dt_parse(date_string)
    TS_FORMAT = "%Y/%m/%d"
    return dt.strftime(TS_FORMAT)


def _get_url(e):
    if "link" in e:
        return e.link
    if "links" in e:
        return e.links[0].href
    
def _parse_entry(e):
    title = e.title
    date = _get_YMD_date(e.published)
    url = _get_url(e)
    return {"pub_date": date, "url": url, "title": title}
 
def _dictify(html):
    feed = feedparser.parse(html)
    entries = feed.entries
    return [_parse_entry(e) for e in entries]


def _load_rss_file(path):
    return open(path).read()


def _write_jsonl(outdata, outpath):
    # write json-lines data to file
    print(f"writing data to {outpath}")
    with open(outpath, "w") as fo:
        fo.write("\n".join([json.dumps(x) for x in outdata] ))


def execute(inpath, outpath):
    data = _load_rss_file(inpath)
    outdata = _dictify(data)
    _write_jsonl(outdata, outpath)


def main():
    # bbc_feed_dir = os.path.join(DevData().data_dir, "rss_feeds", "bbc_5_live")
    # bbc_feed_path = os.path.join(bbc_feed_dir, "podcasts.files.bbci.co.uk_b00lvdrj.rss")
    # bbc_out_path = os.path.join(bbc_feed_dir, "bbc.jsonl")
    # execute(bbc_feed_path, bbc_out_path)
    
    the_take_feed_dir = os.path.join(DevData().data_dir, "rss_feeds", "the_take")
    the_take_feed_path = os.path.join(the_take_feed_dir, "kermodeandmayo.xml")
    the_take_feed_out_path = os.path.join(the_take_feed_dir, "take.jsonl")
    execute(the_take_feed_path, the_take_feed_out_path)


if __name__ == "__main__":
    main()

    
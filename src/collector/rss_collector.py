# Imports
from dotenv import find_dotenv
from dotenv import dotenv_values
config = dotenv_values(find_dotenv())
# NOTE: empty `.env` file was added beneath `src` directory. Ignored by gitignore rules.
import os
import sys
sys.path.append(os.path.dirname(find_dotenv()))
from notebooks.notebook_utils import DevData






def main():
    bbc_feed_path = os.path.join(DevData().data_dir, "rss_feeds", "bbc_5_live", "podcasts.files.bbci.co.uk_b00lvdrj.rss")
    the_take_feed_path = os.path.join(DevData().data_dir, "rss_feeds", "the_take", "kermodeandmayo.xml")
    fouble_feed_path = os.path.join(DevData().data_dir, "rss_feeds", "fourble_archive", "fouble_feed.jsonl")
    podcast_dir = os.path.join(DevData().raw_dir, "podcasts")
    


if __name__ == "__main__":
    main()
    print("Done")

    
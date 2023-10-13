
import feedparser
from dateutil.parser import parse as dt_parse

from feed.clean import strip_tags


def parse_summary(e):
    summary = e.get("summary", e.get("content", ""))
    s = strip_tags(summary).strip()
    return s[:220]

def get_content(e):
    return e.get("content", "")

def extract(i, e, source):
    id = i
    source = source
    title = e.title
    author = e.get("author", "")
    dt = get_datetime(e.published)
    epoch = int(dt.timestamp())
    pub_date = get_pub_date(dt)
    url = e.link,
    # image = e.media_thumbnail[0]["url"]
    summary = parse_summary(e)
    content = get_content(e)
    return {
        "id": id,
        "source": source,
        "title": title,
        "author": author,
        "epoch": epoch,
        "published": pub_date,
        "link": url,
        "description": summary,
        "content": content
    }


def get_datetime(pub_date):
    return dt_parse(pub_date)

def get_pub_date(dt):
    TS_FORMAT = "%b %d %Y, %H:%M"
    return dt.strftime(TS_FORMAT)

def parse_feed_html(html):
    feed = feedparser.parse(html)
    entries = feed.entries
    source = feed.feed.title
    status = feed.status
    if status == 200:
        norm_entries = [extract(i, e, source) for i, e in enumerate(entries)]
        # norm_entries.sort(key=lambda x: x['epoch'])
    else:
        print(f"status: {status} for feed {source}")
        return None
    return {
        "items": [
            norm_entries
        ]
    }




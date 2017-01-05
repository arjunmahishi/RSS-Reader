import feedparser
from bs4 import BeautifulSoup

RSS_feed_url = "http://teckguide.blogspot.com/feeds/posts/default?alt=rss"
atom_feed_url = "http://teckguide.blogspot.com/feeds/posts/default"

feed = feedparser.parse(atom_feed_url)

post_and_title_pair = {}

for entry in feed['entries']:
	postData = BeautifulSoup(entry['summary'], 'html.parser').text
	post_and_title_pair[entry['title']] = postData
	# print postData
	# print

print post_and_title_pair.keys()
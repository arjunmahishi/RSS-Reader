import feedparser

RSS_feed_url = "http://teckguide.blogspot.com/feeds/posts/default?alt=rss"
atom_feed_url = "http://teckguide.blogspot.com/feeds/posts/default"

feed = feedparser.parse(atom_feed_url)

for entry in feed['entries']:
	print entry['title']
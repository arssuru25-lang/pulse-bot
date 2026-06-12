import feedparser

feeds = {
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "Google News": "https://news.google.com/rss"
}

def get_news():
    news_items = []

    for source, url in feeds.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:1]:
            news_items.append({
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", "Unknown")
            })

    return news_items
def create_html(news_items):
    html = "<h2>Top Headlines</h2><ul>"

    for item in news_items:
        html += f"""
        <li>
        <b>{item['source']}</b><br>
        {item['title']}<br>
        Published: {item['published']}<br>
        <a href="{item['link']}">Read more</a>
        </li><br>
        """

    html += "</ul>"

    return html
from email_alert import send_alert

if __name__ == "__main__":
    news_items = get_news()
    html_content = create_html(news_items)

    send_alert(
        "Daily News Summary",
        html_content
    )

    print("News email sent successfully!")
    
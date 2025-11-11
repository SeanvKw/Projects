from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.find_all(name="span", class_="titleline")
links = soup.select(selector="span.titleline a")
article_text = []
article_links = []

for article_tag in title_tag:
    text = article_tag.get_text()
    article_text.append(text)
for article_tag in links:
    link = article_tag.get("href")
    article_links.append(link)


article_upvote = [int(score.get_text().split(" points")[0]) for score
                  in soup.find_all(name="span", class_="score")]
largest_upvote_num = max(article_upvote)
largest_index = article_upvote.index(largest_upvote_num)
print(article_text[largest_index + 1])
# + 23 to adjust for the index shift, im not experienced with web scraping to use lambda or other methods
print(article_links[largest_index + 23])
print(largest_upvote_num)
# print(article_text)
# print(article_links)
# print(article_upvote)

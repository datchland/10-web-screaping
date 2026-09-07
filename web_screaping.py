import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# latest_news = soup.find("div",attrs={"class":"medium-widget blog-widget"})

# titles = latest_news.find_all("a")
# dates = latest_news.find_all("time")

# for title in titles:
#     print(title.get_text("a"))
#     print(title.get("href"))
#     print("-"*30)

# for date in dates:
#     print(date.get_text())
#     print("-"*30)

# usepy= soup.find("div",attrs={"class":"shrubbery"})
# titles = usepy.find_all("h")
# sub_titles = usepy.find_all("p")
# lists= usepy.find_all("ul")

# for title in titles:
#     print(title.get_text("h"))
#     print("-"*30)
# for sub_title in sub_titles:
#     print(sub_title.get_text("h"))
#     print("-"*30)
# for list in lists:
#     print(list.get_text("h"))
#     print("-"*30)
titles_event = soup.select("medium-widget.event-widget.last ul.menu a")
dates_event = soup.select("medium-widget.event-widget.last ul.menu time")

for i in range(len(titles_event)):
    print(titles_event[i].get_text())
    print(dates_event[i].get_text())
    print("-"*30)



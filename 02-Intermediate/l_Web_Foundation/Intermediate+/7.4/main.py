from bs4 import BeautifulSoup
# import lxml

with open("02-Intermediate/l_Web_Foundation/Intermediate+/7.4/website.html") as file:
    content = file.read()


soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)  # type: ignore

# print(soup.p)


all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)  # type: ignore

company_url = soup.select_one(selector="p a")
print(company_url)  # type: ignore

name = soup.select_one(selector="#name")
print(name)  # type: ignore

headings = soup.select(selector=".heading")
for heading in headings:
    print(heading)  # type: ignore

from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
anchor_tags = soup.find_all(name='a')
print('--------------------------------------------')
for tag in anchor_tags:
    print(tag.get('href'))

heading = soup.find(name='h1', id='name')
print(heading)
print('--------------------------------------------')

classes = soup.find(name='h3', class_='heading')
print(classes.get_text())
print('--------------------------------------------')

name = soup.select_one(selector='#name')
print(name)
print('--------------------------------------------')

heading = soup.select(selector='.heading')
print(heading)
# get_text
# findall(name)
# you can iterate through the findall output (list)
# find(name, id) gets the first occurrence of the thing that matches the name and id
# select_one(selector) allows you to pick stuff by its unique html tag combinations

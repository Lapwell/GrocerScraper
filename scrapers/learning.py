from requests_html import HTMLSession
import csv

url = 'https://github.com/Lapwell?tab=repositories'
session = HTMLSession()
r = session.get(url)

p_container = r.html.find('#user-repositories-list', first=True)
list_p_container = p_container.find('li')

sheet = [['Name ', 'Lang ', 'Date ', 'Index']]
loop = 0
for item in list_p_container:
    element = item.text.split('\n')
    if 'Public' in element[0] or 'Public' in element[1] or 'Public' in element[2] or 'Public' in element[-1]:
        for i in element:
            index = element.index(i)
            element[index] = element[index].replace('Public', '')
    if 'Updated' in element[0] or 'Updated' in element[1] or 'Updated' in element[2] or 'Updated' in element[-1]:
        for i in element:
            index = element.index(i)
            element[index] = element[index].replace('Updated', '')
    if len(element[1]) > 10:
        del element[1]
    name = element[0]
    lang = element[2]
    date = element[1]
    sheet.append([name, date, lang, loop])
    loop += 1

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(sheet)

  from bs4 import BeautifulSoup
import PySimpleGUI as gui
import requests

layout =[[gui.Text("Enter the year: ")],
         [gui.Input(key='year',size=(50,1))],
         [gui.Button("OK")]]
window = gui.Window("YEAR",layout,size=(200,200))
while True:
    event, values = window.read()
    year = values['year']
    if event=="OK" or event == gui.WIN_CLOSED:
        break


url = r"https://www.imdb.com/search/title/?release_date="+year+","+year+"&title_type=feature"
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

article = soup.find('div',attrs={'class':'article'}).find('h1')
print(article.contents[0])
print("\n")
content = soup.findAll('div',attrs={'class':'lister-item mode-advanced'})

for i in content:
        header = i.findChildren('h3',attrs={'class':'lister-item-header'})
        #print(header)
        for j in header:
                movie = header[0].findChildren('a')
                print(movie[0].string)
        
window.close()

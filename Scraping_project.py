import requests
from bs4 import BeautifulSoup
import textwrap
url = "https://quotes.toscrape.com/"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")
for quote in soup.find_all("div", class_="quote"):
    texto = quote.find("span", class_="text").text
    autor = quote.find("small", class_="author").text
    tags = []
    for tag in quote.find_all("a", class_="tag"):
        tags.append(tag.text)
    print("Cita:")
    print(textwrap.fill(texto, width=60))
    print("Autor:", autor)
    print("Tags:", ", ".join(tags))
    print("-" * 40)


La pagina que le hicimos scraping es https://quotes.toscrape.com

Muestra de los datos que estas capturando en el Scraaping:

“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
“Try not to become a man of success. Rather become a man of value.”
“It is better to be hated for what you are than to be loved for what you are not.”
“I have not failed. I've just found 10,000 ways that won't work.”
“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
“A day without sunshine is like, you know, night.”

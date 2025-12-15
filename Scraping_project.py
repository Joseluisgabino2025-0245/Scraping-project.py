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

    link = url + quote.find("a")["href"]

    for tag in quote.find_all("a", class_="tag"):
        tags.append(tag.text)

    print("Cita:")
    print(textwrap.fill(texto, width=60))
    print("Autor:", autor)
    print("Enlace:", link)
    print("Tags:", ", ".join(tags))
    print("-" * 40)


La pagina que mi pareja de grupo y yo le hicimos scraping es https://quotes.toscrape.com   

Muestra de los datos que estas capturando en el Scraaping:

Cita:
“The world as we have created it is a process of our
thinking. It cannot be changed without changing our
thinking.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: change, deep-thoughts, thinking, world
----------------------------------------
Cita:
“It is our choices, Harry, that show what we truly are, far
more than our abilities.”
Autor: J.K. Rowling
Enlace: https://quotes.toscrape.com//author/J-K-Rowling
Tags: abilities, choices
----------------------------------------
Cita:
“There are only two ways to live your life. One is as though
nothing is a miracle. The other is as though everything is a
miracle.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: inspirational, life, live, miracle, miracles
----------------------------------------
Cita:
“The person, be it gentleman or lady, who has not pleasure
in a good novel, must be intolerably stupid.”
Autor: Jane Austen
Enlace: https://quotes.toscrape.com//author/Jane-Austen
Tags: aliteracy, books, classic, humor
----------------------------------------
Cita:
“Imperfection is beauty, madness is genius and it's better
to be absolutely ridiculous than absolutely boring.”
Autor: Marilyn Monroe
Enlace: https://quotes.toscrape.com//author/Marilyn-Monroe
Tags: be-yourself, inspirational
----------------------------------------
Cita:
“Try not to become a man of success. Rather become a man of
value.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: adulthood, success, value
----------------------------------------
Cita:
“It is better to be hated for what you are than to be loved
for what you are not.”
Autor: André Gide
Enlace: https://quotes.toscrape.com//author/Andre-Gide
Tags: life, love
----------------------------------------
Cita:
“I have not failed. I've just found 10,000 ways that won't
work.”
Autor: Thomas A. Edison
Enlace: https://quotes.toscrape.com//author/Thomas-A-Edison
Tags: edison, failure, inspirational, paraphrased
----------------------------------------
Cita:
“A woman is like a tea bag; you never know how strong it is
until it's in hot water.”
Autor: Eleanor Roosevelt
Enlace: https://quotes.toscrape.com//author/Eleanor-Roosevelt
Tags: misattributed-eleanor-roosevelt
----------------------------------------
Cita:
“A day without sunshine is like, you know, night.”
Autor: Steve Martin
Enlace: https://quotes.toscrape.com//author/Steve-Martin
Tags: humor, obvious, simile
----------------------------------------
PS C:\Users\Asus\OneDrive - Universidad Adventista Dominicana\Documentos\py> & C:/Users/Asus/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/Asus/OneDrive - Universidad Adventista Dominicana/Documentos/py/scraping_project.py"      
Cita:
“The world as we have created it is a process of our
thinking. It cannot be changed without changing our
thinking.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: change, deep-thoughts, thinking, world
----------------------------------------
Cita:
“It is our choices, Harry, that show what we truly are, far
more than our abilities.”
Autor: J.K. Rowling
Enlace: https://quotes.toscrape.com//author/J-K-Rowling
Tags: abilities, choices
----------------------------------------
Cita:
“There are only two ways to live your life. One is as though
nothing is a miracle. The other is as though everything is a
miracle.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: inspirational, life, live, miracle, miracles
----------------------------------------
Cita:
“The person, be it gentleman or lady, who has not pleasure
in a good novel, must be intolerably stupid.”
Autor: Jane Austen
Enlace: https://quotes.toscrape.com//author/Jane-Austen
Tags: aliteracy, books, classic, humor
----------------------------------------
Cita:
“Imperfection is beauty, madness is genius and it's better
to be absolutely ridiculous than absolutely boring.”
Autor: Marilyn Monroe
Enlace: https://quotes.toscrape.com//author/Marilyn-Monroe
Tags: be-yourself, inspirational
----------------------------------------
Cita:
“Try not to become a man of success. Rather become a man of
value.”
Autor: Albert Einstein
Enlace: https://quotes.toscrape.com//author/Albert-Einstein
Tags: adulthood, success, value
----------------------------------------
Cita:
“It is better to be hated for what you are than to be loved
for what you are not.”
Autor: André Gide
Enlace: https://quotes.toscrape.com//author/Andre-Gide
Tags: life, love
----------------------------------------
Cita:
“I have not failed. I've just found 10,000 ways that won't
work.”
Autor: Thomas A. Edison
Enlace: https://quotes.toscrape.com//author/Thomas-A-Edison
Tags: edison, failure, inspirational, paraphrased
----------------------------------------
Cita:
“A woman is like a tea bag; you never know how strong it is
until it's in hot water.”
Autor: Eleanor Roosevelt
Enlace: https://quotes.toscrape.com//author/Eleanor-Roosevelt
Tags: misattributed-eleanor-roosevelt
----------------------------------------
Cita:
“A day without sunshine is like, you know, night.”
Autor: Steve Martin
Enlace: https://quotes.toscrape.com//author/Steve-Martin
Tags: humor, obvious, simile
----------------------------------------

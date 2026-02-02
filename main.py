import requests
from bs4 import BeautifulSoup

url = "https://www.sneak-kino.de/sneak-prognose/"


def clean_movie_name(name):
    return name.removesuffix(" (auch OV)")


def get_movie_names():
    movie_names = list()
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        entry = soup.find("div", class_="entry")

        divs = entry.find_all("div")
        for div in divs:
            if div.find("h2") and "Sneak-Prognose für" in div.find("h2").text:
                li = div.find_all("li")
                for i in li:
                    movie_names.append(clean_movie_name(i.text))
                break
    else:
        print(f"Request failed with status code: {response.status_code}")

    return movie_names


if __name__ == "__main__":
    print(get_movie_names())

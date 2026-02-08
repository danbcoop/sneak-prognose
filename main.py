import requests
from bs4 import BeautifulSoup
from datetime import date

url = "https://www.sneak-kino.de/sneak-prognose/"


def clean_movie_name(name):
    return name.removesuffix(" (auch OV)")


def get_movie_names():
    movie_names = list()
    uplaod = date.min

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        entry = soup.find("div", class_="entry")

        divs = entry.find_all("div")
        for div in divs:
            if div.find("p") and "Letztes Update" in div.find("p").text:
                s = div.find("p").text
                date_string = s[s.find("Update:"):].split(":")[1].split(",")[0].strip()
                update = date.strptime(f"{date_string}", "%d.%m.%Y")
            if div.find("h2") and "Sneak-Prognose für" in div.find("h2").text:
                print(div.find("h2").text)
                li = div.find_all("li")
                for i in li:
                    movie_names.append(clean_movie_name(i.text))
                break
    else:
        print(f"Request failed with status code: {response.status_code}")

    return (movie_names, update)


if __name__ == "__main__":
    (movie_names, update) = get_movie_names()
    print(update)
    for name in movie_names:
        print(name)


from bs4 import BeautifulSoup
from urllib.request import urlopen


def main():
    url = "https://www.ufv.ca/arfiles/includes/202401-timetable-with-changes.htm"
    page = urlopen(url)

    html = page.read().decode("latin-1")
    soup = BeautifulSoup(html, "html.parser")

    spans = soup.find_all("span")
    for row in spans:
        print(row)


if __name__ == "__main__":
    main()
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def main():
    url = "https://www.ufv.ca/arfiles/includes/202401-timetable-with-changes.htm"
    page = urlopen(url)

    html = page.read().decode("latin-1")
    soup = BeautifulSoup(html, "html.parser")

    spans = soup.find_all("span")

    arr = []
    for row in spans:
        row = str(row)
        course = re.findall(r'[A-Z][A-Z]\s\d\d\d', row)
        name = re.findall(r'(?<=\t)[A-Z].+\s[A-Z].+(?=[^A-Z])', row)
        print(name)


if __name__ == "__main__":
    main()
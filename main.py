from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def main():
    url = "https://www.ufv.ca/arfiles/includes/202401-timetable-with-changes.htm"
    page = urlopen(url)

    html = page.read().decode("latin-1")
    soup = BeautifulSoup(html, "html.parser")

    splits = re.split(r'-----------------------------------------------------------------------------------------------------------------------------------', str(soup))
    for row in splits:
        row_parser(row)
        
            
def row_parser(row):

    row = str(row)
'''
    course = re.findall(r'[A-Z]+\s\d\d\d[A-Z]*', row)
    if (len(course) != 0):
        if (course[0].startswith("ABA") 
            or course[0].startswith("ABB") 
            or course[0].startswith("ABC") 
            or course[0].startswith("ABD")
            or course[0].startswith("ABE")
            or course[0].startswith("ABF")
            or course[0].startswith("ABH")
            or course[0].startswith("CEPA")
            or course[0].startswith("CEPV")):
            course = []
        else:
            course = course[0]    
    name = re.findall(r'(?<=\d\d\d\s\t)[A-Z].+(?=\s\d\.\d)', row)
    credits = re.findall(r'(?<=\s)[ 123456789]\.[05]', row)
    if (len(credits) == 0):
        credits = "No Credits"
    elif (len(credits) >= 1):
        credits = credits[0]

        '''         


if __name__ == "__main__":
    main()
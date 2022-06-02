'''
    Date:           2022-04-20
    Name:           CBSE Schools scraper
    Author:         Shawan Mandal
    Description:    This script helps in scraping the cbseschool's website and write each school's data into a csv file. 
'''

import requests, csv, io
from bs4 import BeautifulSoup

fields = ['Name', 'Address', 'STD Code', 'Office Phone', 'E-mail', 'Website', 'Principal/Head of Institution', 'School Status']
ignored_fields = ['Affiliate ID', 'PIN Code', 'Fax', 'Residence Phone', 'Foundation Year', 'Managing Trust/Society/Committee']

def handleRequests(query, token='', cookie=''):
    '''Returns HTML document'''

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    try:
        request = requests.get(query, headers=headers, cookies=cookie, allow_redirects=False)
        return request.text
    except Exception:
        raise ConnectionError("Error occured while fetching data from the web, please try checking the internet connection.")

def getSoup(data):
    '''Returns parsed Soup Object from html text'''
    return BeautifulSoup(data, "html.parser")

def scrape(link, file_name='cbse_schools'):
    writer = io.open(f'{file_name}.csv', 'a', encoding='utf-8')
    csvwriter = csv.writer(writer)
    csvwriter.writerow(fields)

    data = handleRequests(link)
    soup = getSoup(data)

    results = soup.findAll('div', attrs={'class': 'catbox'})
    print(f'Found a total of {len(results)} schools on this page \n')
    count = 1
    total = len(results)
    for each in results:
        page = handleRequests(each.p.a['href'])
        page_content = getSoup(page)

        table = page_content.find('div', attrs={'id': 'responsivetable'}).table
        elements = table.find_all('tr', attrs={'class': None})
        _name = table.find('tr', attrs={'class': 'tableheading'})
        name = _name.find_all('td')[-1]
        values = {}
        values['Name'] = name.get_text()

        for each_row in elements:
            heading = each_row.find(attrs={'class': 'field'}).get_text()
            value = each_row.find(attrs={'class': None}).get_text()
            if heading in ignored_fields:
                pass
            else:
                values[heading] = value
                #values.append(value)
                #print(heading, value)
        entries = []
        for every_field in fields:
            try:
                entries.append(values[every_field])
            except:
                entries.append("  ")

        csvwriter.writerow(entries)
        print(f'Scraping: {count}/{total} completed', end='\r')
        count += 1

    print(f'Completed: {count - 1}/{total}')
    input("Scraping completed successfully, press any key to exit...")



# Call the function 'scrape()' with the page link, optionally you can pass the file name for saving the file with a different name
# The script will automatically get the list of the schools on a particular page and than visit each page individually, 
# it will scrape the data present on that page and than write them in a csv file in a well-organised manner
#
# USAGE
# scrape('webpage_link', 'filename')

url = 'https://www.cbseschool.org/schools/new-delhi/'

scrape(url, 'New_Delhi') # A CSV file with name New_Delhi.csv will be generated

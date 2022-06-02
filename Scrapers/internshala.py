'''
    Date:        2022-06-03
    Author:      Shawan Mandal
    Description: Scrapes data out of Internshala's website and stores it into a corresponding csv file based on user's input.
'''


import requests, csv, io, re
from bs4 import BeautifulSoup
import urllib.parse

fields = ['Name', 'Company Name', 'Location', 'Start Date', 'Duration', 'Apply by', 'Stipend', 'Number of Openings', 'Website Link', 'Internship Details']

def handleRequests(query):
    '''Returns HTML document'''

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    try:
        request = requests.get(query, headers=headers, allow_redirects=False)
        return request.text
    except Exception:
        raise ConnectionError("Error occured while fetching data from the web, please try checking the internet connection.")

def getSoup(data):
    '''Returns parsed Soup Object from html text'''
    return BeautifulSoup(data, "html.parser")

def slugify(s, separator='-'):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', separator, s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

def scrape(link, file_name='internshala_internships', page=1):
    writer = io.open(f'{file_name}.csv', 'a', encoding='utf-8')
    csvwriter = csv.writer(writer)
    csvwriter.writerow(fields)

    data = handleRequests(link)
    soup = getSoup(data)

    results = soup.find('div', attrs={'id': 'internship_list_container_' + str(page)}).find_all('div', attrs={'class': 'individual_internship'})
    print(f'Found a total of {len(results)} schools on this page \n')
    count = 1
    total = len(results)
    entries = []
    for each in results:
        link = each.find('div', attrs={'class': 'button_container'}).a['href']

        page = handleRequests('https://internshala.com' + link);
        page_content = getSoup(page)

        details_container = page_content.find('div', attrs={'class': 'detail_view'})
        internship_meta = details_container.find('div', attrs={'class': 'individual_internship'}).find('div', attrs={'class': 'internship_meta'})
        individual_internship_details = internship_meta.find('div', attrs={'class': 'internship_other_details_container'})
        internship_details_container = details_container.find('div', attrs={'class': 'internship_details'})


        internship_name = internship_meta.find('span', attrs={'class': 'profile_on_detail_page'})
        company_name = internship_meta.find('div', attrs={'class': 'company_name'})

        company_location = internship_meta.find('div', attrs={'class': 'individual_internship_details'}).find('div', attrs={'id': 'location_names'})
        stipend = individual_internship_details.find('span', attrs={'class': 'stipend'})
        internship_details = internship_details_container.find_all('div')
        website_link = internship_details_container.find('div', attrs={'class': 'website_link'})
        
        internship_start_date = individual_internship_details.find('div', attrs={'id': 'start-date-first'})
        internship_duration = individual_internship_details.find_all('div', attrs={'class': 'other_detail_item_row'})[0].find_all('div', attrs={'class': 'other_detail_item'})[1].find('div', attrs={'class': 'item_body'})
        internship_applyby_date = individual_internship_details.find('div', attrs={'class': 'apply_by'}).find('div', attrs={'class': 'item_body'})

        number_of_openings = internship_details_container.find_all('div', attrs={'class': 'text-container'})[-1]
        
        INTERNSHIP = []

        if (internship_name):
            INTERNSHIP.append(internship_name.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (company_name):
            INTERNSHIP.append(company_name.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (company_location):
            INTERNSHIP.append(company_location.span.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (internship_start_date):
            INTERNSHIP.append(internship_start_date.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (internship_duration):
            INTERNSHIP.append(internship_duration.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (internship_applyby_date):
            INTERNSHIP.append(internship_applyby_date.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (stipend):
            INTERNSHIP.append(stipend.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (number_of_openings):
            INTERNSHIP.append(number_of_openings.get_text(" ", strip=True))
        else:
            INTERNSHIP.append('Not Available')

        if (website_link):
            INTERNSHIP.append(website_link.a['href'])
        else:
            INTERNSHIP.append('Not Available')

        if (internship_details):
            details = ''
            for divs in internship_details:
                details += divs.get_text(" ", strip=True) + '\n\n'

            INTERNSHIP.append(details)
        else:
            INTERNSHIP.append('Not Available')

        csvwriter.writerow(INTERNSHIP)

        print(f'Scraping: {count}/{total} completed', end='\r')
        count += 1

    print(f'Completed: {count - 1}/{total}')
    input("Scraping completed successfully, press any key to exit...")

user_input = input("Enter search params: ")
query = urllib.parse.quote(user_input)
slugified_user_input = slugify(user_input)

home_page = handleRequests('https://internshala.com/internships/' + query + '-internship');
home_page_content = getSoup(home_page)
total_pages = home_page_content.find('div', attrs={'id': 'pagination'}).find('div', attrs={'class': 'page_number'}).find('span', attrs={'id': 'total_pages'}).get_text(" ", strip=True)
total_pages = int(total_pages)
print(f'Found a total of {total_pages} pages')

for x in range(total_pages + 1):
    page = x + 1
    url = 'https://internshala.com/internships/' + query +'/page-' + str(page)
    scrape(url, slugified_user_input + '_' + str(page), page)


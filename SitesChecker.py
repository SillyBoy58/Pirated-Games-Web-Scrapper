import requests
from bs4 import BeautifulSoup

def sendRequest(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def FitGirl_Repacks(gameName):
    url = f"https://fitgirl-repacks.site/?s={gameName}"
        
    soup = sendRequest(url)
    headers = soup.find_all('header', {'class': 'entry-header'})

    if headers:
        print("Results: ")

        for i, header in enumerate(headers, start = 1):
            category = header.find('a', {'rel':'category tag'})
            if category:
                categoryName = category.get_text()
            elif category == 'Updates Digest':
                continue
            else:
                categoryName = "No category"

            title = header.find('a', {'rel':'bookmark'})
            if title:
                titleName = title.get_text()            
                href = title.get('href')
            else:
                titleName = "No title"

            print(f"{i}.\n\nCategory: {categoryName.strip()},\nTitle: {titleName.strip()},\nLink:{href}.\n")
    else:
        print("No results found.")

def SteamRIP(gameName):
    url = f"https://steamrip.com/?s={gameName}"

    soup = sendRequest(url)
    titles = soup.find_all('a', {'class': 'all-over-thumb-link'})

    if titles:
        print("Results: ")

        for i, title in enumerate(titles, start = 1):
            tag = title.parent.find('span', {'class':'tagmetafield'})
            if tag:
                tagName = tag.get_text()
            else:
                tagName = "No tag"

            href = title.get('href')

            title = title.find('span', {'class':'screen-reader-text'})
            if title:
                titleName = title.get_text()
            else:
                titleName = "No title"

            print(f"{i}.\n\nTag: {tagName.strip()};\nTitle: {titleName.strip()};\nLink: https://steamrip.com/{href}.\n")
    else:
        print("No results found.")

def AnkerGames(gameName):
    url = f"https://ankergames.net/search/{gameName}"

    soup = sendRequest(url)
    divs = soup.find_all('div', {'class': 'relative group cursor-pointer'})

    if divs:
        print("Results: ")

        for i, div in enumerate(divs, start = 1):
            tag = div.find('span', {'class':'text-[10px] sm:text-xs text-white'})
            if tag:
                tagName = tag.get_text()
            else:
                tagName = "No tag"

            href = div.find('a', {'class': 'absolute inset-0 flex items-center justify-center focus:outline-none focus-visible:ring-2 focus-visible:ring-green-500'})
            if href:
                href = href.get('href')
            else:
                href = "No link"

            div = div.find('h3', {'class':'text-white font-medium text-sm sm:text-md leading-tight line-clamp-1 translate-y-8 group-hover:translate-y-0 transition-transform duration-300'})
            if div:
                titleName = div.get_text()
            else:
                titleName = "No title"

            print(f"{i}.\n\nTag: {tagName.strip()};\nTitle: {titleName.strip()};\nLink: {href}.\n")
    else:
        print("No results found.")
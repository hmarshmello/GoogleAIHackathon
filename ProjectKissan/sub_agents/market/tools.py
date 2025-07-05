def datetool():
    from datetime import date

    return date.today().strftime("%d-%b-%Y")


def ScrapeWebsiteTool(url: str, key: int):
    name: str = "scrape_website"
    description: str = "Scrapes the content from a website. Use this to gather information from a webpage. Input should be a valid URL."
    try:
        from bs4 import BeautifulSoup
        import requests

        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")
        trendtable = soup.get_text(separator=" ")
        keyinfo = soup.find_all("option")
        if key == 11:
            return str(keyinfo)
        else:
            return trendtable

    except Exception as e:
        return f"Error scraping website: {e}"

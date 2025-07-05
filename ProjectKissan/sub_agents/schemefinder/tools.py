def datetool():
    from datetime import date

    return date.today().strftime("%d-%b-%Y")


def ScrapeWebsiteTool(
    url: str,  # optional date
    datee: None,  # Optional date parameter to specify the date for market prices
):
    name: str = "scrape_website"
    description: str = "Scrapes the content from a website. Use this to gather information from a webpage. Input should be a valid URL."
    try:
        from bs4 import BeautifulSoup
        import requests
        from datetime import date

        if datee is not None:
            # If a date is provided, format it to append to the URL
            formatted_date = datee.strftime("%d-%b-%Y")
            url = f"{url}/{formatted_date}"
        else:
            # If no date is provided, use the current date
            formatted_date = date.today().strftime("%d-%b-%Y")
            url = f"{url}/{formatted_date}"
        # Make the HTTP request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator=" ")
        return text

    except Exception as e:
        return f"Error scraping website: {e}"

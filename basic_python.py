import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.imdb.com/chart/top'
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            " AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/109.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = soup.select('td.titleColumn')
    years = soup.select('span.secondaryInfo')
    print("DEBUG", movies)
    top_25 = []
    for i in range(25):
        movie = movies[i].a.text
        year = years[i].text.strip('()')
        top_25.append((movie, year))
    
    for i, (movie, year) in enumerate(top_25, start=1):
        print(f"{i}. {movie} ({year})")

if __name__ == "__main__":
    main()
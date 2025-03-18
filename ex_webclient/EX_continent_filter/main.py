from fetcher import ContinentFetcher
from filter import ContinentFilter

def main():
    fetcher = ContinentFetcher()
    continents = fetcher.fetch_continents()
    if not continents:
        print("No continents found or API request failed.")
        return
    most_populated_continent = ContinentFilter.find_most_populated_continent(continents)
    print(f"Most populated continent: {most_populated_continent}")
    
if __name__ == "__main__":
    main()
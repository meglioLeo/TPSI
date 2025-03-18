from filter import CompanyFilter
from fetcher import CompanyFetcher

def main():
    fetcher = CompanyFetcher()
    companies = fetcher.fetch_companies()
    if not companies:
        print("No companies found or API request failed.")
        return
    filtered_companies = CompanyFilter.filter_by_employee_count(companies)
    print("Companies with more than 2000 employees:")
    for company in filtered_companies:
        print(f"- {company.name} ({company.employeeCount})")
        
if __name__ == "__main__":
    main()
from config import DEFAULT_STATE_FILTER

class CompanyFilter:
    @staticmethod
    def filter_by_employee_count(companies, DEFAULT_STATE_FILTER):
        filtered_companies = []
        for company in companies:
            if company.employee_count > DEFAULT_STATE_FILTER:
                filtered_companies.append(company)
        return filtered_companies
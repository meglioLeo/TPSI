from config import DEFAULT_EMPLOYEE_COUNT_FILTER

class CompanyFilter:
    @staticmethod
    def filter_by_employee_count(companies, employee_count=DEFAULT_EMPLOYEE_COUNT_FILTER):
        filtered_companies = []
        for company in companies:
            if company.employeeCount > DEFAULT_EMPLOYEE_COUNT_FILTER:
                filtered_companies.append(company)
        return filtered_companies
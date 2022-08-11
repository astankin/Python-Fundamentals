def printing(company_dict):
    for company, employers in company_dict.items():
        print(f"{company}")
        for id in employers:
            print(f"-- {id}")


def company_info():
    companies = {}
    while True:
        data = input()
        if data == "End":
            break
        company_name, employee_id = data.split(" -> ")
        if company_name not in companies:
            companies[company_name] = [employee_id]
        else:
            if employee_id not in companies[company_name]:
                companies[company_name].append(employee_id)
    return companies


companies = company_info()
printing(companies)

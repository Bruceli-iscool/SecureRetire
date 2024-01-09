
def working_years(years, retirementyears):
    age = int(years)
    ret = int(retirementyears)
    work_years = ret - age
    return int(work_years)

def final_income(income, work_years):
    income = int(income)
    workable_years = int(work_years)
    total_income = workable_years * income
    return total_income

def expenses(expensesf, yearsaterretirement, work_years):
    expensesf = int(expensesf)
    yearsaterretirement = int(yearsaterretirement)
    int(work_years)
    expense_before = expensesf * (1.02**yearsaterretirement)
    expenses_work = expense_before + expensesf * (1.02 **work_years)
    return int(expenses_work)
def social_security(eachyear, retirementyears):
    eachyear = int(eachyear)
    retirementyears = int(retirementyears)
    social = final_income + (eachyear * retirementyears)
    return int(social)

def final_amount(social_security, expenses):
    final = social_security - expenses
    return final

def safe_ornot(final):
    if int(final) > 1000:
        print('You have enough money\n' + 'Your Final Amount is: ' + final)

    else:
        print('You don\'t have enough money\n' + 'Your Final Amount is: '+ final)
# formula r - a = w w x i = f, f + s = k - e

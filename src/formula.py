
def working_years(years, retirementyears):
    age = int(years)
    ret = int(retirementyears)
    work_years = ret - age
    return int(work_years)

def final_income(income):
    total_income = working_years * income
    return int(total_income)

def expenses(expensesf, yearsaterretirement):
    expense_before = int(expensesf) * (1.02**yearsaterretirement)
    expenses_work = expense_before + expensesf * (1.02 **working_years)
    return int(expenses_work)
def social_security(eachyear, retirementyears):
    social = final_income + (int(eachyear) * int(retirementyears))
    return int(social)

def final_amount():
    final = int(social_security) - int(expenses)
    return final

def safe_ornot():
    if int(final_amount) > 1000:
        print('You have enough money\n' + 'Your Final Amount is: ' + final_amount)

    else:
        print('You don\'t have enough money\n' + 'Your Final Amount is: '+ final_amount )
# formula r - a = w w x i = f, f + s = k - e

import formula

years_work = input('how old are you? \n')
int(years_work)
when_retire = input('When are you going to retire? \n')
int(when_retire)
years = formula.working_years(years_work, when_retire)
income = input('How much do you make every year? \n')
int(income)
final = formula.final_income(income)
spend = input('How much do you spend every year?\n')
retyears = input('How long do you think you are going to live?\n')
exp = formula.expenses(spend, retyears)
soc = input('How much do you recieve in social security?')
socspend = formula.social_security(soc, retyears)
FIN = formula.final_amount()
print('This is how much you would spend in your life: \n'+ spend)
formula.safe_ornot()
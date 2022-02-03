import numpy as np

def cli_terminal():
    # I earn 10% each year means 0.1
    target_investment = int(input("Set your target in usd, example (100000)    : "))
    target_years =  int(input("How many years do you want take  (15) : "))
    initial_investment =  int(input("What is your initial capital (15000) : "))
    investment_gain_rate_annual =  float(input("How much is your annual gain rate (0.05)  : "))
    time_for_growth(target_investment=target_investment,target_years=target_years,
    initial_investment=initial_investment,investment_gain_rate_annual=investment_gain_rate_annual)
    
def time_for_growth(initial_investment=0,target_investment=100000,target_years=10,investment_gain_rate_annual=0.05):
    investment_rate_monthly = (1+investment_gain_rate_annual)**(1/12)  - 1   
    required_monthly_investment = np.pmt(rate=investment_rate_monthly,  nper=12*target_years , pv=initial_investment,fv=-target_investment)
    print("You will have to invest " + str(round(required_monthly_investment, 2)) + "USD per month to amass "+str(target_investment)+"USD over ",target_years," years")


if __name__ =='__main__':
	cli_terminal()

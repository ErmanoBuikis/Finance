import numpy as np

# Set the annual investment return to 7%
investment_rate_annual = 0.5

# Calculate the monthly investment return
investment_rate_monthly = (1+investment_rate_annual)**(1/12) - 1

# Calculate your required monthly investment to amass $1M
required_investment_monthly = np.pmt(rate=investment_rate_monthly, nper=forecast_months, pv=0, fv=-1000000)
print("You will have to invest $" + str(round(required_investment_monthly, 2)) + " per month to amass $1M over 15 years")




#Your projections show that you can accumulate over $700,000 in just 15 years by following a strict budget and growing your salary steadily over time.

#But you want to be a millionaire in 15 years, retire young, sip margaritas and travel for the rest of your life. In order to do that, you're going to need to invest.

#Remember the .pmt() function from numpy? You can use this function to calculate how much you need to save each month in order to accumulate your desired wealth over time.

#You still have a lot to learn about the stock market, but your financial advisor told you that you can earn anywhere from 5-10% per year on your capital on average by investing in a low cost index fund.

#You know that the stock market doesn't always go up, but you will assume a modest 7% return per year, which has been the average annual return in the US stock market from 1950-2009.

#The forecast_months variable from the previous exercise is available.

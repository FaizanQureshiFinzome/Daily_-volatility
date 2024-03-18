import math
#import math library for math calculations

#close_prices are the data that was converted from .xlsx file to a python data type which is list
# close_ prices will help us to find daily returns
close_prices = [
    18165.35, 18107.85, 18027.65, 18118.55, 18118.3, 17891.95, 17604.35, 17648.95, 17662.15, 17616.3,
    17610.4, 17854.05, 17764.6, 17721.5, 17871.7, 17893.45, 17856.5, 17770.9, 17929.85, 18015.85, 18035.85,
    17944.2, 17844.6, 17826.7, 17554.3, 17511.25, 17465.8, 17392.7, 17303.95, 17450.9, 17321.9, 17594.35,
    17711.45, 17754.4, 17589.6, 17412.9, 17154.3, 17043.3, 16972.15, 16985.6, 17100.05, 16988.4, 17107.5,
    17151.9, 17076.9, 16945.05, 16985.7, 16951.7, 17080.7, 17359.75, 17398.05, 17557.05, 17599.15, 17624.05,
    17722.3, 17812.4, 17828, 17706.85, 17660.15, 17618.75, 17624.45, 17624.05, 17743.4, 17769.25, 17813.6,
    17915.05, 18065, 18147.65, 18089.85, 18255.8, 18069, 18264.4, 18265.95, 18315.1, 18297, 18314.8, 18398.85,
    18286.5, 18181.75, 18129.95, 18203.4, 18314.4, 18348, 18285.4, 18321.15, 18499.35, 18598.65, 18633.85,
    18534.4, 18487.75, 18534.1, 18593.85, 18599, 18726.4, 18634.55, 18563.4, 18601.5, 18716.15, 18755.9,
    18688.1, 18826, 18755.45, 18816.7, 18856.85, 18771.25, 18665.5, 18691.2, 18817.4, 18972.1, 19189.05,
    19322.55, 19389, 19398.5, 19497.3, 19331.8, 19355.9, 19439.4, 19384.3, 19413.75, 19564.5, 19711.45,
    19749.25, 19833.15, 19979.15, 19745, 19672.35, 19680.6, 19778.3, 19659.9, 19646.05, 19753.8, 19733.55,
    19526.55, 19381.65, 19517, 19597.3, 19570.85, 19632.55, 19543.1, 19428.3, 19434.55, 19465, 19365.25,
    19310.15, 19393.6, 19396.45, 19444, 19386.7, 19265.8, 19306.05, 19342.65, 19347.45, 19253.8, 19435.3,
    19528.8, 19574.9, 19611.05, 19727.05, 19819.95, 19996.35, 19993.2, 20070, 20103.1, 20192.35, 20133.3,
    19901.4, 19742.35, 19674.25, 19674.55, 19664.7, 19716.45, 19523.55, 19638.3, 19528.75, 19436.1, 19545.75,
    19653.5, 19512.35, 19689.85, 19811.35, 19794, 19751.05, 19731.75, 19811.5, 19671.1, 19624.7, 19542.65,
    19281.75, 19122.15, 18857.25, 19047.25, 19140.9, 19079.6, 18989.15, 19133.25, 19230.6, 19411.75, 19406.7,
    19443.5, 19395.3, 19425.35, 19525.55, 19443.55, 19675.45, 19765.2, 19731.8, 19694, 19783.4, 19811.85,
    19802, 19794.7, 19889.7, 20096.6, 20133.15, 20267.9, 20686.8, 20855.1, 20937.7, 20901.15, 20969.4,
    20997.1, 20906.4, 20926.35, 21182.7, 21456.65, 21418.65, 21453.1, 21150.15, 21255.05, 21349.4, 21441.35,
    21654.75, 21778.7, 21731.4, 21741.9, 21665.8, 21517.35, 21658.6, 21710.8, 21513, 21544.85, 21618.7,
    21647.2, 21894.55, 22097.45, 22032.3, 21571.95, 21462.25
]
print(type(close_prices))  # Output: <class 'list'>

#To calculate daily_return we need to start the index at 1 till the end of the list 
#daily return are calculated by dividing the current price by the previouse one
daily_returns = [(close_prices[i] / close_prices[i-1]) - 1 for i in range(1, len(close_prices))]

# Step 2: Calculate daily volatility
# It calculates the average daily return over a given period of time
mean_return = sum(daily_returns) / len(daily_returns)
#return_val iterates through each and every value in daily_returns and that value after being subtracted by mean_return is squared
squared_diff = [(return_val - mean_return) ** 2 for return_val in daily_returns]
#variance is average of squared diff by the number of daily_returns
variance = sum(squared_diff) / len(daily_returns)
#Square root of varaiance is Daily_volatility
daily_volatility = math.sqrt(variance)

# Step 3: Calculate annualized volatility
annualized_volatility = daily_volatility * math.sqrt(len(close_prices))

# Print the results
print("Daily Volatility:", daily_volatility)
print("Annualized Volatility:", annualized_volatility)
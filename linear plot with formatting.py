import matplotlib.pyplot as plt
import numpy as np
company1_years = list(range(2015, 2024))
company1_revenue = [150, 170, 190, 200, 220, 250, 280, 300, 320]
company2_years = list(range(2015, 2024))
company2_revenue = [130, 150, 170, 180, 200, 230, 260, 280, 300]
# Plotting the data with different line formatting
plt.plot(company1_years, company1_revenue, label='Company 1', linestyle='-', 
marker='o', color='blue')
plt.plot(company2_years, company2_revenue, label='Company 2', linestyle='--', 
marker='s', color='green')
# Adding labels and title 
plt.xlabel('Years') 
plt.ylabel('Revenue (in millions)')
plt.title('Comparison of Company Revenue Over Time')
# Adding a legend
plt.legend()
# Display the plot 
plt.grid(True) 
plt.show()
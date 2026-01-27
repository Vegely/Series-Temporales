import pandas as pd
import matplotlib.pyplot as plt


# 3. Load the Monthly Data
df_monthly = pd.read_csv('data_monthly.csv')
# Create a datetime column (assigning day=1 since it's monthly data)
df_monthly['DATETIME'] = pd.to_datetime(df_monthly[['ANO', 'MES']].assign(DAY=1).rename(
    columns={'ANO': 'year', 'MES': 'month', 'DAY': 'day'}
))

# 4. Plot Monthly Data
plt.figure(figsize=(12, 6))
plt.plot(df_monthly['DATETIME'], df_monthly['MONTHLY_AVG'], 
         label='Monthly Avg NO2', color='darkred', marker='o', linewidth=2)
plt.title('Monthly Average NO2 Concentration - Estación 38')
plt.xlabel('Date')
plt.ylabel('Concentration (µg/m³)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('monthly_no2_plot.png')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load confirmed cases data
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)
# Clean data: Group by country and transpose
df_clean = df.drop(columns=["Lat", "Long", "Province/State"])
df_country = df_clean.groupby("Country/Region").sum().T
df_country.index = pd.to_datetime(df_country.index, format='%m/%d/%y')  # Convert dates
plt.figure(figsize=(12, 6))
df_country.sum(axis=1).plot(title="Global COVID-19 Cases")
plt.ylabel("Total Cases")
plt.savefig("global_cases.png")  # For portfolio
top_5 = df_country.iloc[-1].sort_values(ascending=False).head(5)
top_5.plot(kind="bar", title="Top 5 Countries by Total Cases")
plt.savefig("top_countries.png")
# Example: Daily new cases in the US
us_cases = df_country["US"].diff().fillna(0)
us_cases.plot(title="Daily New Cases in the US", figsize=(12, 4))
# Normalize to per 100K population
populations = {"US": 331e6, "India": 1.4e9, "Brazil": 213e6}  # Approx
for country in ["US", "India", "Brazil"]:
    df_country[f"{country}_per_100k"] = df_country[country] / populations[country] * 1e5

df_country[["US_per_100k", "India_per_100k", "Brazil_per_100k"]].plot(title="Cases per 100K Population")

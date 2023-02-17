#%%
import duckdb
import pandas as pd

#%%

df = pd.read_csv('us2021census.csv')
# %%

# cities with over a million people
duckdb.filter(df, 'Population > 1000000')
# %%
# using an actual SQL query on the pandas df
query_str = """
SELECT City, Population
FROM df
WHERE Population > 500000
"""

duckdb.query(query_str)

#%%
query_str = """
SELECT State, CAST(AVG(Population) AS INTEGER) AS AVG_City_Pop
FROM df
GROUP BY State
ORDER BY AVG_City_Pop DESC
"""

# convert results of query to a new dataframe
avg_city_pop_by_state = duckdb.query(query_str).to_df()

# %%

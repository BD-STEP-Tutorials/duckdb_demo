#%%
import duckdb
import pandas as pd

#%%
#load csv
census = pd.read_csv('us2021census.csv')


# %%
# Filtering example
query_str = """
    SELECT City, Population
    FROM census
    WHERE Population > 1000000
    """

duckdb.query(query_str)

#%%
# GROUP BY Example
query_str = """
    SELECT State, CAST(AVG(Population) AS INTEGER) AS AVG_City_Pop
    FROM census
    GROUP BY State
    ORDER BY AVG_City_Pop DESC
    """

# convert results of query to a new dataframe
avg_city_pop_by_state = duckdb.query(query_str).to_df()


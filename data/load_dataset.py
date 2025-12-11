from ucimlrepo import fetch_ucirepo
import pandas as pd

print("Fetching data from repo")
online_retail = fetch_ucirepo(id=352)
df_retail = online_retail.data.original
print("Done")
print("Saving set as csv into /data")
df_retail.to_csv("./data/online_retail.csv", index=False)
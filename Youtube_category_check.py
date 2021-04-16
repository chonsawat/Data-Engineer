import pandas as pd
import pickle
import json
from tabulate import tabulate

# มาจาก: https://www.kaggle.com/datasnaek/youtube-new?select=US_category_id.json
kaggle = json.load(open("Data/Kaggle/JSON/US_category_id.json", "rb"))['items']

# มาจาก: https://gist.github.com/dgp/1b24bf2961521bd75d6c
yt_api = pickle.load(open("Data/cate.p", "rb"))

# Kaggle
tmp = []
for item in kaggle:
    id = item['id']
    title = item['snippet']["title"]
    tmp.append({
        "cate_id": int(id),
        "Kaggle": title
    })

df_kaggle = pd.DataFrame(tmp)

# Youtube API
df_yt_api = pd.DataFrame([yt_api]).T.reset_index().rename(columns={
    "index": "cate_id",
    0: "API"
})

# Join
df = df_kaggle.merge(df_yt_api, how="inner", on="cate_id").sort_values("cate_id").set_index("cate_id")
print(tabulate(
    df,
    headers="keys",
    tablefmt="grid"
))


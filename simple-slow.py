import orjson, json
from timeit import default_timer as timer
from collections import defaultdict

import altair
import json
import pandas as pd

subreddit_count = defaultdict(int)

start = timer()

files = ["data/reddit_comments_2019_09.txt"] # "reddit_comments_2019_09.txt"
for dataLocation in files:
    with open(dataLocation) as f:
        for line in f:
            try:
                subreddit = orjson.loads(line)["subreddit"]
                subreddit_count[subreddit] += 1
            except Exception as e:
                print(e)
end = timer()

print(f"seconds elapsed: {end - start}")

with open("output.json", "w") as outfile:
    json.dump(subreddit_count, outfile)


subredditCounts = None
with open("output.json") as f:
    subredditCounts = json.load(f)

data = (
    pd.DataFrame(list(subredditCounts.items()), columns=["subreddit", "comments"])
    .sort_values(by=["comments"], ascending=False)
    .head(20)
)

import altair as alt

bars = (
    alt.Chart(data)
    .mark_bar()
    .encode(x="comments", y=alt.Y("subreddit", sort="-x"))
    .properties(height=500)
    .save("chart.html")
)

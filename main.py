import json
from tolls import *

with open("operations.json", "r", encoding="utf-8") as f:
    df = json.load(f)

sotring_df = sort_date(df)
for line in check_dict(sotring_df)[:5]:
    date = convert_data(line["date"])
    description = line["description"]
    to = hides_data(line["to"])
    if "from" in line:
        from_ = hides_data(line["from"])
        operation = f"{from_} -> {to}"
    else:
        operation = to
    amount = line["operationAmount"]["amount"] + " " + line["operationAmount"]["currency"]["name"]

    print(f"{date} {description}")
    print(f"{operation}")
    print(f"{amount} \n")

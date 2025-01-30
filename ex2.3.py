import json

with open("large-file.json", "r") as large_data:
    lrg_data = json.load(large_data)

updated_lrg_data = []

for i in lrg_data:
    i["payload"]["size"] = 42
    updated_lrg_data.append(i)

rvrs_updated_lrg_data = updated_lrg_data[::-1]

with open("output.2.3.json", "w") as rvrs_large_data:
    json.dump(rvrs_updated_lrg_data, rvrs_large_data, indent = 2)
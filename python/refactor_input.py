from data import data as samples

print(len(samples[0]["cities"]), samples[0]["length"])

for item in samples[0]["cities"]:
    print(item[0], item[1])
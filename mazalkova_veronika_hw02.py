import csv
import json

input_file = "netflix_titles.tsv"
output_file = "hw02_output.json"

outcome = []

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for line in reader:
        
        movie_name = line["PRIMARYTITLE"].strip()

        if line["DIRECTOR"].strip() != "":
            drctrs = line["DIRECTOR"].split(",")
            drctrs = [name.strip() for name in drctrs]
        else:
            drctrs = []

        if line["CAST"].strip() != "":
            ctrs = line["CAST"].split(",")
            ctrs = [name.strip() for name in ctrs]
        else:
            ctrs = []

        gnrs = line["GENRES"].split(",")
        gnrs = [gnr.strip() for gnr in gnrs]

        yrs = line["STARTYEAR"].strip()
        if yrs.isdigit():
            yr = int(yrs)
            dcd = (yr // 10) * 10
        else:
            continue

        
        mv = {
            "title": movie_name,
            "directors": drctrs,
            "cast": ctrs,
            "genres": gnrs,
            "decade": dcd
        }

        outcome.append(mv)

with open(output_file, "w", encoding="utf-8") as output:
    json.dump(outcome, output, ensure_ascii=False, indent=2)
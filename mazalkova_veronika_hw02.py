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
            directors = line["DIRECTOR"].split(",")
            directors = [name.strip() for name in directors]
        else:
            directors = []

        if line["CAST"].strip() != "":
            actors = line["CAST"].split(",")
            actors = [name.strip() for name in actors]
        else:
            actors = []

        genres = line["GENRES"].split(",")
        genres = [gnr.strip() for gnr in genres]

        start_year = line["STARTYEAR"].strip()
        if start_year.isdigit():
            year = int(start_year)
            decade = (year // 10) * 10
        else:
            continue
        
        movie = {
            "title": movie_name,
            "directors": directors,
            "cast": actors,
            "genres": genres,
            "decade": decade
        }

        outcome.append(movie)

with open(output_file, "w", encoding="utf-8") as output:
    json.dump(outcome, output, ensure_ascii=False, indent=2)
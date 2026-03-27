import csv


def save_to_csv_analize(data_list, filename="report_1.csv"):

    headers = ['РЕЗУЛЬТАТ']
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for line in data_list:
            writer.writerow([line])

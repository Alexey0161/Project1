def save_to_csv(data_list, filename="report.csv"):
    import csv
    headers = ['РЕЗУЛЬТАТ']
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for line in data_list:
            writer.writerow([line])
    
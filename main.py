from json import loads
from csv import writer, QUOTE_MINIMAL


def main():
    backup_filename = "webtime-tracker-backup"
    print("Starting to convert ", backup_filename, " to CSV..")

    tracker_data = loads(open(backup_filename + ".json", "r").read())
    with open(backup_filename + ".csv", mode="w", newline="") as transformed_file:
        csv_writer = writer(
            transformed_file, delimiter=",", quotechar='"', quoting=QUOTE_MINIMAL
        )
        csv_writer.writerow(["Date", "Domain", "Time (seconds)"])

        for domain_data in tracker_data["content"]["domains"].values():
            for date, date_data in domain_data["days"].items():
                csv_writer.writerow([date, domain_data["name"], date_data["seconds"]])

    print("Conversion finished!")


if __name__ == "__main__":
    main()

def generate_summary(cleaned_data):

    with open("outputs/summary_report.txt", "w") as f:

        f.write("DATA CLEANING SUMMARY\n")

        f.write(f"Total Clean Records: {len(cleaned_data)}\n")
import chardet

csv_file = "/home/bglbgsz0j3/Downloads/Compliance_SET2/SET2/Compliance_feedback_set_2_nb-NO.csv"

with open(csv_file, "rb") as f:
    result = chardet.detect(f.read())
    print(result)

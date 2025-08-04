import csv
from gpt_utils import evaluate_supplier_risk

with open("suppliers.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        comment = row[0]
        risk = evaluate_supplier_risk(comment)
        print(f"Comment: {comment} -> Risk Score: {risk}")

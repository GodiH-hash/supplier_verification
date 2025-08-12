import csv
from gpt_utils import evaluate_risk

input_file = "suppliers.csv"
output_file = "supplier_risk_results.csv"

results = []

with open(input_file, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        comment = row[0]
        score = evaluate_risk(comment)
        print(f"Comment: {comment}\nRisk: {score}/10\n")
        results.append([comment, score])

# Save results to new CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Supplier Comment", "Risk Score"])
    writer.writerows(results)

print(f"✅ Results saved to {output_file}")

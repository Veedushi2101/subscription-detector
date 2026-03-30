import csv
from datetime import datetime
from detector import detect_subscriptions

# -------------------------------
# Read CSV
# -------------------------------
def read_transactions(file_path):
    transactions = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                date = datetime.strptime(row['Date'], '%Y-%m-%d')
                amount = float(row['Amount'])
                description = row['Description']

                transactions.append({
                    'date': date,
                    'amount': amount,
                    'description': description
                })
            except:
                continue

    return transactions


# -------------------------------
# Display Results
# -------------------------------
def display(subscriptions):
    print("\n Subscriptions Found:")
    print("----------------------------------")

    for sub in subscriptions:
        print(f"{sub['name'].title()} → ₹{sub['amount']}/month "
              f"(Confidence: {sub['confidence']*100:.0f}%)")

    total = sum(sub['amount'] for sub in subscriptions)

    print("\n Total Monthly Spend: ₹", total)
    
def calculate_waste(subscriptions, months=6):
    print("\n Potential Waste:")

    for sub in subscriptions:
        waste = sub['amount'] * months
        print(f"{sub['name'].title()} → ₹{waste} in {months} months")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    file_path = "transactions.csv"

    transactions = read_transactions(file_path)

    subscriptions = detect_subscriptions(transactions)

    if not subscriptions:
        print("No subscriptions detected.")
    else:
        display(subscriptions)
        calculate_waste(subscriptions)
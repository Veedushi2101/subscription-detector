import csv
from datetime import datetime
from collections import defaultdict

# -------------------------------
# Step 1: Read CSV File
# -------------------------------
def read_transactions(file_path):
    transactions = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                date = datetime.strptime(row['Date'], '%Y-%m-%d')
                amount = float(row['Amount'])
                description = row['Description'].strip()

                transactions.append({
                    'date': date,
                    'amount': amount,
                    'description': description
                })
            except:
                continue

    return transactions


# -------------------------------
# Step 2: Detect Recurring Payments
# -------------------------------
def detect_subscriptions(transactions):
    grouped = defaultdict(list)

    # Group by (description, amount)
    for txn in transactions:
        key = (txn['description'].lower(), round(txn['amount'], 2))
        grouped[key].append(txn['date'])

    subscriptions = []

    for (desc, amount), dates in grouped.items():
        if len(dates) < 3:
            continue

        dates.sort()

        # Check if intervals are roughly monthly (25–35 days)
        valid = True
        for i in range(1, len(dates)):
            diff = (dates[i] - dates[i-1]).days
            if diff < 25 or diff > 35:
                valid = False
                break

        if valid:
            subscriptions.append({
                'name': desc,
                'amount': amount,
                'occurrences': len(dates)
            })

    return subscriptions


# -------------------------------
# Step 3: Calculate Spend
# -------------------------------
def calculate_total(subscriptions):
    total_monthly = 0

    for sub in subscriptions:
        total_monthly += sub['amount']

    return total_monthly

def calculate_waste(subscriptions, months=6):
    print("\n Potential Waste (if unused):")

    for sub in subscriptions:
        waste = sub['amount'] * months
        print(f"{sub['name'].title()} → ₹{waste} in {months} months")

# -------------------------------
# Step 4: Display Results
# -------------------------------
def display(subscriptions):
    print("\n Subscriptions Found:")
    print("----------------------------")

    for sub in subscriptions:
        print(f"{sub['name'].title()}  → ₹{sub['amount']} / month")

    total = calculate_total(subscriptions)

    print("\n Total Monthly Spend: ₹", total)


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    file_path = "transactions.csv"  # your input file

    transactions = read_transactions(file_path)

    subscriptions = detect_subscriptions(transactions)

    if not subscriptions:
        print("No subscriptions detected.")
    else:
        display(subscriptions)
    
    calculate_waste(subscriptions)
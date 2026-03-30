# Subscription Trap Detector

A smart Python-based system that analyzes bank transaction data to automatically detect recurring subscriptions and highlight potential financial waste.

---

## Problem

In today’s digital world, users subscribe to multiple services such as streaming platforms, music apps, and memberships. These subscriptions:

* Renew automatically
* Are often forgotten
* Deduct small amounts regularly

**Over time, this leads to **unnoticed financial loss**

---

## What This Project Does

This project takes a **bank statement (CSV file)** as input and:

* Detects recurring transactions
* Identifies subscription patterns intelligently
* Calculates total monthly subscription cost
* Estimates potential waste over time

---

## Key Concepts Used

This project applies important course concepts:

* **Data Structures** → dictionaries, lists, grouping
* **File Handling** → reading CSV files
* **String Processing** → cleaning noisy data
* **Pattern Recognition** → detecting recurring intervals
* **Modular Programming** → structured code design

---

## Project Structure

```
subscription-detector/
│── transactions.csv     # Input data
│── main.py              # Entry point (run this file)
│── detector.py          # Core detection logic
│── utils.py             # Helper functions
│── README.md            # Project documentation
```

---

## Installation & Setup

### Prerequisites

* Python 3 installed on your system

### Steps to Run

1. Clone the repository:

```
git clone https://github.com/your-username/subscription-detector.git
cd subscription-detector
```

2. Make sure your CSV file is present:

```
transactions.csv
```

3. Run the program:

```
python main.py
```

---

## Input File Format

Your CSV file must follow this structure:

```
Date,Amount,Description
2025-01-05,499,Netflix India
2025-02-05,499,NETFLIX.COM
2025-03-06,500,Netflix*123
2025-01-10,119,Spotify
2025-02-10,119,Spotify Premium
2025-03-10,119,SPOTIFY LTD
```

### Important Notes:

* Date format must be: `YYYY-MM-DD`
* Amount must be numeric
* Description can be messy (system handles it)

---

## ▶️ How It Works (Step-by-Step)

### 1. Data Cleaning

* Converts text to lowercase
* Removes special characters
* Normalizes merchant names

---

### 2. Transaction Grouping

Transactions are grouped using:

```
(cleaned_description, approximate_amount)
```

---

### 3. Pattern Detection

* Checks if transactions repeat every ~30 days
* Requires at least 3 occurrences

---

### 4. Smart Detection

Handles:

* Different names for same service
* Slight variation in amounts
* Irregular dates

---

### 5. Confidence Score

Each subscription is assigned a confidence score:

```
confidence = occurrences / 3
```

---

### 6. Waste Calculation

```
waste = monthly_cost × number_of_months
```

---

## Sample Output

```
Subscription Analysis Report
====================================

1. Netflix
   Cost: ₹499/month
   Confidence: 100%

2. Spotify
   Cost: ₹119/month
   Confidence: 100%

------------------------------------
Total Monthly Spend: ₹618

Potential Waste:
Netflix → ₹2994 in 6 months
Spotify → ₹714 in 6 months
```

---

## Example Use Case

A user uploads their bank statement and discovers:

* They are paying for **3 subscriptions**
* Monthly cost is ₹600+
* ₹3000+ wasted over 6 months

**This helps them decide what to cancel.**

---

## Technologies Used

* Python
* CSV file handling
* Datetime module
* Regular Expressions (`re`)
* Collections (`defaultdict`)

---

## Limitations

* Only supports CSV input
* Detects mainly monthly subscriptions
* No real-time bank integration

---

## Future Improvements

* Web application (Flask / React)
* PDF statement support
* Machine learning-based classification
* Graphs and dashboards
* Subscription alerts

---

## 📚 Learning Outcomes

Through this project:

* Applied programming concepts to a real-world problem
* Learned data cleaning and preprocessing
* Implemented pattern detection logic
* Improved code structuring and modular design
* Understood importance of documentation

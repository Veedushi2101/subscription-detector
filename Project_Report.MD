## **Subscription Trap Detector: Detecting and Analyzing Recurring Financial Subscriptions**
---
## **1. Introduction**

With the rapid growth of digital services, users increasingly rely on subscription-based platforms such as streaming services, cloud storage, and e-commerce memberships. These services operate on recurring billing models, automatically deducting money at fixed intervals (monthly, quarterly, or yearly).

While convenient, this model introduces a significant problem: **users often lose track of active subscriptions**, leading to unnecessary financial expenditure. Small recurring payments accumulate over time, resulting in substantial unnoticed losses.

This project, **Subscription Trap Detector**, aims to address this issue by building a system that automatically detects recurring transactions from bank statements and provides meaningful insights into subscription spending.

---

## **2. Problem Statement**

Many individuals fail to monitor their recurring expenses due to:

* Lack of awareness of active subscriptions
* Irregular tracking of bank transactions
* Small transaction amounts that are often ignored

This results in:

* Financial leakage over time
* Inefficient personal finance management

**Objective:**
To design and implement a system that can automatically detect subscription-based payments and provide actionable insights to users.

---

## **3. Objectives**

The primary objectives of this project are:

* To analyze bank transaction data
* To detect recurring transactions automatically
* To identify subscription-based services
* To calculate total monthly subscription expenditure
* To estimate potential financial waste
* To provide a structured and user-friendly output

---

## **4. Scope of the Project**

### **Included:**

* CSV-based bank statement analysis
* Monthly subscription detection
* Basic financial insights

### **Excluded:**

* Real-time bank integration
* Payment cancellation automation
* Advanced ML models (future scope)

---

## **5. System Overview**

The system takes a bank statement as input and processes it through multiple stages:

1. Data ingestion
2. Data cleaning and normalization
3. Transaction grouping
4. Pattern detection
5. Subscription identification
6. Output generation

---

## **6. Methodology**

### **6.1 Data Input**

The system accepts a CSV file with the following fields:

* `Date` (YYYY-MM-DD format)
* `Amount` (numeric)
* `Description` (string)

---

### **6.2 Data Preprocessing**

Steps performed:

* Convert descriptions to lowercase
* Remove special characters using regex
* Normalize whitespace
* Convert date strings to `datetime` objects

---

### **6.3 Feature Engineering**

Two main features are derived:

* **Cleaned Merchant Name** → for grouping
* **Amount Bucket** → handles slight price variations

Example:

```
₹499 → ₹500 (rounded bucket)
```

---

### **6.4 Transaction Grouping**

Transactions are grouped using:

```
(cleaned_description, amount_bucket)
```

This allows the system to handle:

* Typographical variations
* Minor pricing differences

---

### **6.5 Pattern Detection Algorithm**

To identify subscriptions:

* Extract transaction dates for each group
* Sort dates chronologically
* Compute time gaps between consecutive transactions

#### Condition for subscription:

* Minimum 3 transactions
* Average gap between 25–35 days

---

### **6.6 Mathematical Representation**

Let:

* `d1, d2, d3 ... dn` be transaction dates
* Gap = `di - d(i-1)`

Then:

```
Average Gap = (Sum of all gaps) / (n - 1)
```

If:

```
25 ≤ Average Gap ≤ 35
```

→ Transaction is classified as a subscription

---

### **6.7 Confidence Scoring**

Confidence is calculated as:

```
confidence = min(1.0, number_of_occurrences / 3)
```

* 3+ occurrences → High confidence
* Fewer occurrences → Lower confidence

---

### **6.8 Waste Estimation**

Potential waste is calculated as:

```
Waste = Monthly Cost × Number of Months
```

---

## **7. System Architecture**

### **Modular Design**

```
main.py        → Input/Output handling  
detector.py    → Core detection logic  
utils.py       → Helper functions  
```

---

### **Data Flow**

```
CSV File → main.py → detector.py → utils.py → Output
```

---

## **8. Implementation Details**

### **Programming Language**

* Python

### **Libraries Used**

* `csv` → reading files
* `datetime` → date calculations
* `collections` → grouping data
* `re` → text cleaning

---

### **Key Functions**

#### `clean_name()`

* Removes noise from transaction descriptions

#### `is_monthly_pattern()`

* Detects recurring patterns using date gaps

#### `detect_subscriptions()`

* Core function for identifying subscriptions

---

## **9. Results and Output**

### **Sample Output**

```
📊 Subscription Analysis Report

1. Netflix
   Cost: ₹499/month
   Confidence: 100%

2. Spotify
   Cost: ₹119/month
   Confidence: 100%

Total Monthly Spend: ₹618
```

---

## **10. Challenges Faced**

* Inconsistent transaction descriptions
* Slight variations in amounts
* Handling irregular billing cycles
* Avoiding false positives

---

## **11. Evaluation of Solution**

### **Strengths**

* Handles real-world noisy data
* Modular and scalable design
* Easy to use and interpret

### **Limitations**

* Only CSV input supported
* Fixed interval detection (monthly only)
* No real-time tracking

---

## **12. Future Enhancements**

* Web-based interface (Flask/React)
* PDF bank statement parsing
* Machine Learning-based classification
* Category-wise spending analysis
* Email/SMS alerts

---

## **13. Learning Outcomes**

Through this project, the following skills were developed:

* Problem-solving using real-world data
* Data preprocessing and cleaning
* Pattern recognition in time-series data
* Writing modular and scalable code
* Designing user-centric solutions

---

## **14. Conclusion**

The **Subscription Trap Detector** successfully demonstrates how computational techniques can be applied to solve real-world financial problems. By identifying recurring transactions and providing insights into subscription spending, the system helps users make informed financial decisions.

The project balances simplicity and effectiveness, making it both practical and scalable for future enhancements.

---

## **15. References**

* Python Official Documentation
* Concepts of Data Cleaning and Preprocessing
* Time-Series Pattern Detection Techniques
* Online tutorials and programming resources

---


from collections import defaultdict
from typing import List, Dict

def topSpendingCategory (transactions: List[Dict]) -> Dict:

    spending = defaultdict(float)

    for val in transactions:
        category = val['category']
        amount = val['amount']
        spending[category] += amount

    topCategory = max(spending, key=spending.get)

    return {
            'category': topCategory,
            'total': spending[topCategory]
        }

def outputReport (transactions: List[Dict]) -> Dict:

    if not transactions:
        return ("There were no valid transactions provided.")
    
    num = len(transactions)
    totalSpending = 0.0
    for val in transactions:
        totalSpending += val['amount']
    topCategory = topSpendingCategory(transactions)

    categoryGroups = defaultdict(list)
    for val in transactions:
        category = val['category']
        categoryGroups[category].append(val)

    BOLD = '\033[1m'
    END = '\033[0m'

    report = f"""
    
    {BOLD}FINANCIAL REPORT{END}

    {BOLD}Number of Transactions:{END} {num}
    {BOLD}Total Amount:{END} ${totalSpending:.2f}

    {BOLD}Top Spending Category:{END} {topCategory['category'].title()}
    {BOLD}Amount:{END} ${topCategory['total']:.2f}
    """

    for cat, val in categoryGroups.items():
        report += f"\n    {BOLD}{cat.title()}{END}:\n"
        for i in val:
            date = i.get("date")
            merchant = i.get("merchant")
            amount = i["amount"]
            report += f"      {date} {merchant} ${amount:.2f}\n"

    return report

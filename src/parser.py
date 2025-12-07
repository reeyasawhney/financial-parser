import pandas
from pathlib import Path
from typing import List, Dict

def validateTransactions(transaction: Dict) -> bool:
    
    reqFields = ['date', 'merchant', 'amount', 'category']

    for field in reqFields:
        if field not in transaction:
            return False
        if pandas.isna(transaction[field]):
            return False
        if (isinstance(transaction[field], str) and not transaction[field].strip()):
            return False
    
    return True

def parseTransactions(filepath: str) -> List[Dict]:

    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"The provided file {filepath} does not exist.")
    if not filepath.is_file():
        raise ValueError(f"The provided file {filepath} is not recognized as a valid file.")
    
    try:
        parsed = pandas.read_csv(filepath, encoding='utf-8', encoding_errors='replace', on_bad_lines='skip')
        #ADDED ON BAD LINES NEWLYYY
    except Exception as e:
        raise ValueError(f"There was an error parsing the file: {str(e)}")
    
    reqCols = ['date', 'merchant', 'amount', 'category']
    missingCols = []
    for col in reqCols:
        if col not in parsed.columns:
            missingCols.append(col)
    
    if missingCols:
        raise ValueError(f"There are transactions with the following missing fields: {missingCols}")
    
    transactions = parsed.to_dict('records')

    valid = []
    invalid = 0

    inval = []

    for val in transactions:
        if validateTransactions(val):
            valid.append(val)
        else: 
            invalid += 1
            inval.append(val)
    
    if invalid > 0:
        print(f"Skipped {invalid} transactions because they did not have all 4 required fields.")
        for i in inval:
            print(i)

    return valid

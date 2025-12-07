**Instructions to Run Program**
1. Clone this repository
2. Create a python virtual environment
3. Install dependencies: pip install pandas python-dateutil price-parser rapidfuzz forex-python requests
4. Run on command line: python main.py

**Architechture**
* parser.py - parse through CSV and validate transactions
* cleaner.py - clean each of the 4 fields and standardize the transactions
* analyzer.py - calculate top spending category and output a financial report

**Design Choices & Methodology**
* I imported the dateutil library and used dateutil.parser.parse() with fuzzy matching to normalize parsing through dates of different formats. This library can handle standard ISO, text, slash, and date formats. I prompted Claude to generate the code for this and validated it against 10 different date formats.
* I prompted the regex library to clean the merchant names by converting the complete string to lowercase, removing non-ASCII characters, normalizing whitespace, and capitalizing the first letter of each word.
    * I initially attempted to implement fuzzy matching for the merchant names (ex: Uber Eats and Uber Trip would normalize to Uber), but I decided against that in my final implementation because these merchant names could be part of different categories (ex: Food vs Transportation).
* I imported the forex_python.converter library and the free public API (https://api.exchangerate-api.com/v4/latest/USD) to handle converting and normalizing different currencies into USD. I created a dictionary mapping currency codes to their respective symbols since python's CurrencyRates utilizes currency codes, but the transaction list may have the symbol instead (ex: $ vs USD). I prompted Claude to generate the math logic behind converting rates and a fallback process if the API fails or the currency symbol is not in my dictionary. Additionally, I prompted Claude to recognize currency symbols outside the ASCII set. I verified this code by testing it against transaction amounts in the form of (USD, EUR, INR, JYP, $, €, ₹, ¥).
* I prompted Claude to generate a comprehensive messy.csv file. I provided detailed guidelines of what I wanted the messy.csv file to include (ex: invalid transactions missing a field, different date formats, mixed naming convention for merchants, different currency types, etc.)

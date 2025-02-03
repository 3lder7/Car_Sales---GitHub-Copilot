import re

def find_dates(text):
    # Regular expression to match dates in formats like DD/MM/YYYY, DD-MM-YYYY, YYYY/MM/DD, YYYY-MM-DD
    date_pattern = r'\b(?:\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|\d{2,4}[\/\-]\d{1,2}[\/\-]\d{1,2})\b'
    dates = re.findall(date_pattern, text)
    return dates

# Example usage
if __name__ == "__main__":
    sample_text = "These are some dates: 12/05/2021, 2021-05-12, and 05-12-21."
    print(find_dates(sample_text))
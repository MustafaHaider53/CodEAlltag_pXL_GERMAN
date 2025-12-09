# CSV Dataset Documentation

## Overview
This document describes the CSV format of the CodE Alltag XL GERMAN email dataset.

## File Information
- **Filename**: `emails_dataset.csv`
- **Total Records**: 240,673 emails
- **File Size**: ~88MB
- **Encoding**: UTF-8
- **Format**: CSV (Comma-Separated Values) with quoted fields

## CSV Structure

The CSV file contains three columns:

| Column Name | Type | Description |
|-------------|------|-------------|
| `file_id` | String | The original filename (without .txt extension) of the email |
| `directory` | String | The relative directory path where the email was stored |
| `email_text` | String | The complete content of the email |

## Example

```csv
"file_id","directory","email_text"
"8656","8-","On 2008-02-06 08:34:23 -0500, Luca Gianni <hdbg@nvrzwpu-hdwm.ts> said:\n\n\nDir, lieber Lutz, sei anvertraut, daß auch unter konservativen..."
"87955","8-","Am Thu, 5 Mai 2009 09:11:52 +0100 schrieb Thierry Dworsky:\n\n\nDer wäre wohl nicht so ganz die wünschenswerte Alternative gewesen..."
```

## Usage

### Python
```python
import csv
import pandas as pd

# Using csv module
with open('emails_dataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        file_id = row['file_id']
        directory = row['directory']
        email_text = row['email_text']
        # Process email...

# Using pandas
df = pd.read_csv('emails_dataset.csv')
print(df.head())
print(f"Total emails: {len(df)}")
```

### R
```r
# Read CSV
emails <- read.csv('emails_dataset.csv', encoding = 'UTF-8')

# View structure
str(emails)
head(emails)
```

### Excel/Spreadsheet Applications
The CSV file can be opened in Excel, Google Sheets, or LibreOffice Calc. Make sure to:
1. Set encoding to UTF-8
2. Use comma as the delimiter
3. Recognize quoted fields

## Generation

The CSV file was generated using the `convert_to_csv.py` script, which:
1. Recursively scans all directories for `.txt` files
2. Reads each email file with UTF-8 encoding
3. Preserves the original content including line breaks and special characters
4. Outputs a properly formatted CSV with quoted fields

## Notes

- All fields are quoted to handle multi-line content and special characters
- Line breaks within email text are preserved as `\n`
- The original directory structure is preserved in the `directory` column
- Character encoding issues in source files are handled with replacement characters
- The dataset contains pseudonymized emails as described in the main README.md

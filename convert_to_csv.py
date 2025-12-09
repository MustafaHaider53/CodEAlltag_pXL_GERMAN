#!/usr/bin/env python3
"""
Script to convert the German email dataset (CodE Alltag XL GERMAN) to CSV format.
This script traverses all directories and converts individual email text files to a single CSV file.
"""

import os
import csv
import sys
from pathlib import Path

# Progress reporting interval (number of emails processed before showing update)
PROGRESS_INTERVAL = 1000


def find_all_txt_files(base_dir):
    """
    Find all .txt files in the directory structure.
    
    Args:
        base_dir: Base directory to search
        
    Yields:
        Tuple of (file_id, relative_path, absolute_path)
    """
    base_path = Path(base_dir)
    
    for txt_file in base_path.rglob('*.txt'):
        # Get relative path from base directory
        rel_path = txt_file.relative_to(base_path)
        
        # Extract file ID (filename without extension)
        file_id = txt_file.stem
        
        # Get directory path (relative)
        dir_path = str(rel_path.parent)
        
        yield (file_id, dir_path, str(txt_file))


def convert_to_csv(base_dir, output_file='emails_dataset.csv'):
    """
    Convert all email text files to a CSV format.
    
    Args:
        base_dir: Base directory containing email files
        output_file: Output CSV file name
    """
    print(f"Starting conversion of email dataset to CSV...")
    print(f"Base directory: {base_dir}")
    print(f"Output file: {output_file}")
    
    # CSV columns: file_id, directory, email_text
    fieldnames = ['file_id', 'directory', 'email_text']
    
    count = 0
    errors = 0
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        
        for file_id, dir_path, file_path in find_all_txt_files(base_dir):
            try:
                # Read the email content
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    email_text = f.read()
                
                # Write to CSV
                writer.writerow({
                    'file_id': file_id,
                    'directory': dir_path,
                    'email_text': email_text
                })
                
                count += 1
                
                # Progress indicator
                if count % PROGRESS_INTERVAL == 0:
                    print(f"Processed {count} emails...", file=sys.stderr)
                    
            except Exception as e:
                errors += 1
                print(f"Error processing {file_path}: {e}", file=sys.stderr)
    
    print(f"\nConversion complete!")
    print(f"Total emails processed: {count}")
    print(f"Errors encountered: {errors}")
    print(f"Output saved to: {output_file}")


if __name__ == '__main__':
    # Get the script directory (repository root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Output file path
    output_csv = os.path.join(script_dir, 'emails_dataset.csv')
    
    # Convert to CSV
    convert_to_csv(script_dir, output_csv)

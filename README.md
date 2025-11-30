# doctor-data-extractor
A simple Python tool that extracts doctor names, emails, phone numbers, and specialties from HTML files and organizes them into a clean CSV file.
Healthcare Data Collection System

This is a small Python project that collects and organizes doctor information from HTML files. It extracts names, emails, phone numbers, specialties, and saves everything into a CSV file.
I built this because real healthcare datasets are not publicly available, so I created my own sample HTML and built a script that can parse it.

### Features

1. Extracts doctor names 
2. Extracts emails
3. Extracts Pakistani phone numbers
4. Detects common medical specialties
5. Works with any simple HTML file
6. Exports everything into a single CSV file

### How It Works
Add one or more HTML filenames when the script asks
The script reads each file
It pulls out the useful information
A clean CSV file is created with all results

## Requirements

Install the required library:

pip install beautifulsoup4

Run the Script
python main.py

Then provide your HTML file names when asked.

## Output

The program generates:
pakistan_doctor_data.csv



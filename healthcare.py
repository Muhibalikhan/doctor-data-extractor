# python based healthcare professional data collection and organization systen
import re
import csv
from bs4 import BeautifulSoup

# read the html file
def load_html_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except:
        print(f"Could not open file: {filename}")
        return ""

# parse html into text
def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")

# extract doctor names
def extract_doctor_names(text):
    names = []

    # extract name 
    pattern = r"Dr\.?\s+[A-Z][a-zA-Z\.]+(?:\s+[A-Za-z]{2,}){0,3}"

    found = re.findall(pattern, text)
    for name in found:
        names.append(name.strip())

    return list(set(names))

# PAKISTANI PHONE NUMBER EXTRACTION
def extract_phones(text):
    phones = []

    # phone number formats for pakistan:
    # +92 300 1234567
    # 0300-1234567
    # 042-12345678

    pattern = r"(?:\+92|0)\d{2,3}[- ]?\d{6,8}"

    found = re.findall(pattern, text)

    clean = []
    for p in found:
        p = p.replace(" ", "").replace("-", "")
        clean.append(p)

    return list(set(clean))


# Extract the emails
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return list(set(re.findall(pattern, text)))


# Speciality extraction 
def extract_specialties(text):
    keywords = [
        "cardiologist", "dermatologist", "neurologist", "orthopedic",
        "pediatrician", "gynecologist", "surgeon", "dentist",
        "psychiatrist", "urologist", "endocrinologist",
        "ent specialist", "skin specialist", "eye specialist", "general physician",
        "consultant"
    ]

    found = []
    text_lower = text.lower()

    for word in keywords:
        if word in text_lower:
            found.append(word.title())

    return list(set(found))


# Save data to csv
def save_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Doctor Name", "Email", "Phone", "Specialty", "Source File"])

        for row in data:
            writer.writerow(row)

    print(f"\n Data saved successfully to {filename}\n")

# MAIN

def main():
    print("\n=== PAKISTAN HEALTHCARE DATA COLLECTION SYSTEM ===\n")

    files = []
    while True:
        name = input("File name (or 'done'): ")
        if name.lower() == "done":
            break
        files.append(name)

    final_data = []

    for file in files:
        print(f"\n📄 Reading: {file}")

        html = load_html_file(file)
        if not html:
            continue

        text = extract_text(html)

        names = extract_doctor_names(text)
        emails = extract_emails(text)
        phones = extract_phones(text)
        specialties = extract_specialties(text)

        max_len = max(len(names), len(emails), len(phones), len(specialties), 1)

        for i in range(max_len):
            name = names[i] if i < len(names) else ""
            email = emails[i] if i < len(emails) else ""
            phone = phones[i] if i < len(phones) else ""
            specialty = specialties[i] if i < len(specialties) else ""

            final_data.append([name, email, phone, specialty, file])

    unique_data = []
    seen = set()

    for row in final_data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            unique_data.append(row)
            seen.add(row_tuple)

    save_to_csv("pakistan_doctor_data.csv", unique_data)
    print("DONE! Pakistani doctor extraction completed.\n")


main()

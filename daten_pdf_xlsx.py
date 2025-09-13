import pdfplumber
import pandas as pd
import re

pdf_file = r"C:\Users\........"

rows = []

with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            if re.match(r"\d{2}\.\d{2}\.\d{4}", line):
                parts = line.split()
                datum = parts[0]
                verwendung = " ".join(parts[1:-1])
                betrag_str = parts[-1].replace(".", "").replace(",", ".")
                try:
                    betrag = float(betrag_str)
                except ValueError:
                    betrag = 0.0
                rows.append([datum, verwendung, betrag])



df = pd.DataFrame(rows, columns=["Datum", "Verwendungszweck", "Betrag"])

df = df.iloc[::2, :]

print(df)


df.to_excel("kontoauszug.xlsx", index=False)

print("Kontoauszug wurde als kontoauszug.xlsx gespeichert")
import pdfplumber
import pandas as pd
import re

pdf_file = r"C:\Users\Davinci\Desktop\test_rechnung.pdf"

rows = []

with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            if re.match(r"\d{2}\.\d{2}\.\d{4}", line):
                parts = line.split()
                datum = parts[0]
                verwendung = " ".join(parts[1:-1])
                betrag_str = parts[-1].replace(".", "").replace(",", ".")
                try:
                    betrag = float(betrag_str)
                except ValueError:
                    betrag = 0.0
                rows.append([datum, verwendung, betrag])



df = pd.DataFrame(rows, columns=["Datum", "Verwendungszweck", "Betrag"])

df = df.iloc[::2, :]

print(df)


df.to_excel("kontoauszug.xlsx", index=False)

print("Kontoauszug wurde als kontoauszug.xlsx gespeichert")
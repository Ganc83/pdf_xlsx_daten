import pdfplumber
import pandas as pd
import re
import mysql.connector
import os
from datetime import datetime


pdf_file = r"C:\Users\..........."

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


#df.to_excel("kontoauszug.xlsx", index=False)

print("Kontoauszug wurde als kontoauszug.xlsx gespeichert")

daten = df

connection_auszug = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="konnto_auszüge"
)
cursor_auszüge = connection_auszug.cursor()


for index, row in df.iterrows():
    datum_str = row["Datum"]
    verwendung = row["Verwendungszweck"]
    betrag = row["Betrag"]
    # Umwandeln von DD.MM.YYYY → YYYY-MM-DD
    datum_mysql = datetime.strptime(datum_str, "%d.%m.%Y").strftime("%Y-%m-%d")

    print(datum_mysql)  # ergibt: 2025-08-29


    sql = """
    INSERT INTO auszug_konnto_01 (Datum, Verwendungszweck, Betrag)
    VALUES (%s, %s, %s)
    """
    values = (datum_mysql, verwendung, betrag)
    print(values)

    cursor_auszüge.execute(sql, values)

connection_auszug.commit()
cursor_auszüge.close()
connection_auszug.close()

print("✅ Daten erfolgreich in MySQL gespeichert!")
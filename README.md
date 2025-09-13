# PDF Kontoauszug nach Excel exportieren

Dieses Skript liest Kontoauszüge aus einer PDF-Datei aus und speichert die Daten (Datum, Verwendungszweck, Betrag) in einer **Excel-Datei** (`kontoauszug.xlsx`).

## Funktionsweise

- Öffnet eine PDF-Datei mit **pdfplumber**  
- Liest jede Seite und sucht nach Zeilen, die mit einem Datum beginnen (`TT.MM.JJJJ`)  
- Trennt die Zeile in:
  - **Datum**  
  - **Verwendungszweck**  
  - **Betrag**  
- Wandelt den Betrag in eine **Fließkommazahl** um  
- Entfernt jede zweite Zeile (da Kontoauszüge oft doppelte Zeilen enthalten)  
- Speichert die Daten in eine Excel-Datei  

## Voraussetzungen

Installiere die benötigten Python-Pakete mit:

```bash
pip install pdfplumber pandas openpyxl
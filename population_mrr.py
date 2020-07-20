from pathlib import Path
import sqlite3
import csv

conn = sqlite3.connect('DB.db')
c = conn.cursor()

p = Path('sources')
def read_csv(file_name):
    rows = []
    file_name = p / file_name
    with open(f'{file_name}.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0]: # some rows are without values
                rows.append(row)
    return rows[1:]

table = read_csv('Dim_Date')   
c.executemany('INSERT INTO Dim_Date(DateNum,Date,YearMonthNum,Calendar_Quarter,MonthNum,MonthName,MonthShortName,WeekNum,DayNumOfYear,DayNumOfMonth,DayNumOfWeek,DayName,DayShortName,Quarter,YearQuarterNum,DayNumOfQuarter) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', table)
conn.commit()

table = read_csv('BI_assignment_person')   
c.executemany('INSERT INTO Mrr_person(id_person,name,surname,zip,city,country,email,phone_number,birth_date) VALUES (?,?,?,?,?,?,?,?,?)', table)
conn.commit()

table = read_csv('BI_assignment_account')   
c.executemany('INSERT INTO Mrr_Account(id_account,id_person,account_type) VALUES (?,?,?)', table)
conn.commit()

table = read_csv('BI_assignment_transaction')   
c.executemany('INSERT INTO Mrr_Transaction(id_transaction,id_account,transaction_type,transaction_date,transaction_amount) VALUES (?,?,?,?,?)', table)
conn.commit()

conn.close()

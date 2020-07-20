import sqlite3
from datetime import datetime

conn = sqlite3.connect('DB.db')
c = conn.cursor()
# lots of people dont have account. I dont know if it acceptable. I assumed it is okay.
query_stg_account = """
SELECT IFNULL(a.id_account, -99) id_account,
       p.id_person,
       IFNULL(a.account_type, 'Unknown') account_type,
       p.name,
       p.surname,
       p.zip,
       p.city,
       p.country,
       p.email,
       p.phone_number,
       p.birth_date
FROM Mrr_Person p
       LEFT JOIN
       Mrr_Account a ON p.id_person = a.id_person;
"""

c.execute(query_stg_account)
transformed_rows = []

for row in c.fetchall():
    transformed_row = list(row)
    if '-' in transformed_row[10]:
        birth_date = datetime.strptime(transformed_row[10], '%d-%b-%y')
        transformed_birth_date = birth_date.strftime('%m/%d/%y')
        transformed_row[10] = transformed_birth_date
    transformed_rows.append(transformed_row)

table = transformed_rows
c.executemany('INSERT INTO Stg_Account(id_account,id_person,account_type,name,surname,zip,city,country,email,phone_number,birth_date) VALUES (?,?,?,?,?,?,?,?,?,?,?)', table)
conn.commit()

query_stg_transaction = """
SELECT id_transaction,
       id_account,
       transaction_type,
       transaction_date,
       transaction_amount
FROM Mrr_Transaction;
"""

c.execute(query_stg_transaction)
transformed_rows = []

for row in c.fetchall():
    transformed_row = list(row)
    transaction_date = datetime.strptime(transformed_row[3], '%m/%d/%y')
    transformed_transaction_date = transaction_date.strftime('%Y%m%d')
    transformed_row[3] = transformed_transaction_date
    transformed_rows.append(transformed_row)

table = transformed_rows
c.executemany('INSERT INTO Stg_Transaction(id_transaction,id_account,transaction_type,transaction_date,transaction_amount) VALUES (?,?,?,?,?)', table)
conn.commit()

conn.close()

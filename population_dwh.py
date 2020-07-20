import sqlite3
from datetime import datetime

conn = sqlite3.connect('DB.db')
c = conn.cursor()

query_dwh_account = """
SELECT id_account,
       id_person,
       account_type,
       name,
       surname,
       zip,
       city,
       country,
       email,
       phone_number,
       birth_date
FROM Stg_Account
"""

c.execute(query_dwh_account)
table = c.fetchall()
c.executemany('INSERT INTO Dim_Account(id_account,id_person,account_type,name,surname,zip,city,country,email,phone_number,birth_date) VALUES (?,?,?,?,?,?,?,?,?,?,?)', table)
conn.commit()

query_dwh_transaction = """
SELECT t.id_transaction,
       t.id_account,
       a.id id_dim_account,
       t.transaction_type,
       t.transaction_date,
       t.transaction_amount
  FROM Stg_Transaction t
       LEFT JOIN
       Dim_Account a ON t.id_Account = a.id_account;
"""
c.execute(query_dwh_transaction)
table = c.fetchall()
c.executemany('INSERT INTO Fact_Transaction(id_transaction,id_account,id_dim_account,transaction_type,transaction_date,transaction_amount) VALUES (?,?,?,?,?,?)', table)
conn.commit()

conn.close()

WITH person_month AS (
    SELECT month,
           a.id_person
      FROM (
                SELECT DISTINCT SUBSTR(d.DateNum, 5, 2) || '.' || SUBSTR(d.DateNum, 1, 4) month
                FROM Dim_Date d
                WHERE d.DateNum BETWEEN 20200215 AND 20200606
           )
           CROSS JOIN
           (
                SELECT DISTINCT id_person
                FROM Dim_Account
                WHERE id_person IN (1234, 345) 
           )
           a
),
transactions AS (
    SELECT a.id_person,
           SUBSTR(t.transaction_date, 5, 2) || '.' || SUBSTR(t.transaction_date, 1, 4) month,
           t.transaction_amount
      FROM Fact_Transaction t
           INNER JOIN
           Dim_Account a ON t.id_dim_account = a.id
     WHERE a.id_person IN (1234, 345) AND 
           t.transaction_date BETWEEN 20200215 AND 20200606
)
SELECT pm.id_person,
       pm.month,
       IFNULL(SUM(t.transaction_amount), 0) transaction_amount
  FROM person_month pm
       LEFT JOIN
       transactions t ON pm.month = t.month AND 
                         pm.id_person = t.id_person
 GROUP BY pm.id_person,
          pm.month
 ORDER BY pm.id_person DESC,
          pm.month;

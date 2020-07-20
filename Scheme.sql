--I used SQLite so there is no date type
--I assume that an account can have only 1 person attached and people can be in the DWH with no account
--I used an existing CSV for Dim_Date

CREATE TABLE Dim_Date (
    DateNum INTEGER PRIMARY KEY,
    Date TEXT,
    YearMonthNum INTEGER,
    Calendar_Quarter TEXT,
    MonthNum INTEGER,
    MonthName TEXT,
    MonthShortName TEXT,
    WeekNum INTEGER,
    DayNumOfYear INTEGER,
    DayNumOfMonth INTEGER,
    DayNumOfWeek INTEGER,
    DayName TEXT,
    DayShortName TEXT,
    Quarter INTEGER,
    YearQuarterNum INTEGER,
    DayNumOfQuarter INTEGER
);

CREATE TABLE Mrr_Account (
    id_account INTEGER NOT NULL PRIMARY KEY,
    id_person INTEGER NOT NULL,
    account_type TEXT
);

CREATE TABLE Mrr_person (
    id_person INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    surname TEXT,
    zip TEXT,
    city TEXT,
    country TEXT,
    email TEXT,
    phone_number TEXT,
    birth_date TEXT
);

CREATE TABLE Mrr_Transaction (
    id_transaction INTEGER NOT NULL, -- transaction 2439 is repeated many times so i drpped the primary key constraint. but this should be addressed later
    id_account INTEGER NOT NULL,
    transaction_type TEXT,
    transaction_date TEXT,
    transaction_amount REAL
);

CREATE TABLE Stg_Account (
    id_account INTEGER NOT NULL,
    id_person INTEGER NOT NULL,
    account_type TEXT,
    name TEXT,
    surname TEXT,
    zip TEXT,
    city TEXT,
    country TEXT,
    email TEXT,
    phone_number TEXT,
    birth_date TEXT
);

CREATE TABLE Dim_Account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_account INTEGER,
    id_person INTEGER NOT NULL,
    account_type TEXT,
    name TEXT,
    surname TEXT,
    zip TEXT,
    city TEXT,
    country TEXT,
    email TEXT,
    phone_number TEXT,
    birth_date TEXT
);

CREATE TABLE Stg_Transaction (
    id_transaction INTEGER NOT NULL,
    id_account INTEGER NOT NULL,
    transaction_type TEXT,
    transaction_date INTEGER,
    transaction_amount REAL
);

CREATE TABLE Fact_Transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_transaction INTEGER NOT NULL,
    id_account INTEGER NOT NULL,
    id_dim_account INTEGER NOT NULL,
    transaction_type TEXT,
    transaction_date INTEGER,
    transaction_amount REAL
);
import MySQLdb as mysql

db = mysql.connect("localhost","root"," ","bank")
#try:
cur=db.cursor()

cur.execute("drop table accounts;")
cur.execute("drop table accountType;")
cur.execute("drop table companies;")
cur.execute("drop table customers;")
cur.execute("drop table loan;")
cur.execute("drop table transaction;")

cur.execute("CREATE TABLE accounts(accountId INT(16), branchID INT(16), customerID INT(16), accountType VARCHAR(16), balance FLOAT(12,2))")
cur.execute("INSERT into accounts VALUES(12345678, 22222, 9234512, 'Checking', 2344.16)")
cur.execute("INSERT into accounts VALUES(87654321, 22222, 9234512, 'Saving', 350.78)")
cur.execute("INSERT into accounts VALUES(90909090, 22222, 9442821, 'Saving', 423678.16)")
cur.execute("INSERT into accounts VALUES(88888888, 12345, 8282828, 'Checking', 7.42)")
cur.execute("INSERT into accounts VALUES(72717077, 12345, 1111111, 'CD', 1000000000.00)")
cur.execute("INSERT into accounts VALUES(45645600, 52802, 6565656, 'Checking', 909.17)")
cur.execute("INSERT into accounts VALUES(11111111, 22222, 2182064, 'Saving', 2.84)")
cur.execute("INSERT into accounts VALUES(22222222, 52802, 7764403, 'Checking', 5632.98)")
cur.execute("INSERT into accounts VALUES(33333333, 22222, 6213973, 'Saving', 123339.74)")
cur.execute("INSERT into accounts VALUES(44444444, 12345, 1234567, 'CD', 9821.73)")
cur.execute("INSERT into accounts VALUES(55555555, 12345, 9876543, 'CD', 9034.56)")
cur.execute("INSERT into accounts VALUES(66666666, 52802, 5198273, 'Checking', 2193.06)")

cur.execute("CREATE TABLE accountType(typeId INT(16), type VARCHAR(16), description VARCHAR(120), rate FLOAT(4,2), length INT(16))")
cur.execute("INSERT into accountType VALUES(123, 'Saving', 'Basic Savings Account', 0.05, 0)")
cur.execute("INSERT into accountType VALUES(456, 'Checking', 'Checking Account', 0.02, 0)")
cur.execute("INSERT into accountType VALUES(789, 'CD', 'Certificate of Deposit', 2.50, 60)")

cur.execute("CREATE TABLE companies(companyId INT(16), companyName VARCHAR(64), phone VARCHAR(16), email VARCHAR(64), contactName VARCHAR(64))")
cur.execute("INSERT into companies VALUES(642789, 'Nebo School District', 8014326621, 'nebo@schooldistrict.com', 'Father Brown')")
cur.execute("INSERT into companies VALUES(182933, 'Face Tatoo Inc.', 8016661234, 'smashyoface@tiger.com', 'Rondo Rousey')")
cur.execute("INSERT into companies VALUES(243881, 'Two Sport Truckers LLC', 8012246651, 'althete@bestever.com', 'Barry Sanders')")
cur.execute("INSERT into companies VALUES(123456, 'All-Time Sack Leading Demolition', 8012217075, 'beast@texans.com', 'JJ Watt')")
cur.execute("INSERT into companies VALUES(524337, 'Make it Rain Inc.', 8019012314, 'greatest@shooter.com', 'Stephen Curry')")
cur.execute("INSERT into companies VALUES(213448, 'Broken Curse LLC', 8013809965, 'finallywon@cubs.com', 'Anthony Rizzo')")

cur.execute("CREATE TABLE customers(customerID INT(16), firstName VARCHAR(64), lastName VARCHAR(64), streetAddress VARCHAR(64), city VARCHAR(32), state VARCHAR(32), zipCode INT(16), email VARCHAR(64), phone VARCHAR(120), companyID INT(16))")
cur.execute("INSERT into customers VALUES(9234512, 'John', 'Diego', '231 S. 1600 N.', 'Provo', 'Utah', 84646, 'jdiego@gmail.com', 8014326621, 642789)")
cur.execute("INSERT into customers VALUES(9442821, 'Mike', 'Tyson', '22 N. Mountain Way', 'American Fork', 'Utah', 84003, 'biteyourear@gmail.com', 5556732121, 182933)")
cur.execute("INSERT into customers VALUES(8282828, 'Hank', 'Aaron', '645 E. 200 S.', 'Mesa', 'Arizona', 72345, 'hrsfordays@gmail.com', 2346745255, 0)")
cur.execute("INSERT into customers VALUES(1111111, 'Barry', 'Sanders', '65 Columbia Way', 'Flagstaff', 'Arizona', 72409, 'althete@bestever.com', 4231227823, 243881)")
cur.execute("INSERT into customers VALUES(6565656, 'Johnny', 'Unitas', '123 TD Lane', 'Lindon', 'Utah', 84652, 'gocolts@gmail.com', 8011919191, 0)")
cur.execute("INSERT into customers VALUES(2182064, 'JJ', 'Watt', '214 N. 2000 S.', 'Provo', 'Utah', 84604, 'beast@texans.com', 8013272621, 123456)")
cur.execute("INSERT into customers VALUES(7764403, 'Robert', 'Mathis', '98 Sack Circle', 'Orem', 'Utah', 84058, 'getlow@gmail.com', 8016521234, 0)")
cur.execute("INSERT into customers VALUES(6213973, 'Stephen', 'Curry', '3 S. Inagame #13', 'Orem', 'Utah', 84097, 'greatest@shooter.com', 8019012314, 524337)")
cur.execute("INSERT into customers VALUES(1234567, 'Joe', 'Ingles', '222 S. Isreal Circle', 'Salt Lake City', 'Utah', 84907, 'jnotsogreat@gmail.com', 8012222222, 0)")
cur.execute("INSERT into customers VALUES(9876543, 'Paul', 'Pierce', '34 E. 340 S.', 'Boulder', 'Colorado', 64213, 'dudesthetruth@shaq.com', 4257873451, 0)")
cur.execute("INSERT into customers VALUES(5198273, 'Anthony', 'Rizzo', '1908 S. No Goat Lane', 'Orem', 'Utah', 84058, 'rocky@gmail.com', 8013809965, 213448)")

cur.execute("CREATE TABLE loan(loanId INT(16), loanDuration VARCHAR(64), interestRate FLOAT(4,2), customerID INT(16), loanAmount FLOAT(12,2), amountOwed FLOAT(12,2), dateOpened DATE)")
cur.execute("INSERT into loan VALUES(1234567, 120, 4.32, 1111111, 10000.00, 4231.77, '2014-11-11')")
cur.execute("INSERT into loan VALUES(6543210, 120, 4.32, 1111111, 10000.00, 14.89, '2014-11-11')")
cur.execute("INSERT into loan VALUES(6432511, 60, 6.89, 6565656, 5000.00, 2731.77, '2012-01-21')")
cur.execute("INSERT into loan VALUES(7231789, 180, 3.69, 6213973, 500000.00, 37781.21, '2015-03-14')")
cur.execute("INSERT into loan VALUES(9887652, 72, 5.28, 2182064, 60000.00, 9876.47, '2015-02-14')")
cur.execute("INSERT into loan VALUES(1299082, 84, 3.40, 9876543, 45000.00, 12731.77, '2014-12-03')")
cur.execute("INSERT into loan VALUES(1678234, 60, 7.09, 2182064, 5000.00, 2231.13, '2012-06-11')")
cur.execute("INSERT into loan VALUES(0934021, 60, 3.82, 6565656, 15000.00, 12316.90, '2016-10-21')")
cur.execute("INSERT into loan VALUES(9876544, 120, 4.89, 1234567, 5000.00, 3731.17, '2016-10-01')")

cur.execute("CREATE TABLE transaction(transName VARCHAR(16), description VARCHAR(128))")
cur.execute("INSERT into transaction VALUES('Withdrawal', 'Withdraw a flat amount from any account. [Total Balance - Withdrawl]')")
cur.execute("INSERT into transaction VALUES('Deposit', 'Deposit a flat amount into any account. [Total Balance + Deposit]')")
cur.execute("INSERT into transaction VALUES('Interest', 'Interest added to loan or CD total balance. [Total balance + Interest earned]')")

cur.execute("CREATE TABLE branch(branchID INT(16), branchName VARCHAR(32), branchAddress VARCHAR(128), city VARCHAR(32), state VARCHAR(32), zipCode INT(16), phone VARCHAR(120), managerEmployeeID VARCHAR(16))")

#except MySQLdb.Error, e:
#print "Error found"

#finally:
db.commit()
db.close()

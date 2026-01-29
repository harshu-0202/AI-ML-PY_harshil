CREATE DATABASE IF NOT EXISTS smart_library;
USE smart_library;

CREATE TABLE Authors(
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) 
);

CREATE TABLE Books(
    book_id INT PRIMARY KEY VARCHAR AUTO_INCREMENT,
    title VARCHAR(150) NOT NULL,
    author_id INT,
    category VARCHAR(50),
    isbn VARCHAR(20) UNIQUE,
    published_date DATE,
    price DECIMAL(10,2),
    available_copies INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Transactions(
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    fine_amount DECIMAL(10,2),
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

INSERT INTO Authors (name, email) VALUES
('Chetan Bhagat', 'chetan@gmail.com'),
('APJ Abdul Kalam', 'kalam@gmail.com'),
('J K Rowling', NULL);

INSERT INTO Books (title, author_id, category, isbn, published_date, price, available_copies) VALUES
('Wings of Fire', 2, 'Science', 'ISBN001', '1999-01-01', 450, 5),
('Harry Potter', 3, 'Fantasy', 'ISBN002', '2005-06-26', 650, 3),
('Revolution 2020', 1, 'Fiction', 'ISBN003', '2016-03-10', 300, 4);

INSERT INTO Members (name, email, phone_number, membership_date) VALUES
('Rahul', 'rahul@gmail.com', '9999999999', '2021-01-10'),
('Amit', NULL, '8888888888', '2023-05-20'),
('Neha', 'neha@gmail.com', '7777777777', '2019-11-15');

INSERT INTO Transactions (member_id, book_id, borrow_date, return_date, fine_amount) VALUES
(1, 1, '2024-01-01', '2024-01-10', 0),
(1, 2, '2024-02-01', '2024-02-20', 50),
(2, 1, '2024-03-01', NULL, 0);

INSERT INTO Members (name, email, phone_number, membership_date)
VALUES ('Kiran', 'kiran@gmail.com', '6666666666', CURDATE());

UPDATE Books
SET available_copies = available_copies - 1
WHERE book_id = 1;

DELETE FROM Members
WHERE member_id NOT IN (
    SELECT DISTINCT member_id
    FROM Transactions
    WHERE borrow_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
);

SELECT * FROM Books
WHERE available_copies > 0;

SELECT * FROM Books
WHERE published_date > '2015-01-01';

SELECT * FROM Books
ORDER BY price DESC
LIMIT 5;

SELECT * FROM Members
WHERE membership_date < '2022-01-01';

SELECT * FROM Books
WHERE category = 'Science' AND price < 500;

SELECT * FROM Books
WHERE NOT available_copies > 0;

SELECT m.member_id, m.name
FROM Members m
LEFT JOIN Transactions t ON m.member_id = t.member_id
GROUP BY m.member_id
HAVING m.membership_date > '2020-01-01'
   OR COUNT(t.transaction_id) > 3;

SELECT * FROM Books
ORDER BY title ASC;

SELECT member_id, COUNT(*) AS total_borrowed
FROM Transactions
GROUP BY member_id;

SELECT category, COUNT(*) AS total_books
FROM Books
GROUP BY category;

SELECT category, COUNT(*) FROM Books GROUP BY category;

SELECT AVG(price) AS avg_price FROM Books;

SELECT book_id, COUNT(*) AS times_borrowed
FROM Transactions
GROUP BY book_id
ORDER BY times_borrowed DESC
LIMIT 1;

SELECT SUM(fine_amount) AS total_fines FROM Transactions;

SELECT b.title, a.name AS author
FROM Books b
INNER JOIN Authors a ON b.author_id = a.author_id;

SELECT m.name, t.book_id
FROM Members m
LEFT JOIN Transactions t ON m.member_id = t.member_id;

SELECT b.title, t.transaction_id
FROM Transactions t
RIGHT JOIN Books b ON t.book_id = b.book_id;


SELECT m.member_id, m.name
FROM Members m
LEFT JOIN Transactions t ON m.member_id = t.member_id
WHERE t.transaction_id IS NULL;

SELECT * FROM Books
WHERE book_id IN (
    SELECT book_id FROM Transactions
    WHERE member_id IN (
        SELECT member_id FROM Members
        WHERE membership_date > '2022-01-01'
    )
);


SELECT * FROM Members
WHERE member_id NOT IN (
    SELECT DISTINCT member_id FROM Transactions
);


SELECT YEAR(published_date) AS year, COUNT(*) 
FROM Books
GROUP BY YEAR(published_date);


SELECT transaction_id,
DATEDIFF(return_date, borrow_date) AS days_taken
FROM Transactions;


SELECT DATE_FORMAT(borrow_date, '%d-%m-%Y') FROM Transactions;


SELECT UPPER(title) FROM Books;


SELECT TRIM(name) FROM Authors;

SELECT IFNULL(email, 'Not Provided') FROM Members;

SELECT book_id,
COUNT(*) AS total_borrows,
RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_no
FROM Transactions
GROUP BY book_id;


SELECT member_id,
COUNT(*) OVER (PARTITION BY member_id ORDER BY borrow_date) AS cumulative_count
FROM Transactions;

SELECT m.member_id, m.name,
CASE
    WHEN MAX(t.borrow_date) >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    THEN 'Active'
    ELSE 'Inactive'
END AS membership_status
FROM Members m
LEFT JOIN Transactions t ON m.member_id = t.member_id
GROUP BY m.member_id;


SELECT title,
CASE
    WHEN YEAR(published_date) > 2020 THEN 'New Arrival'
    WHEN YEAR(published_date) < 2000 THEN 'Classic'
    ELSE 'Regular'
END AS book_type
FROM Books;
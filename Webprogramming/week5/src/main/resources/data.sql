CREATE TABLE member (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    userid VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO member (name, email, age, userid, password) VALUES
('Alice', 'alice@aaa.net', 30, 'alice', '1111'),
('Bob', 'bob@aaa.net', 25, 'bob', '1111'),
('Charlie', 'charlie@aaa.net', 45, 'charlie', '1111'),
('David', 'david@aaa.net', 29, 'david', '1111'),
('Engela', 'engela@aaa.net', 35, 'angela', '1111'),
('Steeve', 'steeve@aaa.net', 21, 'steeve', '1111');
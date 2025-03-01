create database women;

use women;

CREATE TABLE division_dim (
    division_id INT AUTO_INCREMENT PRIMARY KEY,
    division_name VARCHAR(255) UNIQUE
);
SHOW COLUMNS FROM product_fact;


CREATE TABLE department_dim (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) UNIQUE
);

CREATE TABLE class_dim (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(255) UNIQUE
);
select count(*) from class_dim;

CREATE TABLE product_fact (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    clothing_id INT NOT NULL,
    age INT,
    title VARCHAR(255),
    review_text TEXT,
    rating INT,
    recommended_ind TINYINT(1),
    positive_feedback_count INT,
    division_id INT,
    department_id INT,
    class_id INT,
    FOREIGN KEY (division_id) REFERENCES division_dim(division_id),
    FOREIGN KEY (department_id) REFERENCES department_dim(department_id),
    FOREIGN KEY (class_id) REFERENCES class_dim(class_id)
);

select * from class_dim;
SELECT * FROM product_fact;
select * from department_dim;
select * from division_dim;
SELECT * FROM product_fact WHERE division_id IS NULL OR department_id IS NULL OR class_id IS NULL;

SELECT clothing_id, COUNT(*) FROM product_fact GROUP BY clothing_id HAVING COUNT(*) > 1;

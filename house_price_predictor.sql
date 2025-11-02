-- Create database
CREATE DATABASE IF NOT EXISTS house_price_predictor;
USE house_price_predictor;

-- Create main user table
-- CREATE TABLE user_logs (
--     user_id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     gmail VARCHAR(100) UNIQUE NOT NULL,
--     password VARCHAR(800) NOT NULL,
--     logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- Create history table with FOREIGN KEY linked to user_logs
-- CREATE TABLE users_history (
--     history_id INT AUTO_INCREMENT PRIMARY KEY,
--     user_id INT NOT NULL,
--     income INT,
--     rooms INT,
--     house_age INT,
--     bedrooms INT,
--     population INT,
--     people_in_house INT,
--     city VARCHAR(100),
--     predicted_price INT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES user_logs(user_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );
SELECT * FROM users_history;

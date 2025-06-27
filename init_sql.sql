CREATE DATABASE IF NOT EXISTS resume_ranker;
USE resume_db;

CREATE TABLE IF NOT EXISTS resumes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  mobile_number VARCHAR(50),
  skills TEXT,
  company_name TEXT,
  college_name VARCHAR(255),
  designation VARCHAR(255),
  total_experience VARCHAR(50),
  resume_text LONGTEXT
);

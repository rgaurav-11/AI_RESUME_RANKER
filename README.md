AI Resume Ranker
An AI-powered web application to automatically parse, analyse, and rank resumes using Natural Language Processing (NLP) techniques.
Project Overview
The AI Resume Ranker helps recruiters streamline the resume screening process by extracting relevant data (name, email, skills, experience, etc.) from PDF resumes and scoring candidates based on a predefined skill set. Built with Python, Flask, MySQL, and PDF/NLP tools, it features a web UI for uploading resumes and viewing results.
Features
•	Upload PDF resumes via a user-friendly interface
•	Extracts Name, Email, Phone, Skills, Company, College, Designation, Experience
•	Compares extracted skills with job-specific keywords
•	Generates a match score with visual bar
•	Stores all parsed data in a MySQL database
•	Displays results in a styled UI using Bootstrap
Tech Stack
•	Frontend: HTML, CSS, Bootstrap
•	Backend: Python, Flask
•	Database: MySQL (XAMPP local setup)
•	PDF Parsing: PDFMiner
•	NLP: NLTK, Regex
•	IDE: Visual Studio Code

Installation & Setup
1.	Clone the repository
2.	git clone https://github.com/yourusername/ai-resume-ranker.git
3.	cd ai-resume-ranker
4.	Create and activate a virtual environment
5.	python -m venv venv
6.	source venv/bin/activate  # On Windows: venv\Scripts\activate
7.	Install dependencies
8.	pip install -r requirements.txt
9.	Setup MySQL DB using XAMPP
o	Create a database named resume_ranker
o	Import init_sql.sql via phpMyAdmin
10.	Run the app
11.	python app.py
Visit http://127.0.0.1:5000/ in your browser.

 Sample Resumes
Use the sample resumes provided in /sample_resumes for testing the parser.



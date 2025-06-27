import re
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from save_resume import insert_resume_to_db

stop_words = set(stopwords.words('english'))

# IT skills list for scoring
IT_KEYWORDS = [
  'python', 'java', 'c', 'c++', 'c#', 'javascript', 'typescript', 'react', 'angular', 'node.js',
  'flask', 'django', 'spring', 'mysql', 'mongodb', 'sql', 'html', 'css', 'bootstrap', 'tailwind',
  'docker', 'kubernetes', 'jenkins', 'aws', 'azure', 'linux', 'git', 'github', 'tensorflow',
  'pytorch', 'keras', 'pandas', 'numpy', 'scikit-learn', 'tableau', 'power bi', 'selenium',
  'jira', 'postman', 'kafka', 'spark', 'hadoop', 'terraform', 'ansible', 'salesforce', 'pl/sql'
]

# Skills list used for extraction
SKILL_KEYWORDS = [
  'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript', 'TypeScript', 'React', 'Angular', 'Node.js',
  'Flask', 'Django', 'Spring', 'MySQL', 'MongoDB', 'SQL', 'HTML', 'CSS', 'Bootstrap', 'Tailwind',
  'Docker', 'Kubernetes', 'Jenkins', 'AWS', 'Azure', 'Linux', 'Git', 'GitHub', 'TensorFlow',
  'PyTorch', 'Keras', 'Pandas', 'NumPy', 'Scikit-learn', 'Tableau', 'Power BI', 'Selenium',
  'Jira', 'Postman', 'Kafka', 'Spark', 'Hadoop', 'Terraform', 'Ansible', 'Salesforce', 'PL/SQL'
]

DESIGNATION_KEYWORDS = [
  'Software Engineer', 'Senior Software Engineer', 'Frontend Developer', 'Backend Developer',
  'Full Stack Developer', 'Mobile App Developer', 'DevOps Engineer', 'Data Scientist',
  'Data Analyst', 'Machine Learning Engineer', 'Cybersecurity Analyst', 'Project Manager',
  'Product Manager', 'QA Engineer', 'UI/UX Designer', 'Cloud Engineer', 'Intern'
]

def score_resume(skills_text):
    resume_skills = [s.lower().strip() for s in skills_text.split(",")]
    matched = [kw for kw in IT_KEYWORDS if kw in resume_skills]
    missing = [kw for kw in IT_KEYWORDS if kw not in resume_skills]
    score = round((len(matched) / len(IT_KEYWORDS)) * 100, 2)
    return {
        "score": score,
        "matched_skills": ", ".join(matched),
        "missing_skills": ", ".join(missing)
    }

def extract_info(text):
    email = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone = re.search(r'\+?\d[\d\s\-]{8,12}\d', text)
    name = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)
    skills_found = [kw for kw in SKILL_KEYWORDS if kw.lower() in text.lower()]
    college_match = re.findall(r'(?i)(?:college|institute|university) of [A-Za-z &]+', text)
    company_match = re.findall(r'(?i)(?:at|with|from)\s+([A-Z][\w\s&]+(?:Ltd|Technologies|Solutions|Inc)?)', text)
    experience_match = re.findall(r'(?i)([0-9.]+)\s+(years|yrs)\s+experience', text)
    designation_match = re.findall(r'(?i)(?:designation|role|position)[:\-\s]*([A-Za-z\s]{2,40})', text)

    extracted_data = {
        "name": name[0] if name else "N/A",
        "email": email.group() if email else "N/A",
        "mobile_number": phone.group() if phone else "N/A",
        "skills": ", ".join(skills_found) if skills_found else "N/A",
        "company_name": company_match[0] if company_match else "N/A",
        "college_name": college_match[0] if college_match else "N/A",
        "total_experience": experience_match[0][0] + " years" if experience_match else "N/A",
        "designation": designation_match[0].strip() if designation_match else "N/A",
        "resume_text": text
    }

    # Add score and keyword analysis
    extracted_data.update(score_resume(extracted_data["skills"]))
    return extracted_data

def process_resume(file_path):
    text = extract_text(file_path)
    data = extract_info(text)
    insert_resume_to_db(data, text)  # ← this saves it
    return data


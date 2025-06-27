from db_connection import get_connection

def insert_resume_to_db(data, raw_text):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO resumes (name, email, mobile_number, skills, company_name, college_name, designation, total_experience, resume_text)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (
        data.get("name"), data.get("email"), data.get("mobile_number"),
        ', '.join(data.get("skills", [])),
        ', '.join(data.get("company_name", [])),
        data.get("college_name"), data.get("designation"),
        data.get("total_experience"), raw_text
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

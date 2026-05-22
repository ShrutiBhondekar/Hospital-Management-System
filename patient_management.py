from db_connection import connect
from tabulate import tabulate

def add_patient():
    conn = connect()
    cur = conn.cursor()

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    disease = input("Enter Disease: ")

    query = """
    INSERT INTO patients
    (first_name, last_name, gender, age, phone, address, disease, admission_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,CURRENT_DATE)
    """

    cur.execute(query, (
        first_name,
        last_name,
        gender,
        age,
        phone,
        address,
        disease
    ))

    conn.commit()

    print("\nPatient Added Successfully\n")

    cur.close()
    conn.close()


def view_patients():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT patient_id,
               first_name,
               last_name,
               gender,
               age,
               phone,
               disease,
               admission_date
        FROM patients
        ORDER BY patient_id
    """)

    rows = cur.fetchall()

    headers = [
        "Patient ID",
        "First Name",
        "Last Name",
        "Gender",
        "Age",
        "Phone",
        "Disease",
        "Admission Date"
    ]

    print("\n========= PATIENT RECORDS =========\n")

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    cur.close()
    conn.close()
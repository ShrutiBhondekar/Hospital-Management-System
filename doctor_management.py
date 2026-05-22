from db_connection import connect
from tabulate import tabulate
import psycopg2


def add_doctor():

    conn = connect()
    cur = conn.cursor()

    doctor_name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    phone = input("Enter Contact Number: ")

    query = """
    INSERT INTO doctors
    (doctor_name, specialization, phone)
    VALUES (%s,%s,%s)
    """

    try:

        cur.execute(query, (
            doctor_name,
            specialization,
            phone
        ))

        conn.commit()

        print("\n✅ Doctor Added Successfully\n")

    except psycopg2.Error:

        conn.rollback()

        print("\n❌ Invalid Phone Number")
        print("Phone number must contain exactly 10 digits only.\n")

    finally:

        cur.close()
        conn.close()


def view_doctors():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT doctor_id,
               doctor_name,
               specialization,
               phone,
               available
        FROM doctors
        ORDER BY doctor_id
    """)

    rows = cur.fetchall()

    headers = [
        "Doctor ID",
        "Doctor Name",
        "Specialization",
        "Phone",
        "Available"
    ]

    print("\n========= DOCTOR RECORDS =========\n")

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    cur.close()
    conn.close()
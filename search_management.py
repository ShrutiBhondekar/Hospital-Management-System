from db_connection import connect
from tabulate import tabulate


def search_patients():
    print("\n===== SEARCH PATIENTS =====")
    print("Search by: 1. Name  2. Disease  3. Phone  4. Patient ID")
    choice = input("Enter Choice: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        name = input("Enter name (first or last): ")
        cur.execute("""
            SELECT patient_id, first_name, last_name, gender, age,
                   phone, disease, admission_date
            FROM patients
            WHERE LOWER(first_name) LIKE LOWER(%s)
               OR LOWER(last_name)  LIKE LOWER(%s)
            ORDER BY patient_id
        """, (f"%{name}%", f"%{name}%"))

    elif choice == '2':
        disease = input("Enter disease keyword: ")
        cur.execute("""
            SELECT patient_id, first_name, last_name, gender, age,
                   phone, disease, admission_date
            FROM patients
            WHERE LOWER(disease) LIKE LOWER(%s)
            ORDER BY patient_id
        """, (f"%{disease}%",))

    elif choice == '3':
        phone = input("Enter phone number: ")
        cur.execute("""
            SELECT patient_id, first_name, last_name, gender, age,
                   phone, disease, admission_date
            FROM patients
            WHERE phone LIKE %s
            ORDER BY patient_id
        """, (f"%{phone}%",))

    elif choice == '4':
        pid = int(input("Enter Patient ID: "))
        cur.execute("""
            SELECT patient_id, first_name, last_name, gender, age,
                   phone, disease, admission_date
            FROM patients
            WHERE patient_id = %s
        """, (pid,))

    else:
        print("Invalid Choice")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()
    headers = ["Patient ID", "First Name", "Last Name", "Gender",
               "Age", "Phone", "Disease", "Admission Date"]

    print(f"\n🔍 Found {len(rows)} result(s):\n")
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No matching patients found.")

    cur.close()
    conn.close()


def search_doctors():
    print("\n===== SEARCH DOCTORS =====")
    print("Search by: 1. Name  2. Specialization  3. Availability")
    choice = input("Enter Choice: ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        name = input("Enter doctor name: ")
        cur.execute("""
            SELECT doctor_id, doctor_name, specialization, phone, available
            FROM doctors
            WHERE LOWER(doctor_name) LIKE LOWER(%s)
            ORDER BY doctor_id
        """, (f"%{name}%",))

    elif choice == '2':
        spec = input("Enter specialization keyword: ")
        cur.execute("""
            SELECT doctor_id, doctor_name, specialization, phone, available
            FROM doctors
            WHERE LOWER(specialization) LIKE LOWER(%s)
            ORDER BY doctor_id
        """, (f"%{spec}%",))

    elif choice == '3':
        avail = input("Available? (yes/no): ").strip().lower()
        flag = avail in ("yes", "y", "true", "1")
        cur.execute("""
            SELECT doctor_id, doctor_name, specialization, phone, available
            FROM doctors
            WHERE available = %s
            ORDER BY doctor_id
        """, (flag,))

    else:
        print("Invalid Choice")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()
    headers = ["Doctor ID", "Doctor Name", "Specialization", "Phone", "Available"]

    print(f"\n🔍 Found {len(rows)} result(s):\n")
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No matching doctors found.")

    cur.close()
    conn.close()


def search_appointments():
    print("\n===== SEARCH APPOINTMENTS =====")
    print("Search by: 1. Patient ID  2. Doctor ID  3. Date  4. Status")
    choice = input("Enter Choice: ")

    conn = connect()
    cur = conn.cursor()

    base_query = """
        SELECT a.appointment_id,
               p.first_name || ' ' || p.last_name AS patient_name,
               d.doctor_name,
               a.appointment_date,
               a.appointment_time,
               a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors  d ON a.doctor_id  = d.doctor_id
    """

    if choice == '1':
        pid = int(input("Enter Patient ID: "))
        cur.execute(base_query + " WHERE a.patient_id = %s ORDER BY a.appointment_id", (pid,))

    elif choice == '2':
        did = int(input("Enter Doctor ID: "))
        cur.execute(base_query + " WHERE a.doctor_id = %s ORDER BY a.appointment_id", (did,))

    elif choice == '3':
        date = input("Enter Date (YYYY-MM-DD): ")
        cur.execute(base_query + " WHERE a.appointment_date = %s ORDER BY a.appointment_time", (date,))

    elif choice == '4':
        print("Statuses: Scheduled / Completed / Cancelled")
        status = input("Enter Status: ")
        cur.execute(base_query + " WHERE LOWER(a.status) = LOWER(%s) ORDER BY a.appointment_id", (status,))

    else:
        print("Invalid Choice")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()
    headers = ["Appointment ID", "Patient Name", "Doctor Name", "Date", "Time", "Status"]

    print(f"\n🔍 Found {len(rows)} result(s):\n")
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No matching appointments found.")

    cur.close()
    conn.close()


def search_menu():
    print("\n===== SEARCH & FILTER =====")
    print("1. Search Patients")
    print("2. Search Doctors")
    print("3. Search Appointments")
    print("4. Back")

    choice = input("Enter Choice: ")

    if choice == '1':
        search_patients()
    elif choice == '2':
        search_doctors()
    elif choice == '3':
        search_appointments()
    elif choice == '4':
        return
    else:
        print("Invalid Choice")
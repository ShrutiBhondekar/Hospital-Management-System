from db_connection import connect
from tabulate import tabulate
import psycopg2
from datetime import datetime


def book_appointment():

    conn = connect()
    cur = conn.cursor()

    patient_id = int(input("Patient ID: "))
    doctor_id = int(input("Doctor ID: "))
    date = input("Appointment Date (YYYY-MM-DD): ")

    # Time Validation
    while True:

        time = input("Appointment Time (HH:MM): ")

        try:
            datetime.strptime(time, "%H:%M")
            break

        except ValueError:
            print("\n❌ Invalid Time Format")
            print("Please enter time in HH:MM format.\n")

    query = """
    INSERT INTO appointments
    (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (%s,%s,%s,%s)
    """

    try:

        cur.execute(query, (
            patient_id,
            doctor_id,
            date,
            time
        ))

        conn.commit()

        print("\n✅ Appointment Booked Successfully\n")

    except psycopg2.errors.ForeignKeyViolation:

        conn.rollback()

        print("\n❌ Invalid Patient ID or Doctor ID")
        print("Please check if patient and doctor exist.\n")

    except Exception as e:

        conn.rollback()

        print("\n❌ Error:", e)

    finally:

        cur.close()
        conn.close()


def view_appointments():

    conn = connect()
    cur = conn.cursor()

    query = """
    SELECT
        appointment_id,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status
    FROM appointments
    ORDER BY appointment_id
    """

    cur.execute(query)

    rows = cur.fetchall()

    headers = [
        "Appointment ID",
        "Patient ID",
        "Doctor ID",
        "Date",
        "Time",
        "Status"
    ]

    print("\n========= APPOINTMENTS =========\n")

    print(tabulate(rows, headers=headers, tablefmt="grid"))

    cur.close()
    conn.close()
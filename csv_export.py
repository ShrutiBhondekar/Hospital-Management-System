import csv
import os
from db_connection import connect
from datetime import datetime


def get_export_filename(name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.csv"
    return filename


def export_patients():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT patient_id, first_name, last_name, gender, age,
               phone, address, disease, admission_date
        FROM patients
        ORDER BY patient_id
    """)

    rows = cur.fetchall()
    headers = ["Patient ID", "First Name", "Last Name", "Gender", "Age",
               "Phone", "Address", "Disease", "Admission Date"]

    filename = get_export_filename("patients")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"\n✅ Patients exported to: {os.path.abspath(filename)}\n")

    cur.close()
    conn.close()


def export_doctors():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT doctor_id, doctor_name, specialization, phone, available
        FROM doctors
        ORDER BY doctor_id
    """)

    rows = cur.fetchall()
    headers = ["Doctor ID", "Doctor Name", "Specialization", "Phone", "Available"]

    filename = get_export_filename("doctors")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"\n✅ Doctors exported to: {os.path.abspath(filename)}\n")

    cur.close()
    conn.close()


def export_appointments():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT a.appointment_id,
               p.first_name || ' ' || p.last_name AS patient_name,
               d.doctor_name,
               a.appointment_date,
               a.appointment_time,
               a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors  d ON a.doctor_id  = d.doctor_id
        ORDER BY a.appointment_id
    """)

    rows = cur.fetchall()
    headers = ["Appointment ID", "Patient Name", "Doctor Name",
               "Date", "Time", "Status"]

    filename = get_export_filename("appointments")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"\n✅ Appointments exported to: {os.path.abspath(filename)}\n")

    cur.close()
    conn.close()


def export_bills():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT b.bill_id,
               p.first_name || ' ' || p.last_name AS patient_name,
               b.consultation_fee,
               b.medicine_charges,
               b.room_charges,
               b.total_amount,
               b.payment_status
        FROM billing b
        JOIN patients p ON b.patient_id = p.patient_id
        ORDER BY b.bill_id
    """)

    rows = cur.fetchall()
    headers = ["Bill ID", "Patient Name", "Consultation Fee",
               "Medicine Charges", "Room Charges", "Total Amount", "Payment Status"]

    filename = get_export_filename("bills")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"\n✅ Bills exported to: {os.path.abspath(filename)}\n")

    cur.close()
    conn.close()


def export_menu():
    print("\n===== EXPORT TO CSV =====")
    print("1. Export Patients")
    print("2. Export Doctors")
    print("3. Export Appointments")
    print("4. Export Bills")
    print("5. Export All")
    print("6. Back")

    choice = input("Enter Choice: ")

    if choice == '1':
        export_patients()
    elif choice == '2':
        export_doctors()
    elif choice == '3':
        export_appointments()
    elif choice == '4':
        export_bills()
    elif choice == '5':
        export_patients()
        export_doctors()
        export_appointments()
        export_bills()
    elif choice == '6':
        return
    else:
        print("Invalid Choice")
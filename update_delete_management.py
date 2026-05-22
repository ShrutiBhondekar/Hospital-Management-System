from db_connection import connect
from tabulate import tabulate
import psycopg2


# ─────────────────────────── PATIENTS ────────────────────────────

def update_patient():
    conn = connect()
    cur = conn.cursor()

    patient_id = int(input("Enter Patient ID to update: "))

    cur.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    if not cur.fetchone():
        print("\n❌ Patient not found.\n")
        cur.close()
        conn.close()
        return

    print("\nWhat would you like to update?")
    print("1. Phone")
    print("2. Address")
    print("3. Disease")
    choice = input("Enter Choice: ")

    field_map = {'1': ('phone', 'New Phone'), '2': ('address', 'New Address'), '3': ('disease', 'New Disease')}

    if choice not in field_map:
        print("Invalid Choice")
        cur.close()
        conn.close()
        return

    column, prompt = field_map[choice]
    new_value = input(f"{prompt}: ")

    try:
        cur.execute(f"UPDATE patients SET {column} = %s WHERE patient_id = %s", (new_value, patient_id))
        conn.commit()
        print("\n✅ Patient updated successfully.\n")
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


def delete_patient():
    conn = connect()
    cur = conn.cursor()

    patient_id = int(input("Enter Patient ID to delete: "))

    cur.execute("SELECT first_name, last_name FROM patients WHERE patient_id = %s", (patient_id,))
    row = cur.fetchone()

    if not row:
        print("\n❌ Patient not found.\n")
        cur.close()
        conn.close()
        return

    confirm = input(f"Are you sure you want to delete {row[0]} {row[1]}? (yes/no): ")
    if confirm.lower() not in ("yes", "y"):
        print("Cancelled.")
        cur.close()
        conn.close()
        return

    try:
        # Remove dependent records first
        cur.execute("DELETE FROM billing WHERE patient_id = %s", (patient_id,))
        cur.execute("DELETE FROM appointments WHERE patient_id = %s", (patient_id,))
        cur.execute("DELETE FROM medical_records WHERE patient_id = %s", (patient_id,))
        cur.execute("DELETE FROM patient_rooms WHERE patient_id = %s", (patient_id,))
        cur.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
        conn.commit()
        print("\n✅ Patient deleted successfully.\n")
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


# ─────────────────────────── DOCTORS ─────────────────────────────

def update_doctor():
    conn = connect()
    cur = conn.cursor()

    doctor_id = int(input("Enter Doctor ID to update: "))

    cur.execute("SELECT * FROM doctors WHERE doctor_id = %s", (doctor_id,))
    if not cur.fetchone():
        print("\n❌ Doctor not found.\n")
        cur.close()
        conn.close()
        return

    print("\nWhat would you like to update?")
    print("1. Phone")
    print("2. Specialization")
    print("3. Availability")
    choice = input("Enter Choice: ")

    try:
        if choice == '1':
            phone = input("New Phone (10 digits): ")
            cur.execute("UPDATE doctors SET phone = %s WHERE doctor_id = %s", (phone, doctor_id))
        elif choice == '2':
            spec = input("New Specialization: ")
            cur.execute("UPDATE doctors SET specialization = %s WHERE doctor_id = %s", (spec, doctor_id))
        elif choice == '3':
            avail = input("Available? (yes/no): ").strip().lower()
            flag = avail in ("yes", "y")
            cur.execute("UPDATE doctors SET available = %s WHERE doctor_id = %s", (flag, doctor_id))
        else:
            print("Invalid Choice")
            return

        conn.commit()
        print("\n✅ Doctor updated successfully.\n")

    except psycopg2.Error as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


def delete_doctor():
    conn = connect()
    cur = conn.cursor()

    doctor_id = int(input("Enter Doctor ID to delete: "))

    cur.execute("SELECT doctor_name FROM doctors WHERE doctor_id = %s", (doctor_id,))
    row = cur.fetchone()

    if not row:
        print("\n❌ Doctor not found.\n")
        cur.close()
        conn.close()
        return

    confirm = input(f"Are you sure you want to delete Dr. {row[0]}? (yes/no): ")
    if confirm.lower() not in ("yes", "y"):
        print("Cancelled.")
        cur.close()
        conn.close()
        return

    try:
        cur.execute("DELETE FROM appointments WHERE doctor_id = %s", (doctor_id,))
        cur.execute("DELETE FROM doctors WHERE doctor_id = %s", (doctor_id,))
        conn.commit()
        print("\n✅ Doctor deleted successfully.\n")
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


# ──────────────────────── APPOINTMENTS ───────────────────────────

def update_appointment():
    conn = connect()
    cur = conn.cursor()

    appt_id = int(input("Enter Appointment ID to update: "))

    cur.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appt_id,))
    if not cur.fetchone():
        print("\n❌ Appointment not found.\n")
        cur.close()
        conn.close()
        return

    print("\nWhat would you like to update?")
    print("1. Status  (Scheduled / Completed / Cancelled)")
    print("2. Date")
    print("3. Time")
    choice = input("Enter Choice: ")

    try:
        if choice == '1':
            status = input("New Status: ")
            cur.execute("UPDATE appointments SET status = %s WHERE appointment_id = %s", (status, appt_id))
        elif choice == '2':
            date = input("New Date (YYYY-MM-DD): ")
            cur.execute("UPDATE appointments SET appointment_date = %s WHERE appointment_id = %s", (date, appt_id))
        elif choice == '3':
            time = input("New Time (HH:MM): ")
            cur.execute("UPDATE appointments SET appointment_time = %s WHERE appointment_id = %s", (time, appt_id))
        else:
            print("Invalid Choice")
            return

        conn.commit()
        print("\n✅ Appointment updated successfully.\n")

    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


def delete_appointment():
    conn = connect()
    cur = conn.cursor()

    appt_id = int(input("Enter Appointment ID to delete: "))

    cur.execute("SELECT appointment_id FROM appointments WHERE appointment_id = %s", (appt_id,))
    if not cur.fetchone():
        print("\n❌ Appointment not found.\n")
        cur.close()
        conn.close()
        return

    confirm = input(f"Delete appointment #{appt_id}? (yes/no): ")
    if confirm.lower() not in ("yes", "y"):
        print("Cancelled.")
        cur.close()
        conn.close()
        return

    try:
        cur.execute("DELETE FROM appointments WHERE appointment_id = %s", (appt_id,))
        conn.commit()
        print("\n✅ Appointment deleted successfully.\n")
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


# ─────────────────────────── BILLING ─────────────────────────────

def update_bill_status():
    conn = connect()
    cur = conn.cursor()

    bill_id = int(input("Enter Bill ID to update: "))

    cur.execute("SELECT payment_status FROM billing WHERE bill_id = %s", (bill_id,))
    row = cur.fetchone()

    if not row:
        print("\n❌ Bill not found.\n")
        cur.close()
        conn.close()
        return

    print(f"Current Status: {row[0]}")
    new_status = input("New Payment Status (Pending / Paid / Cancelled): ")

    try:
        cur.execute("UPDATE billing SET payment_status = %s WHERE bill_id = %s", (new_status, bill_id))
        conn.commit()
        print("\n✅ Bill status updated successfully.\n")
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}\n")
    finally:
        cur.close()
        conn.close()


# ─────────────────────────── MENUS ───────────────────────────────

def update_menu():
    print("\n===== UPDATE RECORDS =====")
    print("1. Update Patient")
    print("2. Update Doctor")
    print("3. Update Appointment")
    print("4. Update Bill Payment Status")
    print("5. Back")

    choice = input("Enter Choice: ")

    if choice == '1':
        update_patient()
    elif choice == '2':
        update_doctor()
    elif choice == '3':
        update_appointment()
    elif choice == '4':
        update_bill_status()
    elif choice == '5':
        return
    else:
        print("Invalid Choice")


def delete_menu():
    print("\n===== DELETE RECORDS =====")
    print("1. Delete Patient")
    print("2. Delete Doctor")
    print("3. Delete Appointment")
    print("4. Back")

    choice = input("Enter Choice: ")

    if choice == '1':
        delete_patient()
    elif choice == '2':
        delete_doctor()
    elif choice == '3':
        delete_appointment()
    elif choice == '4':
        return
    else:
        print("Invalid Choice")
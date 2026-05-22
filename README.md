# 🏥 Hospital Management System

**Author:** Shruti Deepak Bhondekar | **Student ID:** 540418116 | **Tutorial:** 26 | **Tutor:** Niousha Nizomi

---

## 📋 Overview

A **Command-Line Interface (CLI) based Hospital Management System** built with **Python** and **PostgreSQL**. The system manages end-to-end hospital operations including patient records, doctor management, appointments, billing, and data exports — all through a terminal interface.

---

## 🛠️ Technologies Used

| Component   | Technology              |
|-------------|-------------------------|
| Language    | Python 3                |
| Database    | PostgreSQL              |
| DB Library  | psycopg2                |
| Display     | tabulate                |
| Interface   | Command-Line (CLI)      |

---

## 🗃️ Database Schema

The system uses **7 relational tables** in PostgreSQL:

```
patients        → Core patient records
doctors         → Doctor profiles & availability
appointments    → Patient-doctor scheduling
medical_records → Diagnosis, treatment, medicines
billing         → Consultation, medicine, room charges
rooms           → Room inventory & type
patient_rooms   → Room assignment & discharge tracking
```

---

## 📁 Project Structure

```
hospital_management/
│
├── main.py                    # Entry point — main menu loop
├── db_connection.py           # PostgreSQL connection handler
├── patient_management.py      # Add & view patients
├── doctor_management.py       # Add & view doctors
├── appointment_management.py  # Book & view appointments
├── billing_management.py      # Generate bills
├── update_delete_management.py# Update & delete records
├── search_management.py       # Search & filter records
├── csv_export.py              # Export data to CSV
└── SQLstmts.sql               # Database setup script
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites

```bash
pip install psycopg2
pip install tabulate
```

### 2. Database Setup

Connect to your PostgreSQL server and run the SQL setup script:

```bash
psql -h <host> -U <username> -d <database> -f SQLstmts.sql
```

### 3. Configure Database Connection

Edit `db_connection.py` with your credentials:

```python
import psycopg2
def connect():
    return psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )
```

### 4. Run the Application

```bash
python main.py
```

---

## 🖥️ Runtime Screenshots

### Main Menu

```
===== Hospital Management System =====
1.  Add Patient
2.  View Patients
3.  Add Doctor
4.  View Doctors
5.  Book Appointment
6.  View Appointments
7.  Generate Bill
8.  Search & Filter
9.  Update Records
10. Delete Records
11. Export to CSV
12. Exit

Enter Choice:
```

---

### 1. Add Patient

```
Enter First Name: Sarah
Enter Last Name: Mitchell
Enter Gender: Female
Enter Age: 34
Enter Phone: 0412345678
Enter Address: 12 King Street, Sydney
Enter Disease: Hypertension

Patient Added Successfully
```

---

### 2. View Patients

```
========= PATIENT RECORDS =========

+------------+------------+-----------+--------+-----+------------+--------------+----------------+
| Patient ID | First Name | Last Name | Gender | Age | Phone      | Disease      | Admission Date |
+============+============+===========+========+=====+============+==============+================+
|          1 | Sarah      | Mitchell  | Female |  34 | 0412345678 | Hypertension | 2025-05-01     |
+------------+------------+-----------+--------+-----+------------+--------------+----------------+
|          2 | James      | Carter    | Male   |  47 | 0498765432 | Diabetes     | 2025-05-03     |
+------------+------------+-----------+--------+-----+------------+--------------+----------------+
|          3 | Priya      | Sharma    | Female |  29 | 0423456789 | Asthma       | 2025-05-10     |
+------------+------------+-----------+--------+-----+------------+--------------+----------------+
```

---

### 3. Add Doctor

```
Enter Doctor Name: Dr. Emily Nguyen
Enter Specialization: Cardiology
Enter Contact Number: 0287654321

✅ Doctor Added Successfully
```

> **Note:** Phone number must be exactly 10 digits. Invalid formats are rejected:
> ```
> ❌ Invalid Phone Number
> Phone number must contain exactly 10 digits only.
> ```

---

### 4. View Doctors

```
========= DOCTOR RECORDS =========

+-----------+------------------+----------------+------------+-----------+
| Doctor ID | Doctor Name      | Specialization | Phone      | Available |
+===========+==================+================+============+===========+
|         1 | Dr. Emily Nguyen | Cardiology     | 0287654321 | True      |
+-----------+------------------+----------------+------------+-----------+
|         2 | Dr. Raj Patel    | Neurology      | 0298765432 | True      |
+-----------+------------------+----------------+------------+-----------+
|         3 | Dr. Lisa Wong    | Orthopedics    | 0277654321 | False     |
+-----------+------------------+----------------+------------+-----------+
```

---

### 5. Book Appointment

```
Patient ID: 1
Doctor ID: 1
Appointment Date (YYYY-MM-DD): 2025-05-20
Appointment Time (HH:MM): 10:30

✅ Appointment Booked Successfully
```

> **Time validation** — invalid formats are caught in a loop:
> ```
> Appointment Time (HH:MM): 25:99
> ❌ Invalid Time Format
> Please enter time in HH:MM format.
> Appointment Time (HH:MM):
> ```

> **Foreign key validation** — non-existent IDs are caught:
> ```
> ❌ Invalid Patient ID or Doctor ID
> Please check if patient and doctor exist.
> ```

---

### 6. View Appointments

```
========= APPOINTMENTS =========

+----------------+------------+-----------+------------+-------+-----------+
| Appointment ID | Patient ID | Doctor ID | Date       | Time  | Status    |
+================+============+===========+============+=======+===========+
|              1 |          1 |         1 | 2025-05-20 | 10:30 | Scheduled |
+----------------+------------+-----------+------------+-------+-----------+
|              2 |          2 |         2 | 2025-05-21 | 14:00 | Scheduled |
+----------------+------------+-----------+------------+-------+-----------+
|              3 |          3 |         1 | 2025-05-15 | 09:00 | Completed |
+----------------+------------+-----------+------------+-------+-----------+
```

---

### 7. Generate Bill

```
Patient ID: 1
Consultation Fee: 150.00
Medicine Charges: 75.50
Room Charges: 200.00

Bill Generated Successfully
Total Amount: 425.5
```

---

### 8. Search & Filter

```
===== SEARCH & FILTER =====
1. Search Patients
2. Search Doctors
3. Search Appointments
4. Back

Enter Choice: 1

===== SEARCH PATIENTS =====
Search by: 1. Name  2. Disease  3. Phone  4. Patient ID
Enter Choice: 2
Enter disease keyword: diab

🔍 Found 1 result(s):

+------------+------------+-----------+--------+-----+------------+----------+----------------+
| Patient ID | First Name | Last Name | Gender | Age | Phone      | Disease  | Admission Date |
+============+============+===========+========+=====+============+==========+================+
|          2 | James      | Carter    | Male   |  47 | 0498765432 | Diabetes | 2025-05-03     |
+------------+------------+-----------+--------+-----+------------+----------+----------------+
```

---

### 9. Update Records

```
===== UPDATE RECORDS =====
1. Update Patient
2. Update Doctor
3. Update Appointment
4. Update Bill Payment Status
5. Back

Enter Choice: 3

Enter Appointment ID to update: 2

What would you like to update?
1. Status  (Scheduled / Completed / Cancelled)
2. Date
3. Time
Enter Choice: 1
New Status: Completed

✅ Appointment updated successfully.
```

---

### 10. Delete Records

```
===== DELETE RECORDS =====
1. Delete Patient
2. Delete Doctor
3. Delete Appointment
4. Back

Enter Choice: 1

Enter Patient ID to delete: 3
Are you sure you want to delete Priya Sharma? (yes/no): yes

✅ Patient deleted successfully.
```

> All related records (billing, appointments, medical records, room assignments) are automatically removed before the patient is deleted to maintain referential integrity.

---

### 11. Export to CSV

```
===== EXPORT TO CSV =====
1. Export Patients
2. Export Doctors
3. Export Appointments
4. Export Bills
5. Export All
6. Back

Enter Choice: 5

✅ Patients exported to: /home/user/patients_20250522_143012.csv

✅ Doctors exported to: /home/user/doctors_20250522_143012.csv

✅ Appointments exported to: /home/user/appointments_20250522_143012.csv

✅ Bills exported to: /home/user/bills_20250522_143012.csv
```

> Files are timestamped automatically in the format `tablename_YYYYMMDD_HHMMSS.csv`.

---

## ✨ Key Features Summary

| Feature | Description |
|---|---|
| 🧑‍⚕️ Patient Management | Add, view, update, delete patient records |
| 👨‍⚕️ Doctor Management | Add, view, update, delete doctors with phone validation |
| 📅 Appointments | Book, view, update, cancel with time & FK validation |
| 💳 Billing | Generate itemised bills with auto-calculated totals |
| 🔍 Search & Filter | Search by name, ID, disease, specialization, date, status |
| ✏️ Update Records | Selective field updates across all entities |
| 🗑️ Delete Records | Safe deletion with confirmation prompts & cascade cleanup |
| 📤 CSV Export | Timestamped exports for all major tables |

---

## 🔒 Data Integrity & Error Handling

- **Foreign Key Validation** — Invalid patient/doctor IDs are caught on appointment booking
- **Phone Format Check** — Doctors' phone numbers enforced as exactly 10 digits via a DB constraint
- **Time Format Validation** — Appointment times validated with `datetime.strptime` in a retry loop
- **Cascade Delete** — Deleting a patient removes all linked billing, appointments, medical records, and room assignments
- **Transaction Rollback** — All write operations use `try/except/finally` with `conn.rollback()` on failure
- **Confirmation Prompts** — Delete operations require explicit `yes/no` confirmation

---

## 🔄 System Flowchart

```
        Start
          │
   Connect to Database
          │
    Display Main Menu
          │
      Enter Choice
          │
     ┌────┴────┐
   Valid?      No ──► Show Error
     │
    Yes
     │
  Process Option
          │
    (loop back or)
         Exit
```

---

## 📝 Notes

- The `admission_date` for new patients is automatically set to `CURRENT_DATE`
- Default appointment status is `'Scheduled'`
- Default bill payment status is `'Pending'`
- Doctor availability defaults to `TRUE` on creation

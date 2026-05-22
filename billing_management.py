from db_connection import connect

def generate_bill():
    conn = connect()
    cur = conn.cursor()

    patient_id = int(input("Patient ID: "))
    consultation_fee = float(input("Consultation Fee: "))
    medicine_charges = float(input("Medicine Charges: "))
    room_charges = float(input("Room Charges: "))

    total = consultation_fee + medicine_charges + room_charges

    query = """
    INSERT INTO billing
    (patient_id,
     consultation_fee,
     medicine_charges,
     room_charges,
     total_amount,
     payment_status)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cur.execute(query, (
        patient_id,
        consultation_fee,
        medicine_charges,
        room_charges,
        total,
        "Pending"
    ))

    conn.commit()

    print("Bill Generated Successfully")
    print("Total Amount:", total)

    cur.close()
    conn.close()
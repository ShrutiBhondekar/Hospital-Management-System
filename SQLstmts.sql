
-- Connect to database before running below tables

-- Patient Table
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    phone VARCHAR(15),
    address TEXT,
    disease TEXT,
    admission_date DATE
);

-- Doctor Table
CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(15),
    available BOOLEAN DEFAULT TRUE
);

-- Appointments Table
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    doctor_id INT REFERENCES doctors(doctor_id),
    appointment_date DATE,
    appointment_time TIME,
    status VARCHAR(20) DEFAULT 'Scheduled'
);

-- Medical Records Table
CREATE TABLE medical_records (
    record_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    diagnosis TEXT,
    treatment TEXT,
    medicines TEXT,
    record_date DATE DEFAULT CURRENT_DATE
);

-- Billing Table
CREATE TABLE billing (
    bill_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    consultation_fee NUMERIC(10,2),
    medicine_charges NUMERIC(10,2),
    room_charges NUMERIC(10,2),
    total_amount NUMERIC(10,2),
    payment_status VARCHAR(20)
);

-- Rooms Table
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10),
    room_type VARCHAR(50),
    availability BOOLEAN DEFAULT TRUE
);

-- Patient Room Assignment
CREATE TABLE patient_rooms (
    assignment_id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(patient_id),
    room_id INT REFERENCES rooms(room_id),
    admission_date DATE,
    discharge_date DATE
);



ALTER TABLE doctors
ADD CONSTRAINT doctor_phone_check
CHECK (phone ~ '^[0-9]{10}$');
import psycopg2
def connect():
    return psycopg2.connect(
        host="awsprddbs4836.shared.sydney.edu.au",
        database="y26s1c9120_sbho0792",
        user="y26s1c9120_sbho0792",
        password="Shruti@123"
    )
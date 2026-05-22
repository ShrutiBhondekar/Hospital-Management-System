from patient_management import *
from doctor_management import *
from appointment_management import *
from billing_management import *
from csv_export import export_menu
from search_management import search_menu
from update_delete_management import update_menu, delete_menu


def main():

    while True:

        print("\n===== Hospital Management System =====")
        print("1.  Add Patient")
        print("2.  View Patients")
        print("3.  Add Doctor")
        print("4.  View Doctors")
        print("5.  Book Appointment")
        print("6.  View Appointments")
        print("7.  Generate Bill")
        print("8.  Search & Filter")
        print("9.  Update Records")
        print("10. Delete Records")
        print("11. Export to CSV")
        print("12. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            add_doctor()
        elif choice == '4':
            view_doctors()
        elif choice == '5':
            book_appointment()
        elif choice == '6':
            view_appointments()
        elif choice == '7':
            generate_bill()
        elif choice == '8':
            search_menu()
        elif choice == '9':
            update_menu()
        elif choice == '10':
            delete_menu()
        elif choice == '11':
            export_menu()
        elif choice == '12':
            print("Thank You")
            break
        else:
            print("Invalid Choice")


main()
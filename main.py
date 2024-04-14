
import psycopg2
from member_functions import register_member, update_member_profile, display_member_dashboard, schedule_management
from trainer_functions import set_trainer_availability, view_member_by_name
from admin_functions import room_booking_management, equipment_maintenance, class_schedule_update, billing_and_payment

def create_connection():
    try:
        return psycopg2.connect(
            host="localhost",
            database="healthfitnessclub",
            user="postgres",
            password="student1",
            port=5432
        )
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def main():
    conn = create_connection()
    if not conn:
        print("Failed to connect to the database.")
        return

    print("Welcome to the Health and Fitness Club Management System")
    role = input("Please enter your role (member/trainer/admin): ").lower()

    if role not in ['member', 'trainer', 'admin']:
        print("Invalid role specified. Exiting application.")
        return

    while True:
        if role == 'member':
            print("\n1: Register as New Member")
            print("2: Update Your Profile")
            print("3: View Your Dashboard")
            print("4: Manage Your Schedule")
            print("0: Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register_member(conn)
            elif choice == '2':
                update_member_profile(conn)
            elif choice == '3':
                display_member_dashboard(conn)
            elif choice == '4':
                schedule_management(conn)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

        elif role == 'trainer':
            print("\n1: Set Your Availability")
            print("2: View Member By Name")
            print("0: Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                set_trainer_availability(conn)
            elif choice == '2':
                view_member_by_name(conn)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

        elif role == 'admin':
            print("\n1: Manage Room Bookings")
            print("2: Manage Equipment Maintenance")
            print("3: Update Class Schedules")
            print("4: Billing and Payment Processing")
            print("0: Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                room_booking_management(conn)
            elif choice == '2':
                equipment_maintenance(conn)
            elif choice == '3':
                class_schedule_update(conn)
            elif choice == '4':
                billing_and_payment(conn)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    print("Thank you for using the Health and Fitness Club Management System.")
    conn.close()

if __name__ == "__main__":
    main()

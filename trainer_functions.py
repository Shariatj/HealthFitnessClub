import psycopg2

def set_trainer_availability(conn):
    trainer_id = input("Enter your trainer ID: ")
    new_start_time = input("Enter new start availability time (HH:MM, 24-hour format): ")
    new_end_time = input("Enter new end availability time (HH:MM, 24-hour format): ")

    try:
        cur = conn.cursor()
        # Update the trainer's availability times
        cur.execute("UPDATE Trainer SET AvailabilityStart = %s, AvailabilityEnd = %s WHERE TrainerID = %s;",
                    (new_start_time, new_end_time, trainer_id))
        conn.commit()
        print("Availability updated successfully.")
    except psycopg2.Error as e:
        print(f"Error updating trainer availability: {e}")
        conn.rollback()
    finally:
        cur.close()

def view_member_by_name(conn):
    member_name_query = input("Enter the member's name or part of it to search: ")

    try:
        cur = conn.cursor()
        # Using ILIKE for case-insensitive partial matching
        cur.execute("SELECT MemberID, Name, Email, DateOfBirth FROM Member WHERE Name ILIKE %s;",
                    ('%' + member_name_query + '%',))
        results = cur.fetchall()

        if results:
            print("\nMember Details Found:")
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]}, Email: {result[2]}, Date of Birth: {result[3]}")
        else:
            print("No members found matching the search criteria.")
    except psycopg2.Error as e:
        print(f"Error retrieving member data: {e}")
    finally:
        cur.close()



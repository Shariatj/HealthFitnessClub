import psycopg2

def room_booking_management(conn):
    action = input("Choose action: 1 for Book, 2 for View Bookings, 3 for Cancel Booking: ")
    if action == '1':
        room_name = input("Enter room name: ")
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        booking_start = input("Enter booking start time (HH:MM): ")
        booking_end = input("Enter booking end time (HH:MM): ")
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Room (RoomName, Date, StartTime, EndTime)
                    VALUES (%s, %s, %s, %s);
                """, (room_name, booking_date, booking_start, booking_end))
                conn.commit()
                print("Room booking added successfully.")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error managing room booking: {e}")
    elif action == '2':
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Room;")
                bookings = cur.fetchall()
                for booking in bookings:
                    print(f"Room ID: {booking[0]}, Name: {booking[1]}, Date: {booking[2]}, Start: {booking[3]}, End: {booking[4]}")
        except psycopg2.Error as e:
            print(f"Error viewing room bookings: {e}")
    elif action == '3':
        room_id = input("Enter the Room ID to cancel booking: ")
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM Room WHERE RoomID = %s;", (room_id,))
                conn.commit()
                print("Room booking cancelled successfully.")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error cancelling room booking: {e}")
    else:
        print("Invalid action selected.")

def equipment_maintenance(conn):
    equipment_id = input("Enter Equipment ID to update: ")
    new_status = input("Enter new equipment status: ")
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE Equipment SET Status = %s WHERE EquipmentID = %s;", (new_status, equipment_id))
            conn.commit()
            print("Equipment status updated successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error updating equipment status: {e}")

def class_schedule_update(conn):
    class_id = input("Enter Class ID to update: ")
    new_date = input("Enter new date for class (YYYY-MM-DD): ")
    new_time = input("Enter new time for class (HH:MM): ")
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE Class SET Date = %s, Time = %s WHERE ClassID = %s;", (new_date, new_time, class_id))
            conn.commit()
            print("Class schedule updated successfully.")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error updating class schedule: {e}")

def billing_and_payment(conn, amount):
    member_id = input("Enter Member ID to process the payment for: ")
    amount_given = input("Enter amount to record: ")
    try:
        if amount_given != amount:
            print("Amount given does not match the expected amount. Transaction cancelled.")
            return
        with conn.cursor() as cur:
            cur.execute("INSERT INTO Payment (MemberID, Amount, Date) VALUES (%s, %s, CURRENT_DATE);", (member_id, amount))
            conn.commit()
            print("Payment processed and recorded successfully.")
            print("Payment details:")
            cur.execute("SELECT * FROM Payment WHERE MemberID = %s ORDER BY Date DESC LIMIT 1;", (member_id,))
            payments = cur.fetchall()
            for payment in payments:
                print(f"Member ID: {payment[1]}, Amount: {payment[2]}, Date: {payment[3]}")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error processing payment: {e}")

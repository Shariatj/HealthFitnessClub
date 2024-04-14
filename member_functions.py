import psycopg2
import sys
from datetime import datetime
from admin_functions import *

def register_member(conn):
    print("Registering a new member:")
    name = input("Enter member's name: ")
    email = input("Enter member's email: ")
    date_of_birth = input("Enter member's date of birth (YYYY-MM-DD): ")

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO Member (Name, Email, DateOfBirth) VALUES (%s, %s, %s) RETURNING MemberID",
                    (name, email, date_of_birth))
        member_id = cur.fetchone()[0]
        conn.commit()

        # Now prompt to enter fitness goals and health metrics optionally
        if input("Add fitness goals? (y/n): ").lower() == 'y':
            add_fitness_goals(conn, member_id)
        if input("Record health metrics? (y/n): ").lower() == 'y':
            add_health_metrics(conn, member_id)

        print("Member registered successfully, Member ID:", member_id)
    except psycopg2.Error as e:
        print(f"Failed to register member: {e}")
        conn.rollback()
    finally:
        cur.close()

def add_fitness_goals(conn, member_id):
    print("Entering fitness goals:")
    height = input("Enter height in cm: ")
    weight = input("Enter weight in kg: ")

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO FitnessGoals (MemberID, Height, Weight) VALUES (%s, %s, %s)",
                    (member_id, height, weight))
        conn.commit()
        print("Fitness goals added successfully.")
    except psycopg2.Error as e:
        print(f"Failed to add fitness goals: {e}")
        conn.rollback()
    finally:
        cur.close()

def add_health_metrics(conn, member_id):
    print("Recording health metrics:")
    height = input("Enter current height in cm: ")
    weight = input("Enter current weight in kg: ")

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO HealthMetrics (MemberID, Height, Weight) VALUES (%s, %s, %s)",
                    (member_id, height, weight))
        conn.commit()
        print("Health metrics recorded successfully.")
    except psycopg2.Error as e:
        print(f"Failed to record health metrics: {e}")
        conn.rollback()
    finally:
        cur.close()

def update_member_profile(conn):
    member_id = input("Enter the member's ID you want to update: ")
    print("Updating basic profile information (leave blank to skip particular updates):")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")

    try:
        cur = conn.cursor()
        updates = []
        params = []

        if name:
            updates.append("Name = %s")
            params.append(name)
        if email:
            updates.append("Email = %s")
            params.append(email)
        if date_of_birth:
            updates.append("DateOfBirth = %s")
            params.append(date_of_birth)

        if updates:
            params.append(member_id)
            update_query = f"UPDATE Member SET {', '.join(updates)} WHERE MemberID = %s;"
            cur.execute(update_query, tuple(params))
            conn.commit()
            print("Basic member profile updated successfully.")

        if input("Would you like to update fitness goals? (y/n): ").lower().startswith('y'):
            update_fitness_goals(cur, member_id)

        if input("Would you like to update health metrics? (y/n): ").lower().startswith('y'):
            update_health_metrics(cur, member_id)

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Failed to update member profile: {e}")
    finally:
        cur.close()

def update_fitness_goals(cur, member_id):
    print("Enter new fitness goals (leave blank to skip):")
    height = input("New height in cm: ")
    weight = input("New weight in kg: ")

    update_fields = []
    params = []

    if height:
        update_fields.append("Height = %s")
        params.append(height)
    if weight:
        update_fields.append("Weight = %s")
        params.append(weight)

    if update_fields:
        params.append(member_id)
        query = f"UPDATE FitnessGoals SET {', '.join(update_fields)} WHERE MemberID = %s;"
        cur.execute(query, params)
        print("Fitness goals updated successfully.")

def update_health_metrics(cur, member_id):
    print("Enter new health metrics (leave blank to skip):")
    height = input("New height in cm: ")
    weight = input("New weight in kg: ")

    update_fields = []
    params = []

    if height:
        update_fields.append("Height = %s")
        params.append(height)
    if weight:
        update_fields.append("Weight = %s")
        params.append(weight)

    if update_fields:
        params.append(member_id)
        query = f"UPDATE HealthMetrics SET {', '.join(update_fields)} WHERE MemberID = %s;"
        cur.execute(query, params)
        print("Health metrics updated successfully.")

def display_member_dashboard(conn):
    member_id = input("Enter member's ID for dashboard display: ")
    try:
        cur = conn.cursor()
        print("\nDisplaying member dashboard...")

        cur.execute("SELECT GoalID, Height, Weight FROM FitnessGoals WHERE MemberID = %s;", (member_id,))
        goals = cur.fetchall()
        print("\nFitness Goals:")
        if goals:
            for goal in goals:
                print(f"Goal ID: {goal[0]}, Height: {float(goal[1])} cm, Weight: {float(goal[2])} kg")
        else:
            print("No fitness goals found.")

        cur.execute("SELECT MetricID, Height, Weight FROM HealthMetrics WHERE MemberID = %s;", (member_id,))
        metrics = cur.fetchall()
        print("\nHealth Metrics:")
        if metrics:
            for metric in metrics:
                print(f"Metric ID: {metric[0]}, Height: {float(metric[1])} cm, Weight: {float(metric[2])} kg")
        else:
            print("No health metrics found.")

    except psycopg2.Error as e:
        print(f"Error fetching dashboard data: {e}")
    finally:
        cur.close()

def schedule_management(conn):
    member_id = input("Enter member's ID to schedule: ")
    print("Type of session (1: Personal Training, 2: Group Fitness Class):")
    sess_type = input("Enter choice: ")

    if sess_type == '1':
        trainer_id = input("Enter trainer's ID: ")
        date = input("Enter session date (YYYY-MM-DD): ")
        time = input("Enter time (HH:MM): ")
        try:
            time = datetime.strptime(time, "%H:%M").time()
            cur = conn.cursor()
            cur.execute("SELECT AvailabilityStart, AvailabilityEnd FROM Trainer WHERE TrainerID = %s;", (trainer_id,))
            availability = cur.fetchone()
            if availability and (availability[0] <= time <= availability[1]):
                cur.execute("INSERT INTO Session (Date, Time, TrainerID, MemberID) VALUES (%s, %s, %s, %s)",
                        (date, time, trainer_id, member_id))
                conn.commit()
                amount = 100
                print("Amount to be paid: ", amount)
                print("would you like to pay now? (y/n)")
                pay = input()
                if pay == 'y':
                    billing_and_payment(conn, amount)
                else:
                    print("You can't schedule without payment.")
            else:
                print("Trainer is not available at the specified time.")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Failed to schedule personal training: {e}")
        finally:
            cur.close()
    elif sess_type == '2':
        try:
            cur = conn.cursor()
            cur.execute("SELECT ClassID FROM Class;")
            classes = cur.fetchall()
            print("Here are the available fitness classes:")
            for cls in classes:
                print(cls[0])

            class_id = input("Enter fitness class ID: ")
            class_ids= [str(cls[0]) for cls in classes]
            if class_id not in class_ids:
                print("Invalid class ID.")
                return
            else:
                amount = 50
                print("Amount to be paid: ", amount)
                print("would you like to pay now? (y/n)")
                pay = input()
                if pay == 'y':
                    billing_and_payment(conn, amount)
                else:
                    print("You can't schedule without payment.")

        except psycopg2.Error as e:
            conn.rollback()
            print(f"Failed to register for fitness class: {e}")
        finally:
            cur.close()
    else:
        print("Invalid session type.")

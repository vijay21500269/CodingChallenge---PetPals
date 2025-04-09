import sys
from util.DBConnUtil import get_db_connection
import mysql.connector


def list_available_pets():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT pet_id, name, age, breed, pet_type, dog_breed, cat_color FROM pets")
        pets = cursor.fetchall()
        print("\n--- Available Pets ---")
        for pet in pets:
            print(f"ID: {pet[0]}, Name: {pet[1]}, Age: {pet[2]}, Breed: {pet[3]}, Type: {pet[4]}", end='')
            if pet[4] == 'Dog':
                print(f", Dog Breed: {pet[5]}")
            elif pet[4] == 'Cat':
                print(f", Cat Color: {pet[6]}")
            else:
                print()
    except Exception as e:
        print("Error while fetching pet data:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def record_cash_donation():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        donor_name = input("Enter Donor Name: ")
        amount = float(input("Enter Donation Amount: "))
        donation_type = 'Cash'
        sql = "INSERT INTO donations (donor_name, amount, donation_date, donation_type) VALUES (%s, %s, CURDATE(), %s)"
        values = (donor_name, amount, donation_type)
        cursor.execute(sql, values)
        conn.commit()
        print("Donation recorded successfully.")
    except Exception as e:
        print("Error while recording donation:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def view_adoption_events():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT event_id, event_name, event_date, location FROM adoption_events")
        events = cursor.fetchall()
        print("\n--- Adoption Events ---")
        for event in events:
            print(f"ID: {event[0]}, Name: {event[1]}, Date: {event[2]}, Location: {event[3]}")
    except Exception as e:
        print("Error while fetching events:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def register_for_event():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        event_id = int(input("Enter Event ID to register for: "))
        participant_name = input("Enter Your Name: ")
        contact_info = input("Enter Contact Info: ")
        sql = "INSERT INTO event_registrations (event_id, participant_name, contact_info, registration_date) VALUES (%s, %s, %s, CURDATE())"
        values = (event_id, participant_name, contact_info)
        cursor.execute(sql, values)
        conn.commit()
        print("Successfully registered for the event.")
    except Exception as e:
        print("Error during event registration:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def main():
    while True:
        print("\n--- PetPals Menu ---")
        print("1. List Available Pets")
        print("2. Record Cash Donation")
        print("3. View Adoption Events")
        print("4. Register for Event")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            list_available_pets()
        elif choice == '2':
            record_cash_donation()
        elif choice == '3':
            view_adoption_events()
        elif choice == '4':
            register_for_event()
        elif choice == '5':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

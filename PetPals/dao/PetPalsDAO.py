from util.DBConnUtil import DBConnUtil


class PetPalsDAO:

    def list_available_pets(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age, breed, pet_type FROM pets")
            for row in cursor.fetchall():
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Breed: {row[3]}, Type: {row[4]}")
        except Exception as e:
            print("Error while fetching pet data:", e)

    def record_cash_donation(self, donor_name, amount, date):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO donations (donor_name, amount, donation_date) VALUES (%s, %s, %s)",
                           (donor_name, amount, date))
            conn.commit()
            print("Donation recorded successfully.")
        except Exception as e:
            print("Error while recording donation:", e)

    def list_adoption_events(self):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM adoption_events")
            for row in cursor.fetchall():
                print(f"Event ID: {row[0]}, Name: {row[1]}, Date: {row[2]}, Location: {row[3]}")
        except Exception as e:
            print("Error fetching adoption events:", e)

    def register_for_event(self, event_id, participant_name):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO participants (event_id, participant_name) VALUES (%s, %s)",
                           (event_id, participant_name))
            conn.commit()
            print("Participant registered successfully.")
        except Exception as e:
            print("Error while registering participant:", e)

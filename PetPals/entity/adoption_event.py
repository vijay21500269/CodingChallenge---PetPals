class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def register_participant(self, participant):
        self.participants.append(participant)

    def host_event(self):
        print("Adoption Event Started!")
        for p in self.participants:
            p.adopt()

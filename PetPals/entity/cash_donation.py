from entity.donation import Donation
from datetime import datetime

class CashDonation(Donation):
    def __init__(self, donor_name, amount, donation_date=None):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date or datetime.now()

    def record_donation(self):
        print(f"Recorded cash donation of ₹{self.amount} by {self.donor_name} on {self.donation_date}")

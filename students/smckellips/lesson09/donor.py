#!/usr/bin/env python

class Donor(object):
    def __init__(self, name, donation_list=None):
        self.name = lcd_name(name)
        self.printname = name
        if not donation_list:
            self.donation_list = []

    @staticmethod
    def lcd_name(name):
        '''least common denominator name'''
        return name.lower().replace(' ','_') 

    def add_donation(donation):
        '''Add donation to donor'''
        if validate_donation(donation):
            self.donation_list.append(donation)
        pass

    @staticmethod
    def validate_donation(donation):
        '''donation validation rules'''
        if donation <= 0 or
            type(donation) not in ['float','int']
            return False
        return True

    @property
    def printname():
        return self.printname

    @property
    def donations():
        return self.donation_list

    @property
    def last_donation():
        return self.donation_list[-1]
    
    @property
    def total_donations():
        return sum(self.donation_list)

    @property
    def average_donations():
        return self.total_donations / len(self.donations)


class DonorCollection(object):
    def __init__(self,donor_list=None):
        '''startup, add sample data if not provided'''
        if not donor_list:
            self.donor_db = build_sample_data()
        
    
    def get_donor(name):
        '''return matching donor object or none'''
        pass

    def add_donor(donor):
        '''Add new donor'''
        if not donor.name in self.donor_db.keys():
            self.donor_db[donor.name] = donor
            return True
        else:
            print("Donor already in DB")
            return None

    def list_donors():
        '''list all donor names'''
        pass
    
    def send_thankyou():
        ''' send single donor thank you letter'''
        pass

    def create_report():
        '''create report of all donors'''
        pass

    def build_sample_data():
        add_donor(Donor("William Gates, III", [653772.32, 12.17]))
        add_donor(Donor("Jeff Bezos",[877.33]))
        add_donor(Donor("Paul Allen", [663.23, 43.87, 1.32]))
        add_donor(Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]))

        
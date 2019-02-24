"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):

        return "Customer: {} {}".format(self.first_name,self.last_name)



def read_customer_info_from_file(filepath):
    """get info from txt file"""
    customer_dict = {}
    file = open(filepath)
    for line in file:
        first_name,last_name,email,password=line.strip().split("|")

        customer_dict[email] = Customer(first_name, last_name, email, password)
    return customer_dict

def get_by_email(email):
    """Return a Customer, given their email."""

    # This relies on access to the global dictionary `melon_types`

    return customer_dict[email]

def get_customer_dict_values():
    return list(customer_dict.values())


customer_dict = read_customer_info_from_file('customers.txt')
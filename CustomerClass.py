class Customer:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__number
    


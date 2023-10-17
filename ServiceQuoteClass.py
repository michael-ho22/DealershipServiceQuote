class ServiceQuote:
    def __init__(self, pcharges, lcharges, sales_tax):
        self.__pcharges = pcharges
        self.__lcharges = lcharges
        self.__sales_tax = sales_tax
        self.__tax_charge = 0
        self.__total_charges = 0

    def set_parts_charges(self, pcharges):
        self.__pcharges = pcharges

    def set_labor_charges(self, lcharges):
        self.__lcharges = lcharges

    def tax_charge(self):
        self.__tax_charge = (self.__pcharges + self.__lcharges) * self.__sales_tax

    def add_charges(self):
        self.__total_charges = self.__pcharges + self.__lcharges + self.__tax_charge

    def get_pcharges(self):
        return self.__pcharges
    
    def get_lcharges(self):
        return self.__lcharges

    def get_tax_charge(self):
        return self.__tax_charge

    def get_total_charges(self):
        return self.__total_charges

"""Classes for melon orders."""


# class DomesticMelonOrder():
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder():
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

       # return self.country_code

class AbstractMelonOrder():

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = ''
        self.passed_inspection = ''

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == 'Christmas':
            base_price = 7.5
        else:
            base_price = 5
        if self.qty < 10 and self.order_type == 'international':
            flat_fee = 3
        else:
            flat_fee = 0

        total = (1 + self.tax) * self.qty * base_price+flat_fee

        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    
    order_type = 'domestic'
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    order_type = 'international'
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty):
        super(). __init__(species, qty)
        self.passed_inspection = False

    tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = True
        
        return self.passed_inspection

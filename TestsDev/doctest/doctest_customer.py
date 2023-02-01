class Customer:
    """
    A sample customer class
    
    >>> customer_1 = Customer("John", "Brad", 5000)
    >>> customer_2 = Customer("Tina", "Smith", 3000)
    >>> customer_1.customer_mail
    'John.Brad@email.com'
    >>> customer_2.customer_mail
    'Tina.Smith@email.com'
    >>> customer_1.customer_fullname
    'John Brad'
    >>> customer_2.customer_fullname
    'Tina Smith'
    >>> customer_1.apply_discount
    4750
    >>> customer_2.apply_discount
    2850
    """
    
    discount = 0.95
    
    def __init__(self, first_name, last_name, purchase):
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        return f'{self.first_name}.{self.last_name}@email.com'
    
    @property
    def customer_fullname(self):
        return f'{self.first_name} {self.last_name}'
                                                            
    @property
    def apply_discount(self):
        return int(self.purchase * self.discount)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000
    def prompt(self):
        self.day = int(input('Day: '))
        invalid_month = True
        while invalid_month:
            self.month = int(input('Month: '))
            if self.month <= 12 and self.month >= 1:
                invalid_month = False            
        invalid_year = True
        while invalid_year:
            self.year = int(input('Year: '))
            if self.year >= 2000:
                invalid_year = False

    def display(self):
        print(f'{self.month:02d}/{self.day:02d}/{self.year}')

    def long_display(self):
        months = [
            'January', 
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        print(f'{months[self.month - 1]} {self.day:02d}, {self.year}')
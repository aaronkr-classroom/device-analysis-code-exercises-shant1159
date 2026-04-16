class SayDays:
    def __init__(self, year: int, month:  int, days : int):
        self.year = year
        self.month = month
        self.day = days 
    def is_leep(self):
        y = self.year
        return (
            (y % 4 == 0 and y %100 != 0) or
            (y%400 == 0)
            )
    def get_day_of_year(self) -> int: 
        days_in_month = [
            31,29 if self.is_leep() else 28,31,30,
            31,30,31,31,
            30,31,30,31
            ]
        total =0
        m = 0
        while m<self.month - 1:
            total +=days_in_month[m]
            m +=1

        total += self.day
        return total


    def days_left(self):
        total_days = 366 if self.is_leep() else 365
        return total_days - self.get_day_of_year() 
    def weekday(self):
        y = self.year
        m = self.month
        d = self.day

        if m <3:
            m += 12
            y -= 1
        k = y%100
        j = y// 100
        h = (d + (13 *(m +1)) //
             5 + k + k //4 +j //4 +5*j)%7
        return h

    def weekdays_name(self) -> str:
        name = [
            "Saturday", 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
            ]
        return name[self.weekday()]

# Run
while True:
    year = int(input("What year is it? : "))
    month = int(input("what month is it : "))
    day = int(input("What is days? : " ))

    date = SayDays(year, month,day)
    print("Days after Jan 1 : ", date.get_day_of_year()) 
    print("Days until Dec 31 : ", date.days_left())
    print("Numeric days of week  : ", date.weekday())
    print("English day of the week : ", date.weekdays_name())
    
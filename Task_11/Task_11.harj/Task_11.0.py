class Worker:
    worker_count = 0

    def __init__(self, forename, surname):
        Worker.worker_count += 1
        self.worker_number = Worker.worker_count
        self.forename = forename
        self.surname = surname

    def print_info(self):
        print(f"{self.worker_number}: {self.forename} {self.surname}")


class Hourly(Worker):

    def __init__(self, forename, surname, hour_wage):
        self.hour_wage = hour_wage
        super().__init__(forename, surname)

    def print_info(self):
        super().print_info()
        print(f"Tuntipalkka: {self.hour_wage}")

class Monthly(Worker):

    def __init__(self, forename, surname, month_wage):
        self.month_wage = month_wage
        super().__init__(forename, surname)

    def print_info(self):
        super().print_info()
        print(f"Kuukausipalkka: {self.month_wage}")


if __name__ == '__main__':
    workers = []
    workers.append(Hourly("Kim", "Löfgren,", 28.50))
    workers.append(Monthly("Sonja", "Löfgren", 6950))
    workers.append(Worker("Pekka", "Puro"))
    workers.append(Hourly("Kippari", "kalle", 18.9))


    for hour in workers:
        hour.print_info()

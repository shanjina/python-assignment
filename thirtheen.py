class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
            print("Car brand:",self.brand)
            print("Car model",self.model)
            print("year",self.year)
c1=Car("Aston Martin","Corolla","2002")
c1.display_info()

class BeautySalon(object):
    def __init__(self, name, service, no_of_services, bill):
        self.__name = name
        self.__service = service
        self.__no_of_services = no_of_services
        self.__bill = bill

    def calculate_Total_Bill(self,bill):

        if self.__bill!=0:
            __status = "Service availed"
            print(__status)

        else:
            print("Waiting for the service")

    def __str__(self):
        return f'Beauty Salon, Customer Name: {self.__name}, Service Name: {self.__service},Payment: {self.__bill},No of services:{self.__no_of_services} '

print('***************************************************************************')
print('Welcome to Beauty Salon')
print('***************************************************************************')
print('Four services available: \n 1. Body Spa(Rs. 500) \n 2. Pedicure (Rs. 150) \n 3. Manicure (Rs. 150) \n 4. Hair Services (Rs. 750)')

salon1 = BeautySalon("Manpreet Kaur","Pedicure, Manicure",2,300)
print(salon1)
salon1.calculate_Total_Bill(300)

salon2 = BeautySalon("Navdeep Kaur","Manicure, Hair Services",1,900)
print(salon2)
salon2.calculate_Total_Bill(900)

salon3 = BeautySalon("Sarbjit Kaur","Hair Services",2,750)
print(salon3)
salon3.calculate_Total_Bill(750)

salon4 = BeautySalon("Navneet Kaur","Body Spa",1,0)
print(salon4)
salon4.calculate_Total_Bill(0)











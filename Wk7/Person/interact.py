from employee import Employee
from customer import Customer


staff1 = Employee("Sally", "female", 24, "cleaner", "nights")
print(staff1)
staff1.introduce()
staff1.length_of_service()
staff1.tasks()
age = staff1.age
staff1.nick_name = "Sal"
print(staff1)



print("******************************************")

staff2 = Employee("Fred", "male", 19, "checkout worker", "days")
print(staff2)
staff2.length_of_service()
staff2.tasks()
staff2.state_gender()
staff2.on_duty()
print("******************************************")

staff3 = Employee("Andy", "male", 56, "customer service assistant", "evenings")
print(staff3)
staff3.length_of_service()
staff3.tasks()
staff3.breathe()
staff3.hours()
staff3.on_duty()
print("******************************************")

cust1 = Customer("George", "male", 21, "buy", "socks")
print(cust1)
cust1.introduce()
cust1.breathe()
cust1.state_age()
cust1.state_gender()
cust1.ask_for_help()
print("******************************************")

cust2 = Customer("Claire", "female", 21, "sell", "panthers")
print(cust2)
cust2.introduce()
cust2.ask_for_help()
print("******************************************")

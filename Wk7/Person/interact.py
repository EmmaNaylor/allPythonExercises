from employee import Employee
from customer import Customer


staff1 = Employee("Sally", "female", 34, "cleaner", "nights")
print(staff1)
staff1.introduce()
staff1.length_of_service()
staff1.tasks()
staff1.nick_name = "Sal"
print(staff1)
staff1.on_duty()
staff1.state_age()
print("******************************************")

staff2 = Employee("Fred", "male", "fruit", "checkout worker", "days")
print(staff2)
staff2.length_of_service()
staff2.tasks()
staff2.state_gender()
staff2.on_duty()
print("******************************************")

staff3 = Employee("Andy", "male", 56, "customer service assistant", "evenings")
print(staff3)
age = staff3.age
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
cust1.length_of_wait()
cust1.ask_for_help()
print("******************************************")

cust2 = Customer("Claire", "female", 21, "sell", "panthers")
print(cust2)
cust2.introduce()
cust2.ask_for_help()
cust2.length_of_wait()
cust2.nick_name = "Panther Lady"
cust2.browse()
print(cust2)
print("******************************************")

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


    #use interheirtance when you need a specific case under the class 


class AdminUser(User):
    def active_users(self):
        return '500'


Brodie = AdminUser('brodie@devcamp.com', 'Brodie', 'Turner')

Christine = User('christine@devcamp.com', 'Christine', 'Turner')


print(Brodie.active_users()) #500

#print(Christine.active_users()) #error


print(Brodie.greeting()) #Hi Brodie Turner
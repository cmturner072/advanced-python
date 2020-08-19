#Class Instance 

class Website:
    def __init__(self, title):
        self.title = title
 
 
 
ws = Website('My Website Title')
print(ws.title) #My Website Title
 
print(ws.__dict__) #{'title': 'My Website Title'}
 
 
ws_two = Website('Second Title')
print(ws_two.__dict__) #{'title': 'Second Title'}




#Class Attributes
class DifferentWebsite:
    title = 'My Class Title'

dw = DifferentWebsite()

print(dw.title) #My Class Title



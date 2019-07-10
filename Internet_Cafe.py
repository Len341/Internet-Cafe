class Internet_cafe():  
    
    items_in_cafe = ['coffee','burger','pizza']
    staff_cust_amount_pcs = [3,6] 
    #here to address the amount of available computers in the cafe 
    #we can use staff_cust_amount_pcs[0] , or [1] to change this amount.
    cust_list = []
    used_tables = {}               
    

    def __init__(self,Name,Id,Tel):
        self.name = Name
        Self.id = Id
        self.tel = Tel

    class Customer():
        total_bill = 0
        def __init__(self,name,tel,age,id):
            self.name = name
            self.tel = tel
            self.age = age
            self.id = id

        def bill(amount,status,item):
            Customer.total_bill+=amount
            items = '##List of Items##'
            items+= '-'+item+'\n'
            if status == 'done' or status =='Done':
                return total_bill
            
        def get_order_price(price_of_item, amount):
            return price_of_item*amount

    

    print('Welcome to your number one internet cafe\nHere you can also order a variety of delicious snacks and beverages')
    staff_or_cust = input('Are you a staff member or customer? (Staff/Cust) ')
    while staff_or_cust != 'Staff' and staff_or_cust!= 'staff' and staff_or_cust!= 'Cust' and staff_or_cust!= 'cust':
          staff_or_cust = input('Please enter the correct option: (Staff/Cust) ')

    if staff_or_cust =='cust' or staff_or_cust =='Cust':
         name = input('Very Welcome, please enter your Name: ')
         age = input('Next is your age: ')
         id = input('Please enter your ID number: ')
         tel = input('Lastly, please enter your telephone number: ')
         customer = Customer(name,tel,age,id)
         #Creating a customer object
         cust_list.append(['Customer Name: '+customer.name, 'Telephone: '+customer.tel, 'Age: '+customer.age, 'ID: '+customer.id])
         print(cust_list)

         pc_book = input('Would you like to book a computer/internet session? ')
         if pc_book == 'yes' or pc_book =='y' or pc_book =='Y' or pc_book =='YES' or pc_book =='Yes':
              print('****TIMES****\n*1) 0 - 1 Hour*\n*2) 1- 2 Hours*\n*3) 2-3 Hours*')
              print('\nThe rate is R20 per hour of use\nand R10 per extra half an hour')
              time = input('For how long will you stay [please select an option from the times table]' )
              while time != '1' and time != '2' and time != '3':
                  time = input('Please enter a valid option')
              cust_bill = Customer.bill(time*20,'used','Internet access')
              for i in ['a','b','c','d','e','f']:
                  if i not in used_tables:
                      used_tables[customer.name] = i
   
              print('Thanks, your table number is '+used_table[customer.name])


              
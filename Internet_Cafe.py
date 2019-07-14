class Internet_cafe():  
    
    staff_id = {'232524':'Sue','95363':'Ann','29499':'Steve'}
    staff_tel = {'232524':'0829374823','95363':'123463489','29499':'0937432863'}
    items_in_cafe = {'coffee':20, 'toast':25, 'Full-dish':100, 'cocktail':40}
    cust_bills = [[],[],[],[],[],[],]
    bills_amnt = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
    cust_list = []
    used_tables = {}               
    

    def __init__(self,Name,Id,Tel,items):
        self.name = Name
        self.id = Id
        self.tel = Tel
        self.items = items

    class Customer():
        total_bill = 0
        def __init__(self,name,tel,age,id):
            self.name = name
            self.tel = tel
            self.age = age
            self.id = id

        def bill(amount,status,item,tot_prod,table):
            num = Internet_cafe.Customer.get_table(table)
            if Internet_cafe.cust_bills[num] == []:
                Internet_cafe.Customer.bill_items = '### List of Items ###\n'
            else:
                Internet_cafe.Customer.bill_items = ''
            amount = int(amount)
            Internet_cafe.bills_amnt[table]+=amount
            if item != '':
                    Internet_cafe.Customer.bill_items+=str('-'+item+' x'+str(tot_prod)+'\n')
                    Internet_cafe.cust_bills[num].append(Internet_cafe.Customer.bill_items)
                    return Internet_cafe.cust_bills[num]
            
            if status == 'done' or status =='Done':
                bill=''
                for i in Internet_cafe.cust_bills[num]:
                    bill+=i
                return bill+'\nYour total bill is R'+str(Internet_cafe.bills_amnt[table])

        def   get_table(table):
            if table == 'a':
                num = 0
            elif table == 'b':
                num = 1
            elif table == 'c':
                num = 2
            elif table == 'd':
                num = 3
            elif table == 'e':
                num = 4
            else:
                num = 5
            return num


    class staff():
        def __init__(self, name, id, tel):
            self.name = name
            self.id = id
            self.tel = tel
    
Lens_cafe = Internet_cafe('Len\'s Internet Cafe','hwR373SD239',+2728371438,Internet_cafe.items_in_cafe)
print('Welcome to your number one internet cafe\nHere you can also order a variety of delicious snacks and beverages')
staff_or_cust = input('Are you a staff member or customer? (Staff/Cust) ')
while staff_or_cust == 'staff' or staff_or_cust == 'Staff' and Lens_cafe.cust_list == []:
    staff_or_cust = input('Error, there\'s no customers, get customers to log orders\n Staff or Cust? ')
while staff_or_cust != 'Staff' and staff_or_cust!= 'staff' and staff_or_cust!= 'Cust' and staff_or_cust!= 'cust':
        staff_or_cust = input('Please enter the correct option: (Staff/Cust) ')

while staff_or_cust == 'cust' or staff_or_cust == 'Cust' or staff_or_cust == 'Staff' or staff_or_cust == 'staff':

    while staff_or_cust =='cust' or staff_or_cust =='Cust':
            name = input('Very Welcome, please enter your Name: ')
            age = input('Next is your age: ')
            id = input('Please enter your ID number: ')
            tel = input('Lastly, please enter your telephone number: ')

            customer = Lens_cafe.Customer(name,tel,age,id)
            #Creating a customer object

            Lens_cafe.cust_list.append(['Customer Name: '+customer.name, 'Telephone: '+customer.tel, 'Age: '+customer.age, 'ID: '+customer.id])
            print(Lens_cafe.cust_list)

            pc_book = input('Would you like to book a computer/internet session? ')
            if pc_book == 'yes' or pc_book =='y' or pc_book =='Y' or pc_book =='YES' or pc_book =='Yes':
                print('****TIMES****\n*1) 0 - 1 Hour*\n*2) 1- 2 Hours*\n*3) 2-3 Hours*')
                print('\nThe rate is R20 per hour of use\nand R10 per extra half an hour')
                time = input('For how long will you stay [please select an option from the times table]: ' )
                while time != '1' and time != '2' and time != '3':
                    time = input('Please enter a valid option')
                
                count = 0
                for i in ['a','b','c','d','e','f']:
                    #tables in cafe
                    if i not in Lens_cafe.used_tables:
                        #available tables in cafe
                        Lens_cafe.used_tables[i] = customer.name
                        customer.bill = ''
                        customer.bill = Lens_cafe.Customer.bill(int(time)*20,'used','Internet access',time+' hours',i)
                        Lens_cafe.cust_bills[count] = customer.bill
                        print(Lens_cafe.used_tables, Lens_cafe.cust_bills)
                        print('Thanks, your table number is '+i)
                        break
                    count+=1
                
    #ended cust 'if' statement:
                staff_or_cust = input('Are you a staff member or customer? (Staff/Cust) ')

    else:
        staff_member_login = input('Welcome, please enter your staff ID: ')
        if staff_member_login in Lens_cafe.staff_id:
            staff_member = Lens_cafe.staff(Lens_cafe.staff_id[staff_member_login],staff_member_login,Lens_cafe.staff_tel[staff_member_login])
            staff = True
            while staff:
                print('Here you can add items or orders to a specific tables bill')
                table_val = input('For which table are you making an order? ')
                while table_val not in Lens_cafe.used_tables:
                    table_val = input('That\'s an incorrect table!\nEnter correct table number: ')
                #valid tables in Lens_cafe is a,b,c,d,e,f.

                count=0
                add_more = True

                for i in Lens_cafe.items:
                    count+=1
                    print(str(count)+') '+i)

                
                while add_more:
                    order = input('Please enter a product to order: ')
                    amount_prod = int(input('Enter the amount of this item: '))
                    cost = amount_prod*Internet_cafe.items_in_cafe[order]
                    customer.bill = Lens_cafe.Customer.bill(cost,'',order,amount_prod,table_val)
                    num = Internet_cafe.Customer.get_table(table_val)
                    Lens_cafe.cust_bills[num] = customer.bill
                    #this above line allows me to track which bill fits with 
                    #which table number
                    add_more = input('Do you want to add more items now? ')

                    if add_more == 'y' or add_more == 'Yes' or add_more == 'Y' or add_more == 'yes':
                        #Here the staff member will have 
                        #oppurtunity to add more items to the bill
                        continue

                    done = input('Are you done with the customers bill? ')
                    if done == 'y' or done == 'Yes' or done == 'Y' or done == 'yes':
                        #staff member is now done with the bill and it 
                        #is ready to be processed for customer
                        customer.bill = Lens_cafe.Customer.bill(0,'done','','',table_val)
                        Lens_cafe.cust_bills[num] = customer.bill
                        print(customer.bill+'\n\nReturn bill to table '+table_val)
                        break

                    else:#when staff member is not yet done with bill but does not want 
                         #to do more orders right now
                        add_more = False
                        staff = False

                staff_or_cust = input('Are you a staff member or customer? (Staff/Cust) ')
                
        

              
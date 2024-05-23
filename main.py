import json
from datetime import datetime
import matplotlib.pyplot as plt

#Modern Personal Finance Tracker Project
print("Personal Finance Tracker")

income = []
expenses = []
savings = []


# Function to load initial data from JSON file
def load_initial_data():
  with open('data.json', 'r') as data_file:
    return json.load(data_file)


data = load_initial_data()


# Function to save data to JSON file
def save_data(data):
  with open('data.json', 'w') as data_file:
    json.dump(data, data_file, indent=4)


#The data dictionary will store the income, expenses, and savings data for each month.
#The dictionary will be updated with the new income data and expenses daily, weekly, or monthly. However a date will be be stored to track when a new income or expenses was added.
#The new income added will be added to a list and the new expenses added to a list and stored withs current date to easily track when the income and expenses was added.
#the savings data will be calculated and updated based on the new income and expenses data.
#The data dictionary will be saved in JSON file.

#HandleLoginsandRegistrationsInput() function will handle the users input and carryout the appropriate operation. Firstly a user will be asked to select an option from the menu such as 1 and 2. 1 is to register as a new user while 2 is to login.
#login information need to be entered to access your own personal tracker. However if the user is not a registered user your own new personal tracker will be created.

#A condition statement will be used to check if the user is a registered user or not. If the condition pass and the user login successfully the program will proceed to the next step where all the user data will be displayed by calling the class User_interface.

#if the user select 2 to register a new user registration having a name input and password input prompt will appear. However, the new user will be added to the data dictionary and contain all the user information such as password, name,income, expenses, savings, and date. the income, expenses, and savings will be 0 for the new user until they update them.
#The login system will


def HandleLoginsandRegistrationsInput():
  #get the user input to login or register
  print("Enter 1: To Login\nEnter 2: To Register")
  while True:
    try:
      userInput = int(input("Enter your Choice: "))
      if userInput != 1 and userInput != 2:
        raise ValueError("Invalid choice Selected. Please select 1 or 2")
      if userInput == 1:
        login()
        break
      elif userInput == 2:
        register()
        break
    except ValueError as e:
      print('Invalid input', e)


def login():
  print("Welcome to the Login system")
  while True:
    try:
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      #check if username is in the data dictionary
      if username not in data:
        #if username not found raise value error
        raise ValueError("Incorrect username or password")
        #check if password is correct
      if password != data[username]['password']:
        #raise error if password is not correct
        raise ValueError("Incorrect username or password")
      print("Login Successfully")
      #create a new instance of the user interface class
      user_interface = User_Interface(username)
      user_interface.call_user_interface()
      break
    except ValueError as e:
      print(e)


def register():
  print("Welcome to the Registration system")
  print("Fill the registration form")

  while True:
    try:
      username = input("Enter username: ")
      # Check if the username already exists in the data dictionary
      if username in data:
        raise ValueError("Username already exists. Please select another one.")
      #get user input for password
      password = input("Enter password: ")
      #get user input to confirm password
      confirmPassword = input("Confirm password: ")
      #check password is the same as confirm password
      if password != confirmPassword:
        #raise value error if password is not in dictionary
        raise ValueError("Passwords do not match. Please try again.")
      # If everything is fine, add the new user to the data dictionary
      data[username] = {
          'password': password,
          'Allincomes': {},
          'Allexpenses': {},
          'Allsavings': {}
      }
      save_data(data)
      print("Registration successful.")
      #create a new instance of the user interface class
      user_interface = User_Interface(username)
      user_interface.call_user_interface()
      break  # Break out of the loop after successful

    except ValueError as e:
      print(e)


class User_Interface:

  def __init__(self, username):
    self.username = username

  def call_user_interface(self):
    print(
        f'Welcome {self.username} to your Personal Finance Tracker Dashboard')
    #print the choices for users to choose from between 1 and 6. 1 is to add income, 2 is to add expenses, 3 is to view income, 4 is to view expenses, 5 is to view savings, and 6 is to logout
    print(
        'choose option\n1: Add Income\n2: Add Expenses\n3: Generate Report\n4: Logout'
    )
    #loop until choices entered by the user meet the condition
    while True:
      try:
        #get the user input for the choices
        option = input("Enter your choice: ")
        #check if the user input is numeric and not alphabets
        if not option.isnumeric():
          #if user input is not numeric raise a value error
          raise ValueError(
              "Invalid choice. please enter a choice between 1 and 6")
          #if user input is not between 1 and 6 raise a value error
        if int(option) < 1 or int(option) > 6:
          raise ValueError(
              "Invalid choice. please enter a number between 1 and 6")
        if option == '1':
          addIncome(self.username)
        elif option == '2':
          addExpenses(self.username)
        elif option == '3':
          generateReport(self.username)
        elif option == '4':
          logout()
      except ValueError as e:
        print(e)


#Function to add income
def addIncome(username):
  # Get the income amount from the user
  incomeAmount = input("Enter income amount: ")
  incomeAmount = int(incomeAmount)
  # Get the income date automatically from the system
  incomeDate = datetime.now().strftime('%Y-%m-%d')
  #store the income added to the array
  #check if the AllIncome is not empty
  if len(data[username]['Allincomes']) == 0:
    incomeID = len(data[username]['Allincomes']) + 1
    incomeID = str(incomeID)
    #add the new income to the dictionary and store the             incomeID incomeDate, and incomeAmount
    data[username]['Allincomes'][incomeID] = {
        'date': incomeDate,
        'income': incomeAmount
    }
    # Save to data.json file
    save_data(data)
    print("Income added successfully")
  #if the Allincomes is not empty
  elif len(data[username]['Allincomes']) > 0:

    #if the Allincome is not empty and has a key and value loop through the items in the Allincome

    for incomeKey, incomeValue in list(data[username]['Allincomes'].items()):
      #check if the income date is already added to the Allincome and date generated is the same, which means the user has already added an income for the same date
      if incomeValue['date'] == incomeDate:
         
        print("Income already added for today")
        print("Do you want to add to the income\n Enter option y or n")
        #if the income date is already added to the Allincome ask the user if they want to add to the income
        confirm = input("Enter y or n: ")
        #if the user input is y add the income to the all income
        if confirm == 'y':
          #use the income key to get the particular one with same date and get the income value
          income = data[username]['Allincomes'][incomeKey]['income']
          #convert the income value to integer to be able to add
          income = int(income)
          #add the income amount to the income value
          income += int(incomeAmount)

          data[username]['Allincomes'][incomeKey] = {
              'date': incomeDate,
              'income': income
          }
          
          save_data(data)
          print("Income updated successfully")
          break
        elif confirm == 'n':
          break

      elif incomeDate != data[username]['Allincomes'][str(len(data[username]['Allincomes']))]['date']:
       
        #get the length of the income added and add 1 to get the next id    
        incomeID = len(data[username]['Allincomes']) + 1
        #convert the incomeID to a string
        incomeID = str(incomeID)
        #add the new income to the dictionary and store the             incomeID incomeDate, and incomeAmount
        data[username]['Allincomes'][incomeID] = {
            'date': incomeDate,
             'income': incomeAmount
        }
        
        # Save to data.json file
        save_data(data)
        print("Income added successfully")
        

#function to add expenses
def addExpenses(username):
  if len(data[username]['Allincomes']) == 0:
    print("No Income added yet. Please add income first")

  else:
    # Get the expense amount from the user
    expensesAmount = input("Enter Expenses amount: ")

    # Get the expenses date automatically from the system
    expensesDate = datetime.now().strftime('%Y-%m-%d')
    #store the expenses added to the array
    #check if the Allexpenses is not empty
    if len(data[username]['Allexpenses']) == 0:
      expensesID = len(data[username]['Allexpenses']) + 1
      #add the new expenses to the dictionary and store the             expensesID expensesDate, and expensesAmount
      data[username]['Allexpenses'][expensesID] = {
          'date': expensesDate,
          'expenses': expensesAmount
      }
      # Save to data.json file
      save_data(data)
      print("Expenses added successfully")
      CalculateSavings(username, expensesDate, expensesID)
      

    elif len(data[username]['Allexpenses']) > 0:

      #if the Allexpenses is not empty and has a key and value in loop through the items in the Allexpenses
      for expensesKey, expensesValue in list(data[username]['Allexpenses'].items()):
        #check if the expenses date is already added to the Allexpenses
        if expensesValue['date'] == expensesDate:

          print("Expenses already added for today")
          print("Do you want to add to the expenses\n Enter option y or n")
          #if the expenses date is already added to the Allexpenses ask the user if they want to add to the expenses
          confirm = input("Enter y or n: ")
          #if the user input is y add the expenses to the all expenses
          if confirm == 'y':
            #use the expenses key to get the particular one with same date and get the expenses value
            expenses = data[username]['Allexpenses'][expensesKey]['expenses']
            #convert the expense value to integer to be able to add
            expenses = int(expenses)
            #add the expenses amount to the expenses value
            expenses += int(expensesAmount)
            #update the expenses value in the dictionary
            data[username]['Allexpenses'][expensesKey] = {
                'date': expensesDate,
                'expenses': int(expenses)
            }
            save_data(data)
            print("Expenses updated successfully")
            
            #call the Calculatesavings function and pass the username, expenses, expensesDate, and expensesKey as parameter
            #this function is called here to update the savings if the expenses is updated
            CalculateSavings(username, expensesDate, expensesKey)
            break
          elif confirm == 'n':
            break

        elif expensesDate != data[username]['Allexpenses'][str(len(data[username]['Allexpenses']))]['date']:
          #get the length of the expenses added and add 1 to get the next id
          expensesID = len(data[username]['Allexpenses']) + 1
          #convert the expensesID to a string
          expensesID = str(expensesID)
          #add the new expenses to the dictionary and store the             expensesID expensesDate, and expensesAmount
          data[username]['Allexpenses'][expensesID] = {
              'date': expensesDate,
              'expenses': int(expensesAmount)
          }
          # Save to data.json file
          save_data(data)
          print("check3")
          print("Expenses added successfully")
          #cal the function Calculatesavings function and pass the username, expenses, expensesDate, expensesKey as parameter
          CalculateSavings(username, expensesDate, expensesID)

          #call Calculatesavings function to to calculate the savings


def CalculateSavings(username, expensesDate, expensesID):
  #assign incomeTotal as 0
  incomeTotal = 0
  expensesTotal =0 
  #loop therough all income to get the income values
  for incomeKey, incomeValue in data[username]['Allincomes'].items():
    #get the income value
    income = incomeValue['income']
    #convert income value to integer
    income = int(income)
    #add the income value to the incomeTotal
    incomeTotal += income
    #caculate to the income and expenses to get the savings
  #loop therough all expense to get the expenses values
  for expensesKey, expensesValue in data[username]['Allexpenses'].items():
    #get the expenses value
    expenses = expensesValue['expenses']
    #convert expenses value to integer
    expenses = int(expenses)
    #add the expenses value to the incomeTotal
    expensesTotal += expenses
    #caculate to the income and expenses to get the savings
  savings = incomeTotal - expensesTotal
  #add the savings to the dictionary and store based on the expensesID
  data[username]['Allsavings'][expensesID] = {
      'date': expensesDate,
      'savings': savings
  }
  #save data to data.json file
  save_data(data)


def generateReport(username):
  income_dates = []
  incomes = []
  expenses_dates = []
  expenses = []
  saving_dates = []
  savings = []

  total_income = 0
  total_expenses = 0
  total_savings = 0

  # Extract the dates, incomes, expenses, and savings from the dictionary to visualize the data
  # Extract the incomes and their dates from the dictionary
  for key, value in data[username]['Allincomes'].items():
    income_dates.append(value['date'])
    incomes.append(value['income'])
    total_income += value['income']

  # Extract the expenses and their dates from the dictionary
  for key, value in data[username]['Allexpenses'].items():
    expenses_dates.append(value['date'])
    expenses.append(value['expenses'])
    total_expenses += value['expenses']

  # Extract the savings and their dates from the dictionary
  for key, value in data[username]['Allsavings'].items():
    saving_dates.append(value['date'])
    savings.append(value['savings'])
    total_savings += value['savings']

  # Plotting the data
  plt.figure(figsize=(10, 6))
  plt.plot(income_dates, incomes, label='Income', marker='o')
  plt.plot(expenses_dates, expenses, label='Expenses', marker='o')
  plt.plot(saving_dates, savings, label='Savings', marker='o')

  plt.title('Personal Finance Report')
  plt.xlabel('Date')
  plt.ylabel('Amount')
  plt.legend()
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.tight_layout()

  # Display total income, total expenses, and total savings
  plt.text(
      0.5,
      0.5,
      f'Total Income: ${total_income}\nTotal Expenses: ${total_expenses}\nTotal Savings: ${total_savings}',
      horizontalalignment='center',
      verticalalignment='center',
      transform=plt.gca().transAxes)

  plt.show()


def logout():
  print("Log out successfully")
  login()


HandleLoginsandRegistrationsInput()

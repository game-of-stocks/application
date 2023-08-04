#packages needed to create form for user input 
import ipywidgets as widgets
from IPython.display import display
from duplicate_helper import duplicate_counter
from dropdown_values import dropdown_options_array

#package needed for regx purposes
import re


name = ""
num_of_stocks_choosen = 1

def inital_user_intake():
    #declare and make it a global variable so it can be use in other places
    global name, num_of_stocks_choosen

    #input box for name
    input_name = widgets.Textarea(
        value='Input your name',
        placeholder='Type something',
        description='First Name:',
        disabled=False
    )

    #Ask user how many stocks they would like in portfolio 

    dropdown_widget_num_of_stocks = widgets.Dropdown(
        options=[1,2,3,4,5,6,7,8,9,10,"Choose Stock Amount:"],
        description="Amount", 
        value="Choose Stock Amount:")

    #display input name, dropdown and instructions
    print("""Welcome to the Game of Stocks! You will be asked a series of questions to get started. 
    You can choose up to 10 stickes to create portfolio. Remember to diversify your portfolio.   """)

    display(input_name)
    # print(f"Choose number of stocks for your portfolio")
    display(dropdown_widget_num_of_stocks)

    # Create a button to trigger an action
    button_stock_amount = widgets.Button(description="Submit")

    # Define a function to be called on button click
    def on_button_click_stock_amount(b):
        #declare and make it a global variable so it can be use in other places
        global name, num_of_stocks_choosen

        name = input_name.value
        num_of_stocks_choosen = dropdown_widget_num_of_stocks.value
        print(f"{name}, you have choosen stock amount: {num_of_stocks_choosen}")
    


    # Attach the function to the button's click event
    button_stock_amount.on_click(on_button_click_stock_amount)

#   Display the button
    display(button_stock_amount)

# getting inital user intake values 
def get_user_inital_input():
    return name, num_of_stocks_choosen

def portfolio_user_intake(stock_amount):
    # Step 1: Create options for dropdown values which was done above

    # Step 2: Create a for loop to generate the ipywidgets.Dropdown widgets and append them to the dropdown_widgets array
    dropdown_widgets = []
    for index in range(stock_amount):  # Passing user choosen number of stocks
        dropdown_widget = widgets.Dropdown(options=dropdown_options_array, description=f'Stock {index + 1}:')
        dropdown_widgets.append(dropdown_widget)
        
    # Step 3: Create corresponding variables to store the selected values (same as before) for all choices including duplicates
    user_portfolio_array = [None] * len(dropdown_widgets)



    # Step 4: Define the function for the submit button's on_click event (same as before)
    def on_submit_button_click(b):
        for i, dropdown in enumerate(dropdown_widgets):
            # Use regular expression to find characters between parentheses
            pattern = r'\((.*?)\)'
            ticker_match = re.findall(pattern, dropdown.value) 
            user_portfolio_array[i]  = ''.join(ticker_match)
            
        # Telling users they choose these duplcate stocks 
        duplicate_counter(user_portfolio_array)
        
        # declaring a global variable so it can be access for all unique stock choosen only
        global unique_user_portfolio_array
        
        # dropping duplicates if user choose the same stock more then once a
        unique_user_portfolio_array = list(set(user_portfolio_array))
        
        print("Selected stocks:", unique_user_portfolio_array)
        
        
    # Create the Submit button (same as before)
    submit_button = widgets.Button(description="Submit")
    submit_button.on_click(on_submit_button_click)

    # Display the dropdown widgets and the Submit button (same as before)
    display(*dropdown_widgets, submit_button)

# getting inital user intake values 
def get_user_portfolio_input():
    return unique_user_portfolio_array

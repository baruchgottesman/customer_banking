"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
# I'm going to import into this main script a module that's already been provided
# by using "from" - (in the pandas we learned how to "go up" a level) and then we're going to import
# the information called "Account" within the Account.py file.  

from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # creating a new entry based on the Account.py file with the opening balance and a blank space for interest

    savings_account = Account(balance, 0)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    #  pretty straight forward, fineds the interest actually earned by calculating the interest rate,
    # converting it to actual interest rate (i.e. 10% is .1, accomplished by dividing by 100) and then 
    # calculating the per month rate by dividing the actual months by 12. 

    interest_earned = balance * (interest_rate / 100 * months / 12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    # now we're creating a third new Item - we have the new savings account, the interest earned and now
    # an "updated balance"
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    # this is the heart of the issue - "set balance" set the value of the account in the account.py
    # file.  This updates the balance in "Savings Account" based on the updated balance, and uses the
    # "set balance" item from Account.py
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    # same deal as set balance, but this time borrowing 14-17 of the Account.py line
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return savings_account.get_balance(), interest_earned


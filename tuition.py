# Name: Caleb Kimble, Tre Williams
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
# Price for in state tuiiton: 156.61
# Price of out of state tuition: 336.21
# Price of capital fee: 23.50
# Price of institutional fee: 1.75
# Price of activity fee: 2.90

import datetime

# define goal variables #
# define tax rate, service fee, and prices
RATE_TUITION_IN = 156.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in state, 2 means out-of state
num_credits = 0
scholarship = 0

tuition_amt = 0
inst_fee = 0
act_fee = 0
cap_fee = 0
total = 0
balance = 0

# define program funcitons
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? : (Y or N)")
        if yesno == "N" or yesno =="n":
            another_student = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
    global inout,num_credits,scholarship
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter 2 for OUT-OF-STATE: "))
    num_credits = int(input("Number of credits registered for: "))
    scholarship = int(input("Scholarship amount recieved: "))

def perform_calculations():
    global tuition_amt,inst_fee,act_fee,cap_fee,total,balance,scholarship

    if inout == 1:
        tuition_amt = RATE_TUITION_IN*num_credits
        cap_fee = 0
    else:
        tuition_amt = num_credits * RATE_TUITION_OUT
        cap_fee = num_credits * RATE_CAPITAL_FEE

    inst_fee = RATE_INSTITUTION_FEE*num_credits
    act_fee = RATE_ACTIVITY_FEE*num_credits
    total = tuition_amt + inst_fee + act_fee + cap_fee
    balance = total - scholarship


def display_results():
    global tuition_amt,inst_fee,act_fee,cap_fee,total,balance,scholarship
    currency = '8,.2f'
    line = '-------------------------------'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]
    print(line)
    print('**** PIEDMONT VIRGINIA COMM COLLEGE ****')
    print('    Tuition and Fees Report')
    print('     date/time', dt_short)
    print(line)
    print('Tuition            $ ' + format(tuition_amt,currency))
    print('Institutional fee  $ ' + format(inst_fee,currency))
    print('Activity fee       $ ' + format(act_fee,currency))
    print('Capital fee        $ ' + format(cap_fee,currency))
    print('Scholarship        $ ' + format(scholarship,currency))
    print('Total              $ ' + format(total,currency))
    print(line)
    print('Balance            $ ' + format(balance,currency))
    print(line)


#### Call on main program to execute
main()

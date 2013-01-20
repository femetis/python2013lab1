# functions
# Get number from users
def get_number():
    num = input('Key in your serial number:')
    return num

# Check Valid Input (All Numbers)
def check_valid_num(ainput):
    try:
        aoutput = int(ainput)
        return True
    except ValueError:
        return False

# Check length
def check_length(anum):
    return len(anum) == 16

# Check whether MasterCard or VISA
def decide_which_card(serial_number):
    if serial_number[0] == '5':
        return 1
    elif serial_number[0] == '4':
        return 2
    else:
        return False

#---------------------------------------
# main
i = False
while not i:
    input_number = get_number()
    if not check_valid_num(input_number):
        print('Invalid!Only numbers are allowed!')
    else:
        if not check_length(input_number):
            print('Invalid length!')
            continue
        else:
            i = True

if decide_which_card(input_number) == 1:
    print('It is a MasterCard!')
elif decide_which_card(input_number) == 2:
    print('It is a VISA card!')
else:
    print('Neither')

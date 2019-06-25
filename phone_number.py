# Define a function to determine a phone number
# Pattern 405-654-98765
def isPhoneNumber(phoneValue=""):

    if len(phoneValue) != 12:
        return False
    for x in range(0, 3):
        if not phoneValue[x].isdecimal():
            return False
    if phoneValue[3] != '-':
        return False
    for x in range(4, 7):
        if not phoneValue[x].isdecimal():
            return False
    if phoneValue[7] != '-':
        return False
    for x in range(8, 12):
        if not phoneValue[x].isdecimal():
            return False

    return True


# Display phone number and determine eligibility
x = '405-645-7654'
print('{0:15} is a phone number -> {1} '.format(x, isPhoneNumber(x)))
x = '405-645-ww45'
print('{0:15} is a phone number -> {1} '.format(x, isPhoneNumber(x)))
x = '405-6457654'
print('{0:15} is a phone number -> {1} '.format(x, isPhoneNumber(x)))
x = '405-645-7654'
print('{0:15} is a phone number -> {1} '.format(x, isPhoneNumber(x)))

# Test phone number validity
print(".......")
print()
message = 'Call me at 405-546-6765 tomorrow. 405-546-6995 is my office'  # Message

for x in range(0, len(message)):
    chunk = message[x:x + 12]  # Loop through chunks of 12
    if isPhoneNumber(chunk):
        print('Phone numbers found: ' + chunk)
print("Done!")
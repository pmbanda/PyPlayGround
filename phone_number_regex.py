import re
# define a function to determine a phone number
# pattern 405-654-98765

print()


def isPhoneNumber(phoneValue=""):
    # phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

    if phone_number_regex.search(phoneValue):
        return (phone_number_regex.search(phoneValue)).group()
    else:
        return False


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

# Loop through chunks of 12
for i in message.split():
    if isPhoneNumber(i):
        print('Phone numbers found ' + isPhoneNumber(i))

print()
print()
# Compile regex using groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(
    'My number is 415-555-4242. plus my personal cell 405-412-9728')
print('Get the first group of numbers {0}'.format(mo.group(1)))
print('Get the first group of numbers {0}'.format(mo.group(2)))
print('Get the first group of numbers {0}'.format(mo.group(0)))

print()

areaCode, phoneNumber = mo.groups()
print('Area code {0} phone number {1}'.format(areaCode, phoneNumber))

print()
print('Match one or more instances')
bat_regex = re.compile(r'bat(wo)+man')
mo = bat_regex.search('The adventures of batwoman')
print('The adventures of batwoman found-> ' + mo.group())
mo = bat_regex.search('The adventures of batwowowowoman')
print('The adventures of batwowowowoman found-> ' + mo.group())

print()
print('Match Zero or more instances Use(*)')

print("Match words containing multiple hahaha")
print("Greedy pattern matching")
regex = re.compile(r'(ha){3,5}')
mo = regex.search("hahahaha this is the Peter you know?")
print('Obtained ' + mo.group())

print()

print("Match words containing multiple hahaha")
print("Non-Greedy pattern matching")
regex = re.compile(r'(ha){3,5}?')
mo = regex.search("hahahahaha this is the Peter you know?")
print('Obtained ' + mo.group())



input()
print()

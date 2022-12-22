from create_user import create_user
from check_balance import check_balance

print("Welcome to the Bank")
print('\n')
print('Choose the service')
print('\n')
print('1. Create an account')
print('2. Check Balance')
print('3. Transact money')
print('\n')

def choose_service():
    print("Enter an option: ", end="")
    service = int(input())
    if(service>3):
        print("Invalid option")
        choose_service()
    else:
        return service

service = choose_service()

if(service == 1):
    create_user()
elif(service == 2):
    check_balance()
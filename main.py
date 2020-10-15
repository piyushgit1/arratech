from create import Create
from delete import delete
from read import Read
from update import Update
from request import req


def main():
    print('Available Options: C=Add_to_cart, R=Count_Cart_quantity, U=Update_any_item, D=Remove_from_cart')
    choice = input('Choose your option = ')

    if choice == 'C':
        createObj = Create()
        createObj.Add_to_cart()
    elif choice == 'R':
        readObj = Read()
        choose = input('Available option: A=calculate_price,B=cart_quantity')
        if choose == 'A':
            print(readObj.count_cart_quantity())
        else:
            print(readObj.calculate_price())
    elif choice == 'U':
        updateObj = Update()
        updateObj.update_cart_value()
    elif choice == 'D':
        deleteObj = delete()
        deleteObj.delt()
    else:
        print('Wrong choice, You are going exist.')






if __name__ == '__main__':
    reqer = req()
    reqer.makereqs()




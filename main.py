from src.morpho.str_to_mor import MoroseCode


if __name__=='__main__':
    
    while True:
        user = input('Select From Below \n1. Encode Content \n2.  Decode Content \nEnter Q to quit ----  ')
        if user=='1':
            password = input('Enter The pattern password : ')
            text = MoroseCode()
            text.initialize(password)
            content = input('Write Your Content :- ')
            print(f'Your Text : {content}')
            crypt=text.encrypt(content)
            print('Result Of your Input :',crypt)
        elif user=='2':
            password = input('Enter The pattern password : ')
            text = MoroseCode()
            text.initialize(password)
            content = input('Write Your Content :- ')
            print(f'Your Text : {content}')
            crypt= text.decrypt(content)
            print('Result Of your Input :',crypt)
        elif user.lower()=='q':
            break
        else:
            print('Invalid input, Try again\n')
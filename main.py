from src.morpho.str_to_mor import MoroseCode


if __name__=='__main__':
    
    while True:
        user = input('Select From Below \n1. Encode Content \n2.  Decode Content \nEnter Q to quit ----  ')
        if user=='1':
            print('\n\n-----------------------\n\n')
            password = input('Enter The pattern password : ')
            text = MoroseCode()
            text.initialize(password)
            content = input('Write Your Content :- ')
            print('\n\n-----------------------\n\n')
            print(f'Your Text : {content}')
            crypt=text.encrypt(content)
            print('\n\n-----------------------\n\n')
            print('Result Of your Input :',crypt)
            print('\n\n-----------------------\n\n')
        elif user=='2':
            print('\n\n-----------------------\n\n')
            password = input('Enter The pattern password : ')
            print('\n\n-----------------------\n\n')  
            text = MoroseCode()
            text.initialize(password)
            content = input('Write Your Content :- ')
            print('\n\n-----------------------\n\n')
            print(f'Your Text : {content}')
            print('\n\n-----------------------\n\n')
            crypt= text.decrypt(content)
            print('\n\n-----------------------\n\n')  
            print('Result Of your Input :',crypt)
            print('\n\n-----------------------\n\n') 
        elif user.lower()=='q':
            break
        else:
            print('\n\n-----------------------\n\n')
            print('Invalid input, Try again\n')
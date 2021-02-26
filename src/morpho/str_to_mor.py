import random
from .emojies import emoji
from .alphabets import alphabet

class MoroseCode:
    def __init__(self, sheet_password) -> None:
        self.encode={}
        self.decode={}
        random.seed(sheet_password)
        for _ in range(0,len(alphabet)):     
            rnd_alpha = random.randrange(0, len(alphabet))
            rnd_emoji = random.randrange(0, len(emoji))
            self.encode[alphabet[rnd_alpha]] = emoji[rnd_emoji]
            self.decode[emoji[rnd_emoji]] = alphabet[rnd_alpha]
            alphabet.pop(rnd_alpha)
            emoji.pop(rnd_emoji)
        # print(self.encode)
        # print(self.decode)
        
        
    
    def encrypt(self, str_to_convert:str):
        encrypt_text=""
        for ch in str_to_convert:
            encrypt_text=encrypt_text+ self.encode[ch]
        return encrypt_text
        
    def decrypt(self, str_to_decode:str):
        decrypt_text=""
        for ch in str_to_decode:
            decrypt_text=decrypt_text+ self.decode[ch]
            
        return decrypt_text
    

        
    

def main():
    encode={}
    decode={}
    random.seed(111)
    for i in range(0,len(alphabet)):     
        encode[alphabet[random.randrange(0, len(alphabet))]] = emoji[random.randrange(0, len(emoji))]
        decode[emoji[random.randrange(0, len(emoji))]] = alphabet[random.randrange(0, len(alphabet))]
        alphabet.pop(random.randrange(0, len(alphabet)))
        emoji.pop(random.randrange(0, len(emoji)))
    print(encode)
    print(decode)

if __name__=='__main__':
    
    main()

        

import random
from .emojies import emojis
from .alphabets import alphabet

class MoroseCode:
    def __init__(self) -> None:
        self.encode={}
        self.decode={}


    def initialize(self, sheet_password):
        self.encode={}
        self.decode={}
        random.seed(sheet_password)
        alphabets = alphabet.copy()
        emoji = emojis.copy()
        emoji1 = alphabet.copy()
        while(len(emoji)!=len(alphabets)+5):
            for i in range(0,random.randrange(2,10)):
                rnd = random.randrange(0, len(emoji1))
                emoji.append(emoji1[rnd])
                if i ==1:
                    emoji1.pop(rnd)
        print(len(emoji), len(alphabets))
        for _ in range(0,len(alphabets)):     
            rnd_alpha = random.randrange(0, len(alphabets))
            rnd_emoji = random.randrange(0, len(emoji))
            self.encode[alphabets[rnd_alpha]] = emoji[rnd_emoji]
            self.decode[emoji[rnd_emoji]] = alphabets[rnd_alpha]
            alphabets.pop(rnd_alpha)
            emoji.pop(rnd_emoji)
        # print(self.encode)
        # print(self.decode)
        
        
    
    def encrypt(self, str_to_convert):
        encrypt_text=""
        for ch in str_to_convert:
            encrypt_text=encrypt_text+ self.encode[ch]
        return encrypt_text
        
    def decrypt(self, str_to_decode):
        decrypt_text=""
        for ch in str_to_decode:
            decrypt_text = decrypt_text + self.decode[ch]
            
        return decrypt_text
    

        
    

# def main():
#     # encode={}
#     # decode={}
#     # random.seed(111)
#     # for i in range(0,len(alphabets)):     
#     #     encode[alphabets[random.randrange(0, len(alphabets))]] = emoji[random.randrange(0, len(emoji))]
#     #     decode[emoji[random.randrange(0, len(emoji))]] = alphabets[random.randrange(0, len(alphabets))]
#     #     alphabets.pop(random.randrange(0, len(alphabets)))
#     #     emoji.pop(random.randrange(0, len(emoji)))
#     # print(encode)
#     # print(decode)

# if __name__=='__main__':
    
#     main()

        

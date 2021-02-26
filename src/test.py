from morpho.str_to_mor import MoroseCode


if __name__=='__main__':
    code = MoroseCode()
    code.initialize('badar')
    crypt_=code.encrypt('badar')
    print(crypt_)
    code.initialize('badar')
    dcrypt= code.decrypt(crypt_)
    print(dcrypt)
    #  code = MoroseCode() 
#     code.initialize('badar')
#     crypt=code.encrypt('badar')
#     dcrypt= code.decrypt(crypt)
#     print(dcrypt)
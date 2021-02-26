from morpho.str_to_mor import MoroseCode

if __name__=='__main__':
    code = MoroseCode('badar')
    crypt=code.encrypt('badar')
    print(crypt)
    dcrypt= code.decrypt(crypt)
    print(dcrypt)
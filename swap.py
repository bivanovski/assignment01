import num2words

def swap(num1,num2):
    if (num1 > 0 and num1< 4) and (num2 > 0 and num2 < 4):
        print(f'a = {num2words.num2words(num1)}, b = {num2words.num2words(num2)}')
    else:
        print('Out of range')    
        

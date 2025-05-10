print("name : monalisa.n\n usn : 1AY24AI073\n section : O ")

def comma_code(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

my_list = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(my_list))  

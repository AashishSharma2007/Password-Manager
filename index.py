import os

# TODO: make it ask again and again
file_path = 'passwords.txt'
what_to_do = input('what do you want to do, add or get password (a/g) ?\n')

if what_to_do == 'a':
    file = open(file_path,'a')
    email = input('Email: ')
    website = input('Website: ')
    password = input('Password: ')

    str = email + ';' + website + ';' + password + ';\n'
    file.write(str)
    print('Saved ')
    file.close()
    input('')

elif what_to_do == 'g':
    file = open(file_path,'r')
    data = file.readlines()
    get_email = input("What is the 'email' ?\n").lower()
    get_website = input("What is the 'website' ?\n").lower()
    print('\n')
    
    for line in data:
        if (get_email == line.split(';')[0]) and (get_website == line.split(';')[1]):
          print(line)
        else: print('Searching...')
    file.close()
    input('')
else : print("Wrong argument it should be 'a' or 'g' only."); input('')
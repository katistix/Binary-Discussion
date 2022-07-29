import requests

url = 'http://207.154.197.160:5000/binary'

minn = input('Enter the minimum number: ')
maxx = input('Enter the maximum number: ')

minn = int(minn)
maxx = int(maxx)

found = False

print('Searching for a result between {} and {}...'.format(minn, maxx))

for i in range(minn, maxx+1):
    temp = ' '.join(format(ord(x),'b').zfill(8) for x in str(i))
    myobj = {'answer': temp}
    x = requests.post(url, json = myobj)



    binary_values = x.text.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character

    if(ascii_string!="Umm.. something seems wrong, I think you should check again your results"):
        print('\nFound the flag: ' + temp)
        found = True
        break

if(found == False):
    print('\nNo result found between {} and {}'.format(minn, maxx))
    print('\nTry again with a different range')
    print('\n')
    exit()
# Chapter 3 Exercises pp. 32-34
# 1-6-2017 

#ex 3-1

def right_justify(s):
    
    ''' takes a string namesd s as a parameter and prints the string with enough
        leading spaces so that the last letter of the string is in column 70 
    '''
    
    space = 70 - len(s)
    print(' ' * 70 + s)

right_justify('monty')


#ex 3-2

def do_twice(f, v):
    f(v)
    f(v)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(func, argu):
    func(argu)
    func(argu)

do_twice(print_twice, 'spam')

do_four(print_twice, 'samp')


#ex 3-3

def print_grid():

    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '* ')

    for i in range(4):
        print('| ' + '  ' * 4 + '| ' + '  ' * 4 + '| ')

    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '* ')

    for i in range(4):
        print('| ' + '  ' * 4 + '| ' + '  ' * 4 + '| ')
        
    print('+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '* ')


def print_beam():
    for i in range(4):
        print('+ ' + '- ' * 4, end='')
    print('+ ')

def print_hollow():  #can be combine with the function above
    for i in range(4):
        print('| ' + '  ' * 4, end='') 
    print('| ')

def print_grid_general():
    for i in range(4):
        print_beam()
        for j in range(4):
            print_hollow()
    print_beam()

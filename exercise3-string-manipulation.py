email = input("Please, enter your email\n")

def parseemail(e):
    at_position = e.find('@')
    username = e[0:at_position]
    domain_plus_extension = e[at_position: ]
    dot_position = domain_plus_extension.find('.')
    domain = domain_plus_extension[1: dot_position]
    extension = domain_plus_extension[dot_position: ]
    print(f'The username is {username}, the domain is {domain} and the extension is {extension}')

parseemail(email)

#test inputs could be an email without @

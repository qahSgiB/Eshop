class UserInputType:
    def __init__(self, name, type, **args):
        self.name = name
        self.type = type
        self.displayName = name if not 'displayName' in list(args.keys()) else args['displayName']
        self.extra = args



basicUserInputTypes = {
    'email': UserInputType('email', 'email', displayName='Email'),
    'password': UserInputType('password', 'password', displayName='Password'),
    'name': UserInputType('name', 'text', displayName='Name'),
    'addressSK': UserInputType('address', 'text', displayName='Address'),
    'zipSK': UserInputType('zip', 'text', displayName='PSC'),
}

generateBasicUserInputType = lambda name: UserInputType(name, 'text')

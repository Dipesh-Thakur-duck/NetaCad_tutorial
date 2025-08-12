# If you use backslash in python code and end a line with it, it will tell python to continue the line of code in the next line of code

def hello_world(greetings):
    if greetings == 'simple'\
    or greetings == 'not so simple':
        print('Hello world')
    else:
        return 'Hi'

hello_world('simple')
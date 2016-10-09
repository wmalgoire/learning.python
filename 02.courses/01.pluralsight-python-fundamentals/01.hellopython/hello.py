''' Hello Python '''


def print_message(message):
    '''print hello message'''
    print('Hello', str(message))


def loop_messages(messages):
    '''loop and print messages'''
    for messsage in messages:
        print_message(messsage)


loop_messages(range(5))

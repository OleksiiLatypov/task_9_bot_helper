def input_error(func):
    def wrapper(*args, **kwargs):
        #print('==================================')
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter Name!'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Bot: Please use whitespace when entering name and phone'
        except TypeError:
            return 'Wrong Command !'
    return wrapper


contacts = {}


@input_error
def hello():
    return f'Bot: Hello, how can I help you?'


@input_error
def add(user_input):
    if not user_input.split()[1].isalpha():
        raise ValueError('You provided wrong name')
    if not user_input.split()[2].isdigit():
        raise ValueError('You provided wrong phone')
    data = user_input.split()
    if data[1] in contacts:
        raise ValueError('Bot: This contact is already exist')
    for i in range(1, len(data), 2):
        contacts[data[i]] = data[i+1]
    return f'Bot: You successfully added contacts'


@input_error
def show_all(contacts):
    all_contacts = 'List of contacts:\n'
    for k, v in contacts.items():
        all_contacts += f'{k}: {v}\n'
    return all_contacts.strip('\n')


@input_error
def change(contacts, user_input):
    if user_input.split()[1] in contacts and user_input.split()[2].isdigit():
        #print(user_input.split()[1])

        contacts[user_input.split()[1]] = user_input.split()[2]
        return f'Bot: You successfully changed phone number'
    else:
        raise ValueError('This contact does not exist or phone number is not correct')



@input_error
def phone(contacts, user_input):
    return contacts.get(user_input.split()[1], f'Bot: This name does not exist, enter another name')


def wrong_input():
    return f'Bot: Wrong enter'


command = {
    'add': add,
    'hello': hello,
    'show all': show_all,
    'change': change,
    'phone': phone,
    'wrong_input': wrong_input
}


def main():
    key_words = ['good bye', 'bye', 'close', 'thank you', 'exit']
    while True:
        user_input = input('User: ').lower()
        if user_input.split()[0] == 'hello':
            print(command[user_input.split()[0]]())
        if user_input.split()[0] == 'add':
            print(command[user_input.split()[0]](user_input))
        if user_input == 'show all':
            print(command[user_input](contacts))
        if user_input.split()[0] == 'change':
            print(command[user_input.split()[0]](contacts, user_input))
        if user_input.split()[0] == 'phone':
            print(command[user_input.split()[0]](contacts, user_input))
        if user_input.split()[0] not in command and user_input not in key_words and user_input != 'show all':
            print(wrong_input())

        if user_input in key_words:
            print(f'Bot: see you next time')
            break


if __name__ == '__main__':
    main()

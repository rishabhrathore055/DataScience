stack = []
top = None
def isEmpty(stack):
    if(stack == []):
        return True
    else:
        return False
def push(stack,item):
    stack.append(item)
    top = len(stack) - 1
    print("pushed item: ",item)
def pop(stack):
    if(isEmpty(stack)):
        return('Underflow')
    else:
        item = stack.pop()
        if(len(stack) == 0):
            top = None
        else:
            top = len(stack) - 1
        return item
def peek(stack):
    if(isEmpty(stack)):
        return('Underflow')
    else:
        top = len(stack) - 1
        return stack[top]
def display(stack):
    if(isEmpty(stack)):
        print('Underflow')
    else:
        top = len(stack) - 1
        print(stack[top],'<----top')
        for i in range(top-1,-1,-1):
            print(stack[i])


while True:
    print('Stack Implementation')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')
    choice = int(input('Enter your choice(1-5): '))
    if(choice == 1):
        item = int(input('Enter the item to be pushed: '))
        push(stack,item)
        print('%d added suscessfully'%item)
        input('Press any key to continue...')
    elif(choice == 2):
        item = pop(stack)
        if(item == 'Underflow'):
            print('Underflow! Stack is empty')
        else:
            print('%d Popped item: '%item)
        input('Press any key to continue...')
    elif(choice == 3):
        item = peek(stack)
        if(item == 'Underflow'):
            print('Underflow! Stack is empty')
        else:
            print('%d is Top item: '%item)
        input('Press any key to continue...')
    elif(choice == 4):
        display(stack)
        input('Press any key to continue...')
    elif(choice == 5):
        break
    else:
        print('Invalid choice')
        input('Press any key to continue...')



 
solution = ['B', 'R', 'I', 'A', 'R']

def printListAsString(l):
    print(''.join(l))

def result(guess):
    result = ['-','-','-','-','-']
    for i in range (0, 5):
        if guess[i] == solution[i]:
            result[i] = guess[i]
    
    for i in range (0, 5):
        for j in range (0, 5):
            if result[i] == '-':
                if guess[i] == solution[j] and result[j] == '-':
                    result[i] = '*'
    return result

while True:
    guess = input('guess: ').upper()
    printListAsString(result(guess))
def fizzbuzz(number):
    '''
    if number divisible by 3 return 'fizz';
    5, 'buzz'; both, fizzbuzz
    else return number
    '''
    if not number % 3:
        if not number % 5:
            return 'fizzbuzz'
        else:
            return 'fizz'
    if not number % 5:
        return 'buzz'
    return number

def main():
    for i in range(1, 101):
        print fizzbuzz(i)

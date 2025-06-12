MAX_VALUE = 17

def main():
    # modify this starter code to call fizzbuzz
    # on every number from 1 to MAX_VALUE


    # divisible by 3, fizz
    # divisible by 5, buzz
    # multiple of 3 and 5 fizzbuzz
    # if it is not divisible by any of those, then return the number


    for i in range(1,MAX_VALUE + 1):
        to_say = fizzbuzz(i)
        print(to_say)



def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    Here are a few examples:
    fizzbuzz(3) returns "Fizz"
    fizzbuzz(15) returns "Fizzbuzz"
    fizzbuzz(2) returns 2
    """
    # TODO: fill in this function
    # integrer, strings, boolean
    # 15 
    if n % 3 == 0 and n % 5 == 0: # 
        return "Fizzbuzz"

    if n % 3 == 0:
        return "Fizz"

    if n % 5 == 0:
        return"Buzz"

    return n

if __name__ == '__main__':
    main()
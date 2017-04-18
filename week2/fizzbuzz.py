# prints numbers 1 to 100
# for multiples of 3 print fizz
# for multiples of 5 print buzz
# for multiples of 3 and 5 print fizzbuzz

for number in range(1,101):
    check_fizz = number%3
    check_buzz = number%5
    if check_fizz == 0 and check_buzz == 0:
        print("fizzbuzz")
    elif check_fizz == 0:
        print("fizz")
    elif check_buzz == 0:
        print("buzz")
    else:
        print(number)

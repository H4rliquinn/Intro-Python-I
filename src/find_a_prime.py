import math

# Get user number
while True:
    print("Gimme Number\n")
    user_input = input()
    if user_input == "q":
        break
    # Find highest prime that could be a factor
    highest_val = int(math.sqrt(int(user_input))//1)+1
    prime = False
    for x in range(2, highest_val):
        # print("vals", user_input, x, int(user_input) % x)
        if int(user_input) % x == 0:
            prime = True

    print("HV", highest_val, prime)

    if not prime:
        print("PRIME!\n")
    else:
        print("NOT PRIME!\n")

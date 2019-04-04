num = 6
print("You have " + str(num) + " chances!")
x = "amphibian"
y = ""
i = 0

while i < num and x != y:
    y = input("Guess the word: ")
    i += 1
    y = y.lower()
    if x == y:
        print("You got it!")
        break

    if x[0] == y[0]:
        print("You got the first letter!")
    if len(y) < 2 or len(x) < 2:
        pass
    else:
        if x[1] == y[1]:
            print("You got the second letter!")
        if len(y) < 3 or len(x) < 3:
            pass
        else:
            if x[2] == y[2]:
                print("You got the third letter!")
            if len(y) < 4 or len(x) < 4:
                pass
            else:
                if x[3] == y[3]:
                    print("You got the fourth letter!")
                if len(y) < 5 or len(x) < 5:
                    pass
                else:
                    if x[4] == y[4]:
                        print("You got the fifth letter!")
                    if len(y) < 6 or len(x) < 6:
                        pass
                    else:
                        if x[5] == y[5]:
                            print("You got the sixth letter!")
                        if len(y) < 7 or len(x) < 7:
                            pass
                        else:
                            if x[6] == y[6]:
                                print("You got the seventh letter!")
                            if len(y) < 8 or len(x) < 8:
                                pass
                            else:
                                if x[7] == y[7]:
                                    print("You got the eighth letter!")
                                if len(y) < 9 or len(x) < 9:
                                    pass
                                else:
                                    if x[8] == y[8]:
                                        print("You got the ninth letter!")
                                    if len(y) < 10 or len(x) < 10:
                                        pass
                                    else:
                                        if x[9] == y[9]:
                                            print("You got the tenth letter!")

    if len(x) == len(y):
        print("Your word is just the right length!")
    elif len(x) >= len(y):
        print("Your word is too short!")
    elif len(x) <= len(y):
        print("Your word is too long!")

    if i < num:
        print("You didn't guess the right word, try again!")
if i == num and x!=y:
     print("You ran out of chances!")
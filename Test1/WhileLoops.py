It = 10
while It > 1: #Skip number in between the number
    if It == 9:
        It = It - 1
        continue #used when want to skip current iteration and continue to the next iteration ( it will return to the first condition)
    if It == 3:
        break #break the while loop whenever condition is met
    print(It)

    It = It - 1

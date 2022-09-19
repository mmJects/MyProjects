#!usr/bin/env python3

# Birthday Paradox by Yun Yun

import random               # to get random values
def generate_birthdays():   # to generate ramdomly birthdays
    months = ["Apr","June","Nov","Sep","Feb","Jan","Mar","May","July","Aug","Oct","Dec"] # list of months
    get_month = random.choice(months)                                                   # randomly choose month
    if get_month in months[:4]:            # check with condition to get precise days
        get_day = random.randint(1,30)     # randomly choose days from 1 to 31 if the months are
    elif get_month == "Feb":               # if the random months is Feburary
        get_day = random.randint(1,28)     # choose days from 1 to 28
    else:                                  # if the other months
        get_day = random.randint(1,31)     # generate to 31 days
    return f"{get_month} {get_day}"        # return the random day

def ask_user():
    lst = list(map(str,range(1,101)))           # list for string numbers of 1 to 100 to limit user's input
    freq = "a"                                  # initialize the input False value to use in while
    while freq not in lst:                      # while the input is not the string list
        print("How many birthdays shall I generate?")  # ask the user
        freq = input("> ")
    return freq                                 # return user's input

# to generate the limited amount of birthday ( user's input , just check)
def freq_generate(freq,time=0):             
    def check_match():                      # to check identical birthdays generator function
        bd_lst = []                         # to store random birthdays
        for _ in range(int(freq)):          # loop through the frequencies of user's input
            bd = generate_birthdays()       # invoke generate randomly birthdays function
            if bd in bd_lst:                # if the random birthday is already in the list           
                yield bd                    # yield that birthday , use yield not to breake the loop
            bd_lst.append(bd)               # appending that birthday into the list
        if time == 0:                       # just a check to limit some intoduction letters
            print(f"Here are {freq} birthdays : ")  
            print(", ".join(bd_lst))        # displaying the random bithdays
    for i in check_match():                 # loop the generator function to get indetnical value
        dup = i                             # if there is identical value , assign it into a variable
    # return the identical birthday if it exits , return nothing if it doesn't    
    return dup                              

def million(freq):                          # million loop of user's limited frequencies
    similar = 0                             # a variable to stroe how many identicals are appeared in a million
    print(f"Generating {freq} birthdays 100,000 times....")
    input("Press Enter to begin...")
    for i in range(100_000):                # loop through a million times
        if i % 10_000 == 0:                 # if 10000 times is runned
            print(i, "simulations run...")  # show how much times has been runned
        # this part is a little complexed as I used the weird syntax in freq_generate fuction
        try:                            # try the generaotr function
            freq_generate(freq,3)       
        except UnboundLocalError:       # if the freq_generate function return nothing
            pass                        # do nothing
        else:                           # if there is an identical birthday
            similar += 1                # add one to the variable
    print("100000 simulations run...")  
    return similar                      # return the identical birthdays in a million times

if __name__ == "__main__":              # driver's function
    freq = ask_user()                   # user's input
    try:
        dup = freq_generate(int(freq))  # invoke freq_geneate function with user's input
    except UnboundLocalError:           # if there is no identical birthdays
        print(f"\nThere is no identical birthday in this {freq} people")    # show no match birthdays
    else:                               # if there is identical birthdays
        print(f"\nIn this simulation, {freq} people have a same birthday on {dup}") # display indentical birthday
        similar = million(freq)                         # invoke a million function with user's input
        probab = round(similar / 100_000 * 100,2)       # calculate percentage with the identical values
        print(f"Out of 100,000 simulations of {freq} people, there was amatching birthday in that group {similar} times.")
        print(f"This means that {freq} people have a {probab} % chance of having a matching birthday in their group.")
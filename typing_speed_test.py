from time import *
import random as r


def mistake(paragraph_test, user_test):
    error = 0
    for i in range(len(paragraph_test)):
        try:
            if paragraph_test[i] != user_test[i]:
                error += 1
        except Exception as e:
            error += 1

    return error


def speed_time(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(user_input)/time_roundoff
    return round(speed)



test = [
    "The quick brown fox jumps over the lazy dog.",
    "How razorback-jumping frogs can level six piqued gymnasts!",
    "Pack my box with five dozen liquor jugs.",
    "The five boxing wizards jump quickly.",
    "Jackdaws love my big sphinx of quartz.",
    "Sympathizing would fix Quaker objectives.",
    "Waltz, nymph, for quick jigs vex Bud.",
    "Sphinx of black quartz, judge my vow.",
    "The jay, pig, fox, zebra, and my wolves quack!",
    "Cozy lummox gives smart squid who asks for job pen.",
]
test1 = r.choice(test)
print("    *****Typing speed*****")
print(test1)
print()
print()

time_1 = time()
test_input = input(" Enter: ")
time_2 = time()


print("Speed : " ,speed_time(time_1, time_2, test_input),"w/sec")
print("Error : ",mistake(test1, test_input))


import random

def generate_random(stop, start = 1, size = 10):
    numbers_up_to_stop = []
    counter = 0
    while counter < size:
        numbers_up_to_stop.append(random.randint(start, stop))
        counter += 1
    return numbers_up_to_stop, start, stop  


def gameplay_logic(list_of_nums,start, stop):
    for index in range(len(list_of_nums)):
        guess = int(input("Enter an integer from {start} to {stop}: ".format(start = start,stop =stop)))
        while list_of_nums[index] != guess:
            if guess < list_of_nums[index]:
                print("guess is low")
            elif guess > list_of_nums[index]:
                print("guess is high")
            else:
                break
            guess = int(input("Enter an integer from {start} to {stop}: ".format(start = start,stop = stop )))
        print("you guessed it!")

def main():
    
    list_to_99,start, stop = generate_random(99)
    gameplay_logic(list_to_99,start,stop)

    list_to_49,start, stop = generate_random(49)
    gameplay_logic(list_to_49,start,stop)
    

    


if __name__ == '__main__':
    main()
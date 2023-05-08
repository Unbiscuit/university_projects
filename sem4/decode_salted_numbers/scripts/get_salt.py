import collections

def main():
    given_numbers = []
    salted_numbers = []
    theoretical_salt = []
    with open("outputs/known_numbers", "r") as known_numbers:
        for number in known_numbers:
            given_numbers.append(int(number))

    with open("outputs/salted_numbers", "r") as decoded_numbers:
        for line in decoded_numbers:
            salted_numbers.append(int(line[-12:-1]))

    for salted_number in salted_numbers:
        for given_number in given_numbers:
            theoretical_salt.append(salted_number - given_number)
    
    print([item for item, count in collections.Counter(theoretical_salt).items() if count == 5])

if __name__ == "__main__":
    main()
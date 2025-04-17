# activity 1:
a_word = input("Save text to file:")
file = None
try:
    file = open("exo1.txt", "w")
    file.write(a_word)
    # with open("exo1.txt", "w") as file:
    # file.write(a_word)
except OSError:
    print("Error: unable to write to file exo1.txt")
finally:
    if file is not None:
        file.close()

# activity 2:
def save_to_log(entry):
    try:
        with open("exo1.txt", "a") as file:
            file.write(entry + "\n")
    except OSError:
        print("Error: unable to write to file exo1.txt")
    finally:
        if file is not None:
            file.close()

text = input("Enter text to add to file:")
save_to_log(text)

# activity 3:
try:
    with open("exo1.txt", "r") as file:
        file = file.readlines()
        for line in file:
            print(line.upper())
except OSError:
    print("Error: unable to read file exo1.txt")

# activity 4:
def to_upper_case(input_file):
    data = []
    try:
        with open(input_file, "r") as file:
            for line in file:
                data.append(line.strip().upper())
            return data
    except OSError:
        print("Error: unable to read file exo1.txt")

print(to_upper_case("exo1.txt"))

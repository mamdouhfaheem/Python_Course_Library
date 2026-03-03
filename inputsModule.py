

def ask_for_int(prompt="Please enter a number"):
    try:
        num = int(input(prompt))
    except Exception as e :
        print("Please enter a valid number")
        return ask_for_int(prompt)
    else:
        if num <0 :
            print("Book number must be greater than zero")
            return ask_for_int(prompt)

        return num

def ask_for_name(prompt="Please enter a name"):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        print("----Please enter a valid name")


def ask_for_non_empty_string(prompt="Please enter a non-empty string"):
    while True:
        input_string = input(prompt)
        input_string = input_string.strip()
        if len(input_string) > 0:
            return input_string
        print("----Please enter a non-empty string---")


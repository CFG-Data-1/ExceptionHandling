# Teenager club registration program

def age_validation(age):
    '''

    :param age: int
    :return: True  if teenager, false if not
    '''

    if age < 0:
        raise ValueError("Negative age is not allowed")

    assert 12 < age < 20

    return True


def name_validation(name):

    if "," not in name:
        raise ValueError("Incorrect input: missing ',' to separate name and surname")

    name, surname = name.split(",")

    if not len(name) or not len(surname):
        raise ValueError("Incorrect input: missing name or surname values")

isSuccessful= False

try:
    name = input("Please enter your name and surname separated by coma: ")
    name_validation(name)
    age = int(input("Enter your age: "))
    age_validation(age)

except ValueError as exc:
    print("Invalid input: %s" % exc)

except AssertionError as exc:
    print("Assertion Error, age is in the range of teenager: %s" % exc)

else :
    with open("registraton_file.txt", 'a+') as file:
        file.write("New member name: {} and age {}. \n".format(name, age))
    isSuccessful = True

finally:
    if isSuccessful:
        print("Registration Process completed SUCCESSFULLY!")
    else :
        print("Registration Process aborted!")




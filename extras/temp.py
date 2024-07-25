def validate(start, end):
    def wrapper(function):
        def inner():
            value = function()
            if value not in range(start, end+1):
                print("Input Should be between {0}-{1}".format(start, end+1))
            else:
                print("Accepted")
        return inner
    return wrapper


@validate(0, 100)
def add_marks():
    while True:
        try:
            marks = int(input("Enter Marks: "))
            return marks
        except ValueError:
            print("Invalid input. Please enter an integer")

add_marks()



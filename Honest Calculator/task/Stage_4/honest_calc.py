msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

running = True
memory = 0


# Start Stage 4/5
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b if b != 0.0 else print(msg_3)


def is_one_digit(a):
    try:
        if a == int(a):
            return -10 < a < 10
    except ValueError:
        return False


def calc(a, op, b):
    # Stage 2/5
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = subtract(a, b)
    elif op == "*":
        res = multiply(a, b)
    else:
        res = division(a, b)
    return res


def check(a, op, b):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg += msg_6
    if op == "*" and (a == 1 or b == 1):
        msg += msg_7
    if (a == 0 or b == 0) and (op != "/"):
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)
# End Stage 4/5


# Stage 1/5
while running:
    print(msg_0)
    user_input = input()
    x, operation, y = user_input.split()

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    valid_operations = '+-*/'
    if operation not in valid_operations:
        print(msg_2)
        continue

    check(x, operation, y)

    result = calc(x, operation, y)
    if result is not None:
        print(result)
    else:
        continue

    # Stage 3/5
    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False

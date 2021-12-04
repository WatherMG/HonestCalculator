msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

valid_operations = ["+", "-", "/", "*"]
running = True
memory = 0
# Stage 1/5
while running:
    print(msg_0)
    user_input = input()
    x, operation, y = user_input.split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if operation not in valid_operations:
        print(msg_2)
        continue

        # Stage 2/5
    result = 0
    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        if y == 0:
            print(msg_3)
            continue
        else:
            result = x / y
    print(result)

    running = False


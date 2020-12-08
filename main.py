with open("input.txt") as file:
    data = file.read().split("\n")


def readline(line):
    command = line.split(" ")
    return {"type": command[0], "value": int(command[1])}


acc = 0
seen = {}
i = 0
repeat = False
while not repeat or i <= len(data):
    command = readline(data[i])
    if i in seen:
        print(f"Repeat variable, acc is {acc}")
        repeat = True
        break
    seen.update({i: True})
    if command["type"] == "acc":
        acc += command["value"]
        i += 1
    elif command["type"] == "jmp":
        i += command["value"]
    else:
        i += 1

# Part two
def run_program(modified_data):
    acc = 0;
    i = 0;
    t = 0;
    while i < len(data) and t < 5000:
        t += 1
        command = readline(modified_data[i])
        if command["type"] == "acc":
            acc += command["value"]
            i += 1
        elif command["type"] == "jmp":
            i += command["value"]
        else:
            i += 1
    if i == len(data):
        print(f"ACC was {acc}")


for i in range(0, len(data)-1):
    command = readline(data[i])
    modified_data = data.copy()
    if command["type"] == "nop":
        modified_data[i] = f"jmp {command['value']}"
        run_program(modified_data)
    elif command["type"] == "jmp":
        modified_data[i] = f"nop {command['value']}"
        run_program(modified_data)
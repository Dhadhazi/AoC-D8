with open("input.txt") as file:
    data = file.read().split("\n")


def readline(line):
    command = line.split(" ")
    return {"type": command[0], "value": int(command[1])}


acc = 0
seen = {}
i = 0
repeat = False
while not repeat:
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
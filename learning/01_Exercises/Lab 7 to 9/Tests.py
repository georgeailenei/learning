
ceva = {"Batman": 2, "Avengers": 3}
sameDic = {}

with open("tests", "w") as file:
    for key, value in ceva.items():
        file.write(key + ": ")
        file.write(str(value) + "\n")

with open("tests", "r") as f:
    lines = f.readlines()

    for line in lines:
        static = line.split(":")
        sameDic[static[0].strip()] = static[1].strip()

print(sameDic)



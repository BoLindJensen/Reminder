import json

with open("Input.json", "r") as inputFile:
    obj = json.load(inputFile)
    with open("Output.txt", "w") as outputFile:
        outputFile.write(obj["name"] + " is interested in the following job positions:\n")
        for hobby in obj["jobapplications"]:
            outputFile.write(hobby + "\n")

        outputFile.write("\n")

        outputFile.write("My Hobbies are:\n")
        for hobby in obj["hobbies"]:
            outputFile.write(hobby + "\n")


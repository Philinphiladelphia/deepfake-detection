import os

trans = open("transcript.txt", "r")

csv = ""


fileNames = os.listdir("./preprocessed")

i  = 0

allLines = trans.readlines()

for line in allLines:
    if line == "\n":
        continue

    line = line.replace(",", "")

    line = line.strip()

    csvLine = fileNames[i] + ","

    csvLine += line + ","
    csvLine += line

    csv += csvLine + "\n"

    i += 1

csv = csv.strip()

output = open("training.csv", "w")

output.writelines(csv)

output.close()

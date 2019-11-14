def calcReimburse(rate, startMileage, endMileage):
    return eval(f"{rate} * ({endMileage} - {startMileage}) / 100") # evaluates string representation of expression

def readFile(fileName):
    with open(fileName, 'r') as file: # read in contents of file
        lines = file.read().split("\n") # lines is a list of lines of the file
    data = [[], []]
    # data[0] will hold subtitles
    # data[1] will hold list of lists of car data
    for line in lines:
        tokens = line.split(',')  # tokens obtained using comma delimiter
        if not line == lines[0]: # if line is not equal to the heading line
            data[1].append(tokens)
        if line == lines[0]:
            data[0] = tokens
    for carData in data[1]: # for each car data list, calculate the reimbursement
        val_reimb = calcReimburse(carData[1], carData[2], carData[3])
        carData.append(val_reimb) # add the reimbursement amount to the appropriate car data list
    return data

def writeFile(data, fileName):
    with open(fileName, 'w') as file: # open file for writing
        for subtitle in data[0]:  # write subtitles to file first and newline
            if not subtitle == data[0][-1]: # if not last element, include a comma
                file.write(subtitle + ",")
            else:
                file.write(subtitle)
        file.write("\n") # newline after subtitles
        for carData in data[1]: # write car data to file
            for item in carData:
                if not item == carData[-1]: # if not last element, include a comma
                    file.write(str(item) + ",")
                else:
                    file.write(str(item))
            file.write("\n") # newline after each car's data is done being written to file

def main():
    data = readFile("dataIn.csv")
    writeFile(data, "dataOut.csv")

if __name__ == '__main__':
    main()
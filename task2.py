from csv import reader, writer

dataFiles = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

outFile = open("data/cumulative_sales_data.csv", "w", newline="")
CSVWriter = writer(outFile)
for file_name in dataFiles:
    inFile = open("data/" + file_name, "r", newline="")
    CSVReader = reader(inFile)
    next(CSVReader)
    for line_data in CSVReader:
        if line_data[0] != "pink morsel":
            continue
        sales = float(line_data[1].strip('$')) * float(line_data[2])
        CSVWriter.writerow([sales, line_data[3], line_data[4]])
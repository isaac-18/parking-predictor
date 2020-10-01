import openpyxl
import string
import time

# ----- GOALS ----
# - I want to test populating data within a range then begin overwriting when reaching the end.
# - This can be done by saving the last edited cell to a txt and then reading that cell name 
#   when the script is run again.
# - I also want to test using time module to write time value to excel file

# ---- POTENTIAL ISSUES ----
# - Need to figure out what to do when file is initially empty at first program run.
#     - Init function?
#     - Give starting cell location
#  - Not using startingCell value to begin interating


filename = 'testing_data.xlsx'
wb = openpyxl.load_workbook(filename)
ws1 = wb.active

columnRange = list(string.ascii_uppercase[1:22])
cnt = 1

if ws1.max_row == 1:
    startingCell = 'B2'
else:
    with open('last_cell.txt', 'r') as f:
        lastEditedCell = f.read()

    lastCellCol = lastEditedCell[0]
    lastCellRow = int(lastEditedCell[1])

    if (lastCellCol == 'V' and lastCellRow >= 9):
        nextCol = columnRange[0]
        nextRow = 2
    else:
        if (lastCellRow >= 9):
            nextCol = columnRange[columnRange.index(lastCellCol) + 1]
            nextRow = 2
        else:
            nextRow = lastCellRow + 1

    startingCell = "{}{}".format(nextCol, nextRow)

# Need to use startingCell 
# Also, while True: around the below?

for column in columnRange:
    for row in range(2, 10):
        currentCell = "{}{}".format(column, row)
        ws1[currentCell] = cnt
        
        cnt += 1
        with open('last_cell.txt', 'w') as f:
            f.write(currentCell)
        wb.save(filename)
    time.sleep(5) 
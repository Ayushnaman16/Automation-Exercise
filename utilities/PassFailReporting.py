from utilities.Excel_Utility import writeCellData, fillGreenColor, fillRedColor

def update_test_result(file, sheet, row, col, status):
    writeCellData(file, sheet, row, col, status)

    if status.upper() == "PASS":
        fillGreenColor(file, sheet, row, col)

    elif status.upper() == "FAIL":
        fillRedColor(file, sheet, row, col)
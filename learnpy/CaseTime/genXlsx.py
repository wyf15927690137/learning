# import xlsxwriter module
import xlsxwriter
import ast
import datetime

class GenXLSX:
    def __init__(self):
        pass

    def genXlsx(self, file):
        workbook = xlsxwriter.Workbook(f'{file}.xlsx')
        worksheet = workbook.add_worksheet("cases")

        row = 0
        col = 0

        format = workbook.add_format()
        format.set_pattern(1)
        format.set_bg_color('red')

        zero_time = datetime.datetime.strptime("00:00:00","%H:%M:%S")
        max_time = datetime.datetime.strptime("0:02:30","%H:%M:%S") - zero_time

        s_file = open(f"{file}_case.txt", "r", encoding='UTF-8')
        all_content = s_file.read()
        lines = all_content.split('\n')
        for line in lines:
            try:
                line = ast.literal_eval(line)
            except:
                pass
            if type(line) == list:
                worksheet.write(row, col, line[0])
                worksheet.write(row, col + 1, line[1])
                if datetime.datetime.strptime(line[1], "%H:%M:%S") - zero_time > max_time:
                    worksheet.write(row, col +1, line[1], format)
                worksheet.write(row, col + 2, line[2])
                if line[2] == "FAILED":
                    worksheet.write(row, col + 2, line[2], format)
            else:
                worksheet.write(row, col, line)
            row += 1
        workbook.close()

if __name__ == "__main__":
    genXls = GenXLSX()
    genXls.genXlsx(20097)
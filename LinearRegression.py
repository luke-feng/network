import xlrd as xl
import xlwt
import numpy as np
from sklearn.linear_model import LinearRegression

def open_excel(file ):
    try:
        data = xl.open_workbook(file)
        return data
    except Exception,e:
        print(e.message)

def excel_get_col_data(file, colid1,colid2  ):
    data = open_excel(file)
    table = data.sheets()[0]
    nrows = table.nrows
    x = np.array(table.col_values(colid1)).reshape(-1,1)
    y = table.col_values(colid2)
    return x,y

def linear_regression(file):
    x,y = excel_get_col_data(file,0,1)
    model = LinearRegression()
    model.fit(x, y)
    print('y = %fx + %f' % (model.coef_, model.intercept_))
    r2 = model.score(x, y)
    print(r2)
    return model.coef_, model.intercept_,r2

def result_write(file,coef,intercept,r2):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet()
    sheet.write(0,0,"coef")
    sheet.write(0, 1, "intercept")
    sheet.write(0, 2, "r2")
    for line in range(0,coef.lenth,1):
        sheet.write(line+1,0,coef[line])
        sheet.write(line + 1, 1, intercept[line])
        sheet.write(line + 1, 2, r2[line])
    wbk.save(file)


def main():
    path = ""
    seed = 0.00005
    n_node = 1000  # number of nodes
    filename = "overvier.xls"
    coef = []
    intercept = []
    r2 = []
    outputfile = path+"ER_result.xls"
    for iter in range(1,100,1):
        p_edge = seed * iter  # p
        lambda_p = p_edge * (n_node - 1)
        foldername = "ER_N1000_lammda_%f"+lambda_p+"_%d"+iter+"//"
        filepath = path + foldername + filename
        x,y,r = linear_regression(filepath)
        coef.append(x)
        intercept.append(y)
        r2.append(r)
        result_write(outputfile,coef,intercept,r2)


if __name__=="__main__":
    main()





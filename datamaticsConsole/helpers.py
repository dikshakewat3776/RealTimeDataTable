import pandas as pd
import numpy as np
from datamaticsConsole.constants import REMOVE_FROM_LIST, ADD_TO_LIST


def tables_to_dataframe(tablesList):
    df = pd.DataFrame(tablesList)
    return df


def write_to_html_file(df, title, filename):
    result = '''
    <html>
    <head>
    <style>

    h2 {
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }
    table tbody tr:hover {
        background-color: #dddddd;
    }
    .wide {
        width: 90%; 
    }
    </style>
    </head>
    <body>
    '''
    result += '<h2> %s </h2>\n' % title
    if type(df) == pd.io.formats.style.Styler:
        result += df.render()
    else:
        result += df.to_html(classes='wide', escape=False)
    result += '''
    </body>
    </html>
    '''
    with open(filename, 'w') as f:
        f.write(result)
    return filename


def unique_list(anylist):
    x = np.array(anylist)
    unq = list(np.unique(x))
    return unq


def remove_unwanted(anylist):
    unwantedList = REMOVE_FROM_LIST
    for i in unwantedList:
        if i in anylist:
            anylist.remove(i)
        else:
            anylist = anylist
    return anylist


def extend_to_list(anylist):
    to_extend = ADD_TO_LIST
    anylist.extend(to_extend)
    return anylist


def merge_dict(dict1, dict2):
    dict2.update(dict1)
    return dict2


if __name__ == "__main__":
    a = {'col_company': ['index', 'CompanyId', 'Company', 'Speciality', 'IndustryType1', 'SubIndustryType1',
                         'EmployeeSizeFromValue', 'EmployeeSizeToValue'],
         'col_contact': ['index', 'FirstName', 'LastName', 'JobTitle1', 'JobLevel1', 'JobFunction1',
                         'Contact Country', 'CompanyId']}
    b = {'sideColsList': ['Company', 'Contact Country', 'IndustryType1', 'JobFunction1', 'JobLevel1', 'JobTitle1',
                          'Speciality', 'SubIndustryType1', 'EmployeeSize']}

    m = merge_dict(a, b)
    print(m)


    # a = [{'TABLE_NAME': 'company', 'COLUMN_NAME': 'index'}, {'TABLE_NAME': 'company', 'COLUMN_NAME': 'CompanyId'}]
    # n = []
    # for i in a:
    #     n.append(i['COLUMN_NAME'])
    # print(n)

    # list1 = ['hi', 'bye', 'hello', 'whatsup', 'meow']
    # extend_list = ['hi', 'hello']
    # a = extend_to_list(list1)
    # print(a)
    # a = remove_unwanted(list1)
    # print(a)
    # if unwanted_num in a:
    #     print("True")
    # if any(i == unwanted_num for i in list1):
    #     print("True")
    #     for i in unwanted_num:
    #         a.remove(i)
    #     print(a)
    # else:
    #     print("False")
    #     print(a)
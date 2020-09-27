from django.shortcuts import render

from datamaticsConsole.constants import DATABASE_CONFIGS, ADD_TO_SEARCH, REMOVE_FROM_SEARCH
from datamaticsConsole.sql_functions import table_overview, column_overview, get_table_column_names, get_table_names, \
    show_search_table
from datamaticsConsole.helpers import unique_list, remove_unwanted, extend_to_list, merge_dict
import copy


# from flask import Flask
# app = Flask(__name__)


def Home(request):
    print(request)
    tabs = table_overview()
    cols = column_overview()
    overviewList = {'tableList': tabs,
                    'columnList': cols}
    response = render(request, 'home.html', overviewList)
    return response


def Search(request):
    cols = column_overview()
    col_names = []
    for i in cols:
        col_names.append(i['COLUMN_NAME'])
    unique_cols = unique_list(col_names)

    filteredList = remove_unwanted(unique_cols)
    finalList = extend_to_list(filteredList)
    sideColsList = copy.deepcopy(finalList)

    for i in ADD_TO_SEARCH:
        unique_cols.append(i)
    unique_cols.remove('EmployeeSize')
    unique_cols.remove('CompanyId')
    unique_cols.remove('Contact Country')

    searchTable = show_search_table(5000)    # Can be made configurable

    finalList = {'sideColsList': sideColsList,
                 'colsSearch': unique_cols,
                 'searchTable': searchTable}

    response = render(request, 'search.html', finalList)
    return response


def Analyze(request):
    print(request)
    response = render(request, 'analyze.html')
    return response


def filterEntries(request):
    if request.method == 'POST':
        print("MEOW")
    # print(columnName)
    # response = render('filterEntries.html')
    # return response


# def allEntries(request):
#     print(request)
#     cols = column_overview()
#     overviewList = {'columnList': cols}
#     response = render(request, 'allEntries.html', overviewList)



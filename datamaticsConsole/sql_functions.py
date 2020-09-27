import pymysql
from datamaticsConsole.constants import DATABASE_CONFIGS
import cachetools.func
import time


# from cachetools import TTLCache

# cache = TTLCache(maxsize=360, ttl=180)


def make_mysql_connection():
    try:
        server = DATABASE_CONFIGS['DB_HOST']
        username = DATABASE_CONFIGS['DB_USER']
        password = DATABASE_CONFIGS['DB_PASSWORD']
        database_name = DATABASE_CONFIGS['DB_NAME']
        return pymysql.connect(server, username, password, database_name)
    except Exception as e:
        print("Could not establish a connection with the remote server: " + str(e))


def execute_sql_query(query):
    cursor = None
    connection = None
    try:
        try:
            connection = make_mysql_connection()
        except Exception as e:
            connection = None
            print("Could not establish a connection with the remote server: " + str(e))
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        if cursor.rowcount == 1:
            row = cursor.fetchone()
        else:
            row = cursor.fetchall()
        connection.commit()
        return {"Success": True, "Row": row}
    except Exception as e:
        raise Exception("Procedure Call failed with query: " + query + " and Error: " + str(e))
    finally:
        cursor.close()
        connection.close()


@cachetools.func.ttl_cache(maxsize=360, ttl=5 * 60)
def get_table_names(database_name):
    table_names = []
    r = execute_sql_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='{}'"
                          .format(database_name))
    if r['Success']:
        if isinstance(r, dict):
            tableList = r['Row']
            for i in tableList:
                for val in i.values():
                    table_names.append(val)
    return table_names


@cachetools.func.ttl_cache(maxsize=360, ttl=5 * 60)
def get_table_count(database_name, table_name):
    table_count = None
    r = execute_sql_query("SELECT count(*) FROM {}.{}" . format(database_name, table_name))
    if r['Success']:
        if isinstance(r, dict):
            resp = r['Row']
            for table_count in resp.values():
                return table_count


@cachetools.func.ttl_cache(maxsize=360, ttl=5 * 60)
def table_overview():
    table_info = []
    database_name = DATABASE_CONFIGS['DB_NAME']
    table_names_list = get_table_names(database_name)
    for table in table_names_list:
        table_count = get_table_count(database_name=database_name, table_name=table)
        response = {
            'SCHEMA_NAME': database_name,
            'TABLE_NAME': table,
            'TABLE_COUNT': table_count
        }
        table_info.append(response)
    return table_info


@cachetools.func.ttl_cache(maxsize=360, ttl=5 * 60)
def get_table_column_names(database_name, table_name):
    column_names = []
    r = execute_sql_query("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='{}' "
                          "AND `TABLE_NAME`='{}'" . format(database_name, table_name))
    if r['Success']:
        if isinstance(r, dict):
            tableList = r['Row']
            for i in tableList:
                for val in i.values():
                    column_names.append(val)
    return column_names


@cachetools.func.ttl_cache(maxsize=360, ttl=5 * 60)
def column_overview():
    column_info = []
    database_name = DATABASE_CONFIGS['DB_NAME']
    table_names_list = get_table_names(database_name)
    for table in table_names_list:
        column_names_list = get_table_column_names(database_name, table)
        for col in column_names_list:
            response = {
                'TABLE_NAME': table,
                'COLUMN_NAME': col
            }
            column_info.append(response)
    return column_info


@cachetools.func.ttl_cache(maxsize=360, ttl=10 * 60)
def get_distinct_entries_in_columns(database_name, table_name, column_name):
    distinct_entries = []
    r = execute_sql_query("SELECT distinct {} FROM {}.{}" .format(column_name, database_name, table_name))
    if r['Success']:
        if isinstance(r, dict):
            tableList = r['Row']
            for i in tableList:
                for val in i.values():
                    distinct_entries.append(val)
    return distinct_entries


# Can be made configurable
@cachetools.func.ttl_cache(maxsize=1000000, ttl=30 * 60)
def show_search_table(limit):
    tableList = []
    r = execute_sql_query("SELECT Company,IndustryType1,JobFunction1, JobLevel1, JobTitle1, Speciality, "
                          "SubIndustryType1, FirstName, LastName, EmployeeSizeFromValue, EmployeeSizeToValue "
                          "FROM data.company INNER JOIN data.contact ON "
                          "data.company.CompanyId = data.contact.CompanyId LIMIT {}"
                          .format(limit))
    if r['Success']:
        if isinstance(r, dict):
            tableList = r['Row']
            # for i in tableList:
            #     print(i)
            #     for val in i.values():
            #         print(val)
            #         entries.append(val)
    return tableList


if __name__ == "__main__":
    a = show_search_table(2)
    for i in a:
        print(i)
    # print(a)
    # for i in a:
    #     print(i)
    # t1 = time.time()
    # a = show_search_table(1)
    # print(a)
    # t2 = time.time()
    # print(t2-t1)
    # a = get_table_names('data')
    # r = {}
    # for i in range(0, len(a)):
    #     for j in a:
    #         b = get_table_column_names('data', j)
    #         r["col{}". format(i)] = b
    # print(r)
    # r["add_something"] = "meow"
    # print(r)
    # for i in a:
    #     for j in range(0, len(a))
    #     b = get_table_column_names('data', i)
    #     r[]
    # print(r)
    # a = column_overview()
    # print("#" * 50)
    # print(a)
    # t1 = time.time()
    # a = get_distinct_entries_in_columns('data', 'company', 'Company')
    # print(a)
    # t2 = time.time()
    # print(t2-t1)
    # print(len(a))

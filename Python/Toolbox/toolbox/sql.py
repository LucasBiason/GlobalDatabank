from typing import List, Optional
from django.conf import settings

from django.db import connections, transaction


def sql_to_dict(select_sql: str, param: Optional[str]=None, 
                database_alias: Optional[str]='default') -> dict:
    """
        Execute the query 'select_sql' in databank, passing 'param' as a parameter to the cursor,
        and returns the result of the query, with each line converted to a dictionary.
        The 'database_alias' parameter is the database alias against which to select.
        Possible aliases are the keys of the 'DATABASES' dictionary, which is located in the settings.
    """
    assert database_alias in settings.DATABASES
    cursor = connections[database_alias].cursor()
    cursor.execute(select_sql, param)
    fields_names = [name[0] for name in cursor.description]
    to_return = []
    for line in cursor.fetchall():
        line_list = []
        for field in zip(fields_names, line):
            line_list.append(field)
        to_return.append(dict(line_list))
    return to_return


def query_value(select_sql: str, database_alias: Optional[str]='default') -> str:
    """
        Executes the query 'select_sql' in databank and returns the value of the first column of the first row returned by the query.
        The 'database_alias' parameter is the database alias against which to select.
        Possible aliases are the keys of the 'DATABASES' dictionary, which is located in the settings.
    """
    assert database_alias in settings.DATABASES

    cursor = connections[database_alias].cursor()
    cursor.execute(select_sql)
    to_return = cursor.fetchone()
    return to_return[0] if to_return else None


def exec_sql(select_sql: str, database_alias: Optional[str]='default'):
    """
        Run a 'select_sql' command on databank.
        The 'database_alias' parameter is the database alias which to select.
        Possible aliases are the keys of the 'DATABASES' dictionary, which is located in the settings.
    """
    with transaction.atomic():
        assert database_alias in settings.DATABASES
        con = connections[database_alias]
        cursor = con.cursor()
        cursor.execute(select_sql)
        try:
            con.commit()
            con.close()
        except Exception as msg:
            print(f"Error: {msg}")


def sql_escape(valor: str) -> str:
    return valor.replace(r'%','').replace("'","''")

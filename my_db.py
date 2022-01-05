import mysql.connector

def interact_db(query, query_type: str):
    return_value = False
    # creating a connection to the db
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment_10_db')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':

        connection.commit()
        return_value = True



    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result



    connection.close()
    cursor.close()
    return return_value

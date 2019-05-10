import json
import sqlite3

def lambda_handler(event, context):
    # TODO implement
    conn = sqlite3.connect('/var/task/testdb.db')
    query = "select personID, people.first_name || ' ' || people.last_name as Name, count(*) as Num_of_visits from (select personId from visits group by  personId, siteId) as group_results left join people on people.id = group_results.personId group by personId order by Num_of_visits desc LIMIT 10"
    cursor = conn.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

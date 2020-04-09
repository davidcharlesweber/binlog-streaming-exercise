import json
import boto3
import os
import requests
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent)
from common import get_secret, serialize, awsauth
def main():
    secret = json.loads(get_secret())

    stream = BinLogStreamReader(
        connection_settings={
            "host": secret['db_host'],
            "port": int(secret['db_port']),
            "user": secret['db_user'],
            "passwd": secret['db_password']
        },
        server_id=10112335,
        blocking=True,
        resume_stream=True,
        only_tables=['users'],
        only_events=[UpdateRowsEvent]
    )

    for binlogevent in stream:
        url = os.environ['ES'] + '/primary_database/primary/'
        for row in binlogevent.rows:
            if isinstance(binlogevent, DeleteRowsEvent):
                r = requests.delete(url + str(row["values"]["indv_key"]), auth=awsauth, headers={"Content-Type": "application/json"})
                continue
            if isinstance(binlogevent, UpdateRowsEvent):
                current_data = row['after_values']
            else:
                current_data = row['values']
            r = requests.put(url + str(current_data["indv_key"]), auth=awsauth, data=json.dumps(current_data, sort_keys=True, default=serialize), headers={"Content-Type": "application/json"})
if __name__ == "__main__":
    main()

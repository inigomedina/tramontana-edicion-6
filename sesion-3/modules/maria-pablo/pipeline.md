## Pipeline
python3 fetch.py events | python3 maria-pablo/counter.py user_id | python3 maria-pablo/topn.py 5 | python3 maria-pablo/join.py users.json | python3 maria-pablo/report.py

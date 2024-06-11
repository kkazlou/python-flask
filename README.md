# Python-flask
Basic REST API using Python and Flask

## Usage
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
## Example of requests
```
GET all items
curl http://127.0.0.1:5000/items

POST a new item
curl -X POST -H "Content-Type: application/json" -d '{"name":"Item1"}' http://127.0.0.1:5000/items

GET a specific item (replace <item_id> with the actual UUID)
curl http://127.0.0.1:5000/items/<item_id>

PUT to update an item
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Item1"}' http://127.0.0.1:5000/items/<item_id>

DELETE an item
curl -X DELETE http://127.0.0.1:5000/items/<item_id>
```

## References
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)

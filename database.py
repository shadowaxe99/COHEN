```python
import pymongo

class Database:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.db = None

    def connect(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client.get_database()

    def authenticate(self):
        self.db.authenticate(self.username, self.password)

    def insert_data(self, collection, data):
        self.db[collection].insert_one(data)

    def update_data(self, collection, query, data):
        self.db[collection].update_one(query, {"$set": data})

    def delete_data(self, collection, query):
        self.db[collection].delete_one(query)

    def find_data(self, collection, query):
        return self.db[collection].find(query)

    def close(self):
        self.client.close()
```

import unittest

import utility as util
from flask_app import create_test_app as create_app

# Dont Use PyCharm does not find tests
app = create_app()


class TestModelFlaskUnit(unittest.TestCase):

    client = app.test_client()

    def test_add_store_and_delete_again(self):
        util.log("test_add_store_and_delete_again")
        rv = TestModelFlaskUnit.client.post('/store/StoreToADD', json={'name': 'doesnotmatter'})
        '''
        {
            "id": ?,
            "name": "StoreToADD",
            "email": null,
            "type": null,
            "item_count": null
        }   
        '''
        rv_jason = rv.get_json()
        print("result as json: {}".format(rv_jason))  # 'A store with name \'StoreToADD\' already exists.'
        print(b"result: " + rv.data)
        assert b"\"name\": \"StoreToADD\"" in rv.data  # "name": "StoreToADD"

        rv = self.client.delete('/store/StoreToADD')
        print(b"result: " + rv.data)
        assert b"Store deleted" in rv.data




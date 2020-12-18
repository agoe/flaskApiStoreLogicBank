import unittest
import requests
import utility as util
#  "run wsgiapp.py to start the Api Server"


apiUrl = 'http://localhost:5000'

class TestModelFlaskUnit(unittest.TestCase):


    def test_add_store_and_delete_again(self):
        url = apiUrl+'/store/StoreToADD'
        util.log("test_add_store_and_delete_again")
        rv = requests.post(url, json={'name': 'doesnotmatter'})
        '''
        {
            "id": ?,
            "name": "StoreToADD",
            "email": null,
            "type": null,
            "item_count": null
        }   
        '''
       #  rv_jason = rv.json()
       #  print("result as json: {}".format(rv_jason))  # 'A store with name \'StoreToADD\' already exists.'
        print("result: " + rv.text)
        assert "\"name\": \"StoreToADD\"" in rv.text  # "name": "StoreToADD"

        rv = requests.delete(apiUrl+'/store/StoreToADD')
        print("result: " + rv.text)
        assert "Store deleted" in rv.text




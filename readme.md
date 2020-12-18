Use RI Branch for executing Parent Check Rules

copy env.example to .env and change to your environment

run test/run_teststore.py for plain sqlalchemy calls with LogicBank

test/test_model.py  unit tests plain sqlalchemy calls with LogicBank

test/test_model_flask.py unittest for flask and LogicBank rules via flask_client

test/test_model_flask_remote.py integration test for Remote flask and LogicBank rules 
    via Python Requests Api (Requires running wsgiapp Flask Api Server)


Start Flask api Server With Logic Rules via wsgiapp.py


Rules in logix/rules_bank.py:

 Rule.constraint(validate=StoreModel,
                    as_condition=lambda row: 'X' not in row.name,
                    error_msg="Store Names({row.name}) should not  contain X")
    Rule.count(StoreModel.item_count, as_count_of=ItemModel)
    Rule.parent_check(validate=ItemModel, error_msg="no parent", enable=True)
    
some rest calls:

create store
post http://localhost:5000/store/\<storename\>
json body {}

delete store
delete  http://localhost:5000/store/\<storename\>

list stores
get http://localhost:5000/stores

update item
put http://localhost:5000/item/\<itemname\>
json body{"price": 8.89, "store_id": 9999}
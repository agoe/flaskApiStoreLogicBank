from logic_bank.util import ConstraintException
#  just run as main

def read_all_stores():
    result = {'items': list(map(lambda s: s.json(), models.StoreModel.query.all()))}
    print(result)


def count_stores():
    result = models.StoreModel.query.count()
    print("Number of Stores: {} ".format(result))


def count_items_for_store(store_id: int):
    result = models.ItemModel.query.filter_by(store_id=store_id).count()
    print("Number of Items: {}  for Store {}".format(result, store_id))


def add_store_and_delete_again():
    store = models.StoreModel("StoreToAdd")
    store.save_to_db()
    print("added store: {}".format(store.json()))
    count_stores()
    store.delete_from_db()
    print("store  deleted")
    count_stores()


def add_store_with_x():
    store = models.StoreModel("StoreXYZ")
    try:
        store.save_to_db()
    except ConstraintException as e:
        print("expected exception: {} ".format(e))
        session = db.Session()
        session.rollback()
    else:
        print("Missing Constraint exception: 'NO x in Store Name'")


def add_store_and_item_and_delete_again():
    store = models.StoreModel("StoreToAdd")
    store.save_to_db()
    item1 = models.ItemModel('item1', 9.99, store.id)
    item2 = models.ItemModel('item2', 8.99, store.id)
    item1.save_to_db()
    item2.save_to_db()
    count_items_for_store(store.id)
    print("Item_Count from LogicRule: {}".format(store.item_count))
    item1.delete_from_db()
    item2.delete_from_db()
    count_items_for_store(store.id)
    print("Item_Count from LogicRule: {}".format(store.item_count))
    store.delete_from_db()


def add_item_no_parent():
    item1 = models.ItemModel('itemNoParent', 9.99, None)
    item1.save_to_db()


def add_item_nonexisting_parent():
    try:
        item1 = models.ItemModel('itemNoParent', 9.99, 4711)
        item1.save_to_db()
    except Exception as e:
        print("expected exception: {} ".format(e))
        session = db.Session()
        session.rollback()
        result = e
    else:
        print("Missing Constraint exception: 'no parent fro item'")


if __name__ == "__main__":
    import db
    import models
    # noinspection PyUnresolvedReferences
    import logic

#    add_item_no_parent()
    add_item_nonexisting_parent()
#
    read_all_stores()
    count_stores()
    add_store_and_delete_again()
    add_store_with_x()

    add_store_and_item_and_delete_again()
    db.Session.remove()


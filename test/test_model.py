# noinspection PyUnresolvedReferences
import db
import models
# noinspection PyUnresolvedReferences
import logic
#  import db, model, logic first or know what you are doing
from logic_bank.util import ConstraintException
import unittest


class TestModel(unittest.TestCase):

    def test_add_store_and_delete_again(self):
        orig = count_stores()
        expected = orig + 1
        store = models.StoreModel("StoreToAdd")
        store.save_to_db()
        result = count_stores()
        print("added store: {}".format(store.json()))
        self.assertEqual(result, expected)
        store.delete_from_db()
        result = count_stores()
        expected = orig
        self.assertEqual(result, expected)
        print("store  deleted")
        count_stores()

    def test_add_store_and_item_and_delete_again(self):
        store = models.StoreModel("StoreToAdd")
        store.save_to_db()
        item1 = models.ItemModel('item1', 9.99, store.id)
        item2 = models.ItemModel('item2', 8.99, store.id)
        item1.save_to_db()
        item2.save_to_db()
        result = count_items_for_store(store.id)
        expected = 2
        self.assertEqual(result, expected)
        self.assertEqual(store.item_count, expected)
        print("Item_Count from LogicRule: {}".format(store.item_count))
        item1.delete_from_db()
        item2.delete_from_db()
        result = count_items_for_store(store.id)
        expected = 0
        self.assertEqual(result, expected)
        self.assertEqual(store.item_count, expected)
        print("Item_Count from LogicRule: {}".format(store.item_count))
        store.delete_from_db()

    def test_add_store_and_item_and_delete_again_store_first(self):
        store = models.StoreModel("StoreToAddFkUnitTest")
        store.save_to_db()
        item1 = models.ItemModel('item1FkUnitTest', 9.98, store.id)
        item2 = models.ItemModel('item2FkUnitTest', 8.98, store.id)
        item1.save_to_db()
        item2.save_to_db()
        result = count_items_for_store(store.id)
        expected = 2
        self.assertEqual(result, expected)
        self.assertEqual(store.item_count, expected)
        print("ItemCount from LogicRule: {}".format(store.item_count))
        result: (Exception, None) = None
        try:
            store.delete_from_db()
        except ConstraintException as e:
            print("expected exception: {} ".format(e))
            session = db.Session()
            session.rollback()
            result = e
        else:
            print("Missing Constraint exception: 'Delete rejected - items has rows'")
        finally:
            count_items_for_store(store.id)
            item1.delete_from_db()
            item2.delete_from_db()
            count_items_for_store(store.id)
            store.delete_from_db()
            print("Finally Delete Store and Items in correct order")

        self.assertIsInstance(result, ConstraintException)


    def test_add_store_with_x_trigger_constraint(self):
        store = models.StoreModel("StoreXYZ")
        result: (Exception, None) = None
        try:
            store.save_to_db()
        except ConstraintException as e:
            print("expected exception: {} ".format(e))
            session = db.Session()
            session.rollback()
            result = e
        else:
            print("Missing Constraint exception: 'NO x in Store Name'")

        self.assertIsInstance(result, ConstraintException)


def count_stores() -> int:
    result: int = models.StoreModel.query.count()
    print("Number of Stores: {} ".format(result))
    return result


def count_items_for_store(store_id: int) -> int:
    result: int = models.ItemModel.query.filter_by(store_id=store_id).count()
    print("Number of Items: {}  for Store {}".format(result, store_id))
    return result

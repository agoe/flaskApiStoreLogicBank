from flask_restful import Resource

from logic_bank.util import ConstraintException
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except ConstraintException as err:
            return {"message": "Rule Error {}".format(err)}, 400
        except RuntimeError:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        else:
            return {'message': 'Store not found'}, 404




class StoreList(Resource):
    def get(self):
        return {'data': list(map(lambda x: x.json(), StoreModel.query.all())),
                'total': StoreModel.query.count()}
#       return list(map(lambda x: x.json(), StoreModel.query.all()))

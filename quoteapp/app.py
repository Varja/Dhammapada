import falcon
import dhammapada_api

api = application = falcon.API()
storage_path = '/home/ubuntu/workspace'

quote_collection = dhammapada_api.Collection(storage_path)
api.add_route('/quote/{name}', quote_collection)

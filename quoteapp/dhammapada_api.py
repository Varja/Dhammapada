import os
import falcon
import msgpack

storage_type = "file"

class Collection(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path
        
    def on_get_file(self, req, resp, name):
        filename = name + '.txt'
        quote_path = os.path.join(self.storage_path, filename)
        try:
            resp.stream = open(quote_path, 'rb')
        except IOError:
            raise falcon.HTTPNotFound()
        resp.stream_len = os.path.getsize(quote_path)
        
    def on_get_database(self, req, resp, name):
        test = 1

    def on_get(self, req, resp, name):
        if storage_type == "file":
            on_get_file(self, req, resp, name)
        elif storage_type == "database":
            on_get_database(self, req, resp, name)


    def on_post(self,req, resp, name):
        filename = name + ".txt"
        quote_path = os.path.join(self.storage_path, filename)
        
        with open(quote_path, 'wb') as quote_file:
            chunk = True
            while chunk:
                chunk = req.stream.read(4096)
                quote_file.write(chunk)
        resp.status = falcon.HTTP_201
        resp.location = '/quote/' + filename
        

import tornado.ioloop
import tornado.web
import tornado.websocket

class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)
    '''
    When the server receive a message, it is send to every client
    '''
    def on_message(self, message):
        [client.write_message(message) for client in self.connections]

    def on_close(self):
        self.connections.remove(self)

    def check_origin(self, origin):
        return True

def make_app():
    return tornado.web.Application([
        (r"/websocket", SimpleWebSocket)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

import os

from tornado import gen
import tornado.ioloop
import tornado.web


DEFAULT_PAUSE = 5


class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self, t=None):
        t = self._parse(t)
        yield gen.sleep(t)
        self.finish({"waited": t})

    @gen.coroutine
    def post(self, t=None):
        t = self._parse(t)
        yield gen.sleep(t)
        self.finish(self.request.body)

    @staticmethod
    def _parse(t):
        try:
            t = float(t)
        except:
            t = DEFAULT_PAUSE
        return t

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/(\S+)", MainHandler),
    ])

if __name__ == "__main__":
    port = os.getenv('PORT', 80)
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

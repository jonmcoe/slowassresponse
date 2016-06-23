import os
import time

import tornado.ioloop
import tornado.web


DEFAULT_PAUSE = 5


class MainHandler(tornado.web.RequestHandler):
    def get(self, t=None):
        self.finish({"waited": self._safe_sleep(t)})

    def post(self, t=None):
        self._safe_sleep(t)
        self.finish(self.request.body)

    def _safe_sleep(self, t):
        try:
            t = float(t)
        except:
            t = DEFAULT_PAUSE
        time.sleep(t)
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

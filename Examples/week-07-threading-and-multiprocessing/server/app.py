from itertools import count

i = count()

def app(environ, start_response):
  data = "Hello, World. %d\n" % i.next()
  start_response("200 OK", [
      ("Content-Type", "text/plain"),
      ("Content-Length", str(len(data)))
  ])
  return iter([data])

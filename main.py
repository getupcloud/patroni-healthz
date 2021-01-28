import os, sys
from bottle import route, run, HTTPError
import requests

@route('/healthz')
def healthz():
    res = requests.get(os.environ.get('PATRONI_URL'))
    if not res.ok:
      raise HTTPError(status=500, body='ERROR\n')
    return 'OK\n'

if 'PATRONI_URL' not in os.environ:
    print("Missing env PATRONI_URL")
    sys.exit(1)

run(host='0.0.0.0', port=8080)

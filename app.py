from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_port():
    return f"Running on {app.config['host']}:{app.config['port']}"

if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser(add_help=False)
  parser.add_argument('-p', default=5000, type=int)
  parser.add_argument('-h', default='0.0.0.0', type=str)
  args = parser.parse_args()
  port = args.p
  host = args.h
  app.config['port'] = port
  app.config['host'] = host
  app.run(host=host,port=port)

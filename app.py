from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_port():
    return "Running on port %s" % app.config['port']

if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('-p', default=5000, type=int)
  args = parser.parse_args()
  port = args.p
  app.config['port'] = port
  app.run(port=port)

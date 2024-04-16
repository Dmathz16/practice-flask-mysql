import flask


def request_input(name):
    return flask.request.form.get(name)

def request_args(name):
    return flask.request.args.get(name)

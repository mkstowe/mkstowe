"""mkstowe.com package initializer."""
import flask
from datetime import datetime
from gensim.models import Word2Vec
import csv

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (mkstowe/config.py)
app.config.from_object('mkstowe.config')

app.config.from_envvar('MKSTOWE_SETTINGS', silent=True)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.context_processor
def events_to_dict():
    event_dict = {}
    with open(app.config["STATIC_ROOT"]/'events.csv') as file:
        for line in csv.DictReader(file, fieldnames=["story", "event_idx", "text"], quotechar='"', delimiter=',',
                                   quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if line['story'] not in event_dict:
                event_dict[line['story']] = [line['text']]
            else:
                event_dict[line['story']].append(line['text'])

    return event_dict


app.config["VARIEGATA_MODEL"] = Word2Vec.load(str(app.config["VARIEGATA_ROOT"]/'model'/'variegata.model'))
app.config["VARIEGATA_EVENTS_LIST"] = events_to_dict()


import mkstowe.views  # noqa: E402  pylint: disable=wrong-import-position

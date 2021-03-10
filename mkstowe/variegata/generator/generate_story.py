import pathlib
import os
import random
# from gensim.models import Word2Vec
import mkstowe.variegata
import csv


def events_to_dict():
    event_dict = {}
    with open(mkstowe.app.config["STATIC_ROOT"]/'events.csv') as file:
        for line in csv.DictReader(file, fieldnames=["story", "event_idx", "text"], quotechar='"', delimiter=',',
                                   quoting=csv.QUOTE_ALL, skipinitialspace=True):
            if line['story'] not in event_dict:
                event_dict[line['story']] = [line['text']]
            else:
                event_dict[line['story']].append(line['text'])

    return event_dict


# model = Word2Vec.load(str(mkstowe.app.config["VARIEGATA_ROOT"] / 'model' / 'variegata.model'))
# events_dict = events_to_dict()


def generate_story(num_nodes):
    story_events = []
    # cur_node = str(random.choice(list(events_dict.keys()))) + "_0"
    # for i in range(num_nodes):
    #     cur_node = random.choice(model.most_similar(cur_node)[:10])[0]
    #     split_node = cur_node.split("_")
    #     story_events.append(events_dict[split_node[0]][int(split_node[1])])

    return story_events

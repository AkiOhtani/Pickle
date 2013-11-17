#! /usr/bin/python
# -*- coding: utf-8 -*-
import time
starttime = time.clock()

from numpy import *
import logging
import cPickle as pickle


with open('features.tab', 'r') as fp:
    data = {}
    feature_names = None

    for (n, line) in enumerate(fp):
        values = line.rstrip().split()

        # # shimdataをすべて取り終えたらループを抜ける
        # if count == 0:
            # break
        if n == 0:
            feature_names = values[1:]
            continue

        keyword = values[0]

        features = []
        for (n, value) in enumerate(values[1:]):
            if value == '-':
                features.append(0)
            else:
                features.append(value)

        data[keyword] = features

    with open('features.pickle', 'w') as f:
        pickle.dump(dict(data=data, feature_names=feature_names), f, protocol=2)

        # node = map(lambda x: 0 if x == '-' else int(x), line[1:])

        # if shimdata.has_key(keyword):

        #     features_.append(node)
        #     labels_.append(shimdata[keyword])
        #     feature_names_.append(keyword)
        #     count = count - 1


#---------------------------------#
# features = array(features_)
# labels = array(labels_)


# count = 0
# for feature in features:
# #    print '%.5f  %.5f'% (feature[3],feature[4])
# #    print '%s %.5f' % (feature_names_[count], feature[3]/feature[2])
#     print feature[3]
#     print feature[2]
#     count = count + 1

# time2 = time.clock()

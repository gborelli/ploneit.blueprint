# -*- coding: utf-8 -*-
import simplejson
from zope.interface import classProvides, implements

from collective.transmogrifier.interfaces import ISectionBlueprint, ISection


class JsonImport(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        file_ = open(options['filename'], 'r')
        self.reader = file_.read()

    def __iter__(self):
        for item in self.previous:
            yield item

        data = simplejson.loads(self.reader, encoding='utf-8')
        for json_data in data:
            yield json_data

# -*- coding: utf-8 -*-
import simplejson
# from datetime import datetime

from zope.interface import classProvides, implements

from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
# from collective.transmogrifier.utils import Expression


class JsonImport(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous

        # if options.get('keys_to_date'):
        #     self.keys_to_date = Expression(options['keys_to_date'],
        #                                    transmogrifier,
        #                                    name,
        #                                    options)(self) #bah
        # else:
        #     self.keys_to_date = ()

        file_ = open(options['filename'], 'r')
        self.reader = file_.read()

    def __iter__(self):
        for item in self.previous:
            yield item

        data = simplejson.loads(self.reader, encoding='utf-8')
        for json_data in data:
            # convertire in data ciò che mi serve
            # for k, v in json_data.iteritems():
            #     if v and k in self.keys_to_date:
            #         json_data[k] = datetime.strptime(v, "%Y/%m/%d %H:%M:%S").isoformat()
            yield json_data

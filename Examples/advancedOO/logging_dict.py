import collections
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Base():
    def __str__(self):
        return "\n".join(['%s : %s' % (key, self[key]) for key in self.keys()])


class LoggingDict(Base, dict):
    def __setitem__(self, key, value):
        logging.info('Setting %s to %s' % (key, value))
        super(LoggingDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        value = super(LoggingDict, self).__getitem__(key)
        logging.info('Getting %s (%s)' % (key, value))
        return value


class UpperCaseDict(Base, dict):
    def __setitem__(self, key, value):
        super(UpperCaseDict, self).__setitem__(key.upper(), value.upper())


class LoggingOrderedDict(UpperCaseDict, LoggingDict, collections.OrderedDict):
    pass

d = logging_dict = LoggingDict()
d = upper_case_dict = UpperCaseDict()
d = logging_ordered_dict = LoggingOrderedDict()

d['a_key'] = 'my_value'
d['b_key'] = 'my_value'
d['c_key'] = 'my_value'

print(d)

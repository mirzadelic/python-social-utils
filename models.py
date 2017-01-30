# -*- coding: utf-8 -*-


class Person(object):
    """ Model for person with attributes. """
    _error_msg = 'Data is not correct.'

    def __init__(self, **params):
        try:
            self.id = int(params['id'])
            self.firstName = str(params['firstName']) if params['firstName'] is not '' else None
            self.surname = str(params['surname']) if params['surname'] is not '' else None
            self.age = int(params['age']) if params['age'] is not '' else None
            gender = str(params['gender'])
            if gender not in ['male', 'female']:
                raise ValueError(self._error_msg)
            self.gender = gender
            self.friends = []
            for fid in params['friends'].split(','):
                self.friends.append(int(fid))
        except:
            raise ValueError(self._error_msg)

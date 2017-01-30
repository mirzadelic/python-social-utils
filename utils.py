# -*- coding: utf-8 -*-

from models import Person as PersonModel


class Person:

    def __init__(self):
        self.persons = []

    def load_data(self):
        """ Loading data from file. """
        file = open('data.txt', 'r')
        for line in file.read().splitlines():
            splitted = line.split(';')
            p = PersonModel(
                id=splitted[0],
                firstName=splitted[1],
                surname=splitted[2],
                age=splitted[3],
                gender=splitted[4],
                friends=splitted[5]
            )
            self.persons.append(p)
        print 'Loaded %d persons from file.' % len(self.persons)
        print '--------------------------'

    def get_person_by_id(self, id):
        """ Get person by id. """
        if type(id) == int:
            person = filter(lambda x: x.id == id, self.persons)
            return person[0] if len(person) == 1 else None
        else:
            print 'Parameted ID must be int.'

    def is_friend(self, id1, id2):
        """ Check if id1 and id2 are friends. """
        person1 = self.get_person_by_id(id=id1)
        if id2 in person1.friends:
            return True
        return False

    def shortest_distance(self, id1, id2):
        """ Getting list of ids for shortest distance. """
        person = self.get_person_by_id(id=id1)
        return self.shortest_full_path(person, id1, id2)

    def shortest_full_path(self, person, id1, id2, path=[]):
        path = path + [id1]
        if id1 == id2:
            path.pop(0)
            return path
        shortest_path = None
        for p in person.friends:
            if p not in path:
                new_person = self.get_person_by_id(id=p)
                new_path = self.shortest_full_path(new_person, p, id2, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path

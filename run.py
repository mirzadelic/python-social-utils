# -*- coding: utf-8 -*-

from utils import Person


person = Person()
person.load_data()

person1 = person.get_person_by_id(16)
person2 = person.get_person_by_id(20)
person3 = person.get_person_by_id(19)

is_friend1 = person.is_friend(16, 20)
is_friend2 = person.is_friend(16, 19)

print '%s(%d) and %s(%d) are firends: %s' % (
    person1.firstName, person1.id, person2.firstName, person2.id, is_friend1)
print '%s(%d) and %s(%d) are firends: %s' % (
    person1.firstName, person1.id, person3.firstName, person3.id, is_friend2)

sd1 = person.shortest_distance(16, 20)
sd2 = person.shortest_distance(16, 19)

print 'Shortest distance between %s(%d) and %s(%d): %s' % (
    person1.firstName, person1.id, person2.firstName, person2.id, sd1)
print 'Shortest distance between %s(%d) and %s(%d): %s' % (
    person1.firstName, person1.id, person3.firstName, person3.id, sd2)

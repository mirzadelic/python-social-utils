# social utils for python

Persons data are loaded from `data.txt` file.

### Methods of `Person` class
  - `get_person_by_id(id)` - get person by id
  - `is_friend(id1, id2)` - checks if persons with ids are friends
  - `shortest_distance(id1, id2)` - get shortest distance between two persons

### Run
```sh
python run.py
```

```sh
Daren(16) and Katy(20) are firends: True
Daren(16) and Catriona(19) are firends: False
Shortest distance between Daren(16) and Katy(20): [20]
Shortest distance between Daren(16) and Catriona(19): [20, 19]
```


# Python Containers
You may find Python documentation pages on [data structures](https://docs.python.org/2/tutorial/datastructures.html) and [collections](https://docs.python.org/2/library/collections.html) useful.

Containers are compound data types and are one of the key types of data structure in Python.

## Tuple
Tuples are an ordered sequence. Different types such as int, float and string can be all contained in one single tuple. Each element of a tuple can be accessed via an index. 

Tuples can be concatenated using `+` oeprator; tuples can also be sliced using regular array indexing. Tuples are immutable, meaning you cannot change the value of a given element of a tuple. Tuples can be nested, meaning the elements of a tuple can be tuples.

Assigning a tuple to a new tuple simply creates a reference alias of the original tuple.


### Named Tuple
Container `namedtuple` is a useful data type in Python where different types of objects can be stored together. As a subclass of `tuple`, it enables reference to elements through names. Elements of `namedtuple` are accessible through name, index and iterator. It can also be viewed as a class with only user-defined fields but no methods. In a sense, `namedtuple` is similar to `list` in R, as both can store different types of objects with names, but the difference is neither `namedtuple` field names nor values are mutable. Still, just like `tuple`, `namedtuple` can contain mutable fields, such as a `list` object.

Field names shall not be keywords such as `def`, `print`, `return` and shall not start with a digit or underscore. The constructor argument rename=True auto-corrects invalid field names.

Below is an example of defining a `namedtuple` container and creating an instance of it.

```python
from collections import namedtuple
Person = namedtuple('Person', ['name', 'dob', 'gender'])
person1 = Person('Nicholas','02/29/2018', 'M')
```

Since a `namedtuple` object is immutable, in order to update field value, one can use the member function `namedtuple._replace()`, which returns by value a new object. The argument can be either of format `<field_name>=<new_field_value>` or the unpacking operator `**` followed by a dictionary.

```python
# directly use a field name
person1 = person1.replace(name='Han')
	
# use an unpacked dictionary
args = {'name':'Han', 'dob'='01/01/2018'}
person1 = person1._replace(**args)
```

## List
Lists, like Tuples, are also an ordered sequence. Lists, unlike Tuples, are mutable. List concatenation can be achieved using `+` operator, `<list>.extend(args)`, whereas `<list>.append(args)` will add a single element `args` to the list. `del(<list>[0])` removes the 0th element in the list. `<str>.split(arg_delim)` splits a string into a list of substrings separated by the delimiter.

Assigning a list to a new list simply creates a reference alias of the original list.

```python
A = [1, 2, "hello"]
B = A # B is an alias of A
B = A[:] # B is an independent copy of A
```

## Dictionary
A dictionary has keys and values. The key is analogous to the index; they are like addresses but don't have to be integers, usually characters. The keys of a dictionary are immutable and unique. `<dict>.keys()` returns all keys, same for values.


### Counter
A `Counter` is a subclass of `dict`, where the value are integers (can be negative). When a key is not in a `Counter`, it has default value 0. Just like in `dict` a user can create an element through `myDict[<new_key>] = <new_value>`, one can assign arbitrary integer value to a given key through `myCounter[<key>] = <any_int>`.

A constructor of `Counter` takes iterable object, dictionary object, or keyword arguments. Notice that string is interpreted as a single iterable.

```python
cnt = Counter('knowledgeispower')
cnt1 = Counter({'fish': 4, 'chips': 20, 'thigh': 2, 'wings': 2})
cnt2 = Counter(fish=12, chips=10, thigh=3, wings=1, drumstick=6)
```

Some useful operations are given below. Notice that `Counter` is unordered, just like `dict`.

```python
# returns the most common keys
>>> cnt1.most_common(2)
[('chips', 20), ('fish', 4)]

# returns the sum of counts across two counters
>>> cnt1 + cnt12
Counter({'chips': 30, 'drumstick': 6, 'fish': 16, 'thigh': 5, 'wings': 3})

# returns the difference of counts across two counters
# only positive counts are kept, others are zero
>>> cnt1 - cnt12
Counter({'chips': 10, 'wings': 1})

# returns the larger count for each key
>>> cnt1 | cnt12
Counter({'chips': 20, 'drumstick': 6, 'fish': 12, 'thigh': 3, 'wings': 2})
```

### Ordered Dictionary
An `OrderedDict` is a subclass of `dict`, which keeps track of insertion order. Below is a direct excerpt from the documentation, which I find to be very concise and clear, so I make a direct quote instead of paraphrasing it.

Equality tests between OrderedDict objects are order-sensitive and are implemented as `list(od1.items())==list(od2.items())`. Equality tests between OrderedDict objects and other Mapping objects are order-insensitive like regular dictionaries. This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.

Below is an example of defining a `OrderedDict` container and creating an instance of it.

```python
>>> from collections import OrderedDict
>>> # unsorted dictionary
>>> myDict = {'Math': 146, 'English': 140, 'Chinese': 141, 'Physics': 82, 'Chemistry': 64}

>>> # OrderedDict sorted by key
>>> myDict = OrderedDict(sorted(myDict.items(), key=lambda t: t[0]))
>>> print myDict
OrderedDict([('Chemistry', 64), ('Chinese', 141), ('English', 140), ('Math', 146), ('Physics', 82)])

>>> # OrderedDict sorted by value
>>> myDict = OrderedDict(sorted(myDict.items(), key=lambda t: t[1]))
>>> print myDict
OrderedDict([('Chemistry', 64), ('Physics', 82), ('English', 140), ('Chinese', 141), ('Math', 146)])
```

Member function `OrderedDict.popitem()` deletes the last (or the first if argument last=False) element by reference and returns the item deleted.
```python
>>> myDict.popitem()
('Math', 146)

>>> myDict.popitem(last=False)
('Chemistry', 64)
```

## Set
Like lists and tuples, sets can take different data types. Sets are unordered and only have unique elements. Set definition uses `{}` with elements separate by comma.

`<set>.add()` and `<set>.remove()` are used to add and remove elements. Operator `&`, `<set1>.union(<set2>)` and `<set1>.issubset(<set2>)` are used for intersection, union and subset respectively.

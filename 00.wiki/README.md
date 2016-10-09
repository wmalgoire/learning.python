[ ] TO ADD TO TRELLO CARDS, OR CREATE A README HERE

### Objects

- Think of named references ('variables') as references to objects
- The gargbage collector reclaims unreachable objects (objects without references)
- ```id()``` returns the guid of the object
 - rarely used in production
- The ```is``` operator determines equality of **identity** (a is None, a is b, ...)
- The ```==``` test for value equivalence (ex: 2 lists containing the same items, but not necesseraly referencing the same object)

#### Everything is an ```object``` (modules, functions, ...)
- ```type```(variable|function|module|...) to get the type
- ```dir```(variable|function|module|...) to introspect and get attributes like __name__, __doc__ ...
- ```import``` and ```def``` keywords result in binding to named references, just like *variables*

### Types

- Dynamic typing
  - No compile check agains types in advance
- Strong typing
  - Types are not automatically coerced to match (ex: str(int))

### Scoping

- LEGB rule: four nested scopes
  - Local (function)
  - Enclosing
  - Global
  - *Built-ins*
- Use ```global``` inside a local scope to assign a global reference

### Functions

- Arguments are passed by object-reference
- Reference is lost if a function argument is rebound.
  - To change a mutable argument, replace it *contents*
- return also passes by object-reference
  - empty return will return ```None```
- arguments can be specified with defaults
  - evaluaated once, when ```def``` is executed

## List/Set/Dict comprhension syntax

### List comprehensions

- Syntaxic shortcut to creaate list from iterables (list, set, tuple...)
- General syntax
  ```[exp(item) for item in iterable]```
- Example
  ```python
  # using list comprehension
  [len(word) for word in words]
  >>> [3, 6, 5, 1, 10]

  # using for loop
  lengths = []
  for word in words:
    lengths.append(len(word))

  # another more complex example
  f = [len(str(factorial(x))) for x in range(20)]
  ```
### Set comprehensions

- Syntaxic shortcut to creaate set from iterables (list, set, tuple...)
- General syntax
  ```{exp(item) for item in iterable}```
  - Note that it Will remove duplicates as fir all set containers 
  - Note that the resulting ```set``` will not necesseraly stored in a meaninful order as for all set containers
- Example
  ```python
  f = {len(str(factorial(x))) for x in range(20)}
  ```
### Dictionary comprehensions

- Syntaxic shortcut to creaate dictinoaries from iterables (list, set, tuple...)
 - General syntax
  ```{key_expr:value:expr for item in iterable}```
 - Note that in case of duplicates later keys will overwrite earlier keys
- Example
  ```python
  words = ["hi", "hello", "foxtrot", "**hotel**"]
  f = {x[0] : x for x in words}
  {'h': '**hotel**', 'f': 'foxtrot' }
  ```

### Filtering predicates

- Works with list,set,dictionary comprehensions
- Example
  ```python
  def is_prime(x):
    if (x < 2):
      return False
    for i in range(2, sqrt(x)) + 1):
      if x % i == 0:
        return False
    return True

  # Stores all prime numbers up to 101 in a list, using list comprehension syntax + filtering predicate (if... syntax)
  [x for x in range(101) if is_prime(x)]
  ```

## Iterable and Iterator

- ```iterable``` objects can be passed to the built-in ```iter()``` function to get an ```iterator```
  - ```iterator = iter(iterable)```
- ```iterator``` objects can be passed to the built-in ```next()``` function to fetch the next item
  - ```item = fetch(iterator)```
- Example
  ```python
  iterable = ["Spring", "Summer"]
  iterator = iter(iterable)
  next(iterator)
  >>> 'Spring'
  next(iterator)
  >>> 'Summer'
  next(iterator)
  >>> StopIteration Exception
  ```
- Concrete Example
  ```python
  def first(iterable):
    iterator = iter(iterable)
    try:
      return next(iterator)
    except StopIteration
      raise ValueError("iterable is empty!")
  
  first(["1st", "2nd"])
  >>> "first"
  first(set())
  >>> ValueError: iterable is empty!
  ```
## Generators

- Specify **iterable sequences**
  - All generators are iterators
- **Lazily** evaluated
  - The next value in the seqyebce is computed on demand
- Can model **infinite sequences**
  - Such as data streams with no definite end
- Are composable into **pipelines**
  - For natural stream processing
- Use the ```yield``` keyword

### Simple example

```python
def gen123():
  yield 1
  yield 2
  yield 3

g = gen123()
next(g)
>>> 1
next(g)
>>> 2
next(g)
>>> 3
next(g)
>>> StopIteration exception

for v in gen123():
  print(v)

```

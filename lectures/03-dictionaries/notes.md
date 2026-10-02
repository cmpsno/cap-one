# 03 — Dictionaries / Hash Maps

## They do
- [x] BroCode: dictionaries video (Day 0)

# dictionary = a collaction of {key:value} pairs\
#              ordered and unchangeable, no dupes.

capitals = {"USA": "Washington D.C.", "india": "New Dehli", "China": "Beijing", "Russia": "Moscow"}

# print(dir(captials))
  return: class - values (attributes and methods)
# print(help(capitals))


# if (capitals.get("USA"))
#   print("That capital exists")
# else: 
#   print("that capital does not exist")

# capitals.update({"Germeny": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

*keys method*

# keys = capitals.keys()

print(keys)
  return: dict_keys['usa' - 'russia']

for key in capitals.keys():L
  print(key)
    return: usa, india, china, russia, 

*values method*

# values = captials.values()
for value in capitals.value():
  print(value)
    return: dc, new dehli, beijing, moscow

# items = capitals.items()
for keym value in capitals.items():
print(items)
  return: dict_items([()])

--- 
## We do
- rep 1: classify internships into good/mid/bad tiers
- rep 2: how many "good"? print only the good ones
- rep 3: move a company between tiers

## I do (unseen, solo)
- attempt:

## Stuck points
-

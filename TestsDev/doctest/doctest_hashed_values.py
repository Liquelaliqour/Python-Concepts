"""
There are cases where the unpredictable value cannot be ignored,
because that would make the test incomplete or inaccurate.
For example, simple tests quickly become more complex when dealing with data types whose string representations are inconsistent.
The string form of a dictionary, for example, may change based on the order the keys are added.
Because of hash randomization and key collision,
the internal key list order may be different for the dictionary each time the script runs.
Sets use the same hashing algorithm, and exhibit the same behavior.
"""

# doctest_hashed_values.py
keys = ['x', 'xx','xxx']

print('dict:', {l: len(l) for l in keys})
print('set :', set(keys))

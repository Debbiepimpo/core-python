def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("")==0, "Empty string"
assert count_upper_case("A")==0, "One upper case"
assert count_upper_case("a")==0, "one lower case"
assert count_upper_case("*&^%$")==0, "Special charaters"

print("All the test passed")


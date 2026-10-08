rates_dict = {
    'June'      : 6.55,
    'July'      : 6.56,
    'August'    : 5.29,
    'September' : 5.57,
    'October'   : 5.98
}

print(f'July: {rates_dict['July']}')

rates_dict['September'] = 5.79
print(rates_dict)

rates_dict['November'] = 6.25
print(rates_dict)

# Question 2d
# As they use the same syntax of dictionary[key]=value they both assign values to the dictionary, but
# because key elements need to be unique. When a value is assigned to a key that already exists, the key remains the same but
# the value is overridden. While when a new key that isn't present in the dictionaty is assigned a value both are added to the dictionary.
# So, since 'September' already existed in the dictionary so just the new value got assigned to it. 'November' was not present in the
# dictionary so both key and value were added instead of anything being overrrided.
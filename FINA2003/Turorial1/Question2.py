# year = '2026' # (Wrong Assignment) This variable should be assigned as a integer/number
# print('%s - Fearless and Focused' year) # Missing the % operator on the year variable as well as using the wrong type (%s should be %d)
# print('f{year} - Fearless and Focused') #  f at the start of the string should be outside the '' and not inside.
# print('{1} - Fearless and Focused'.Format(year)) # Format() is wrong, it should be format() and idexes start at 0 not 1

birthYear = 2003
print('%d - Loyalty over Love' %birthYear)
print(f'{birthYear} - Loyalty over Love')
print('{0} - Loyalty over Love'.format(birthYear))

print(str(birthYear) + ' - Loyalty over Love') # Using string concatenation needs all values to be strings for it to work as it can only concatentate strings together.

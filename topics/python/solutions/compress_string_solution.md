## Compress String Solution

1. Write a function that gets a string and compresses it
  - 'aaaabbccc' -> 'a4b2c3'
  - 'abbbc' -> 'a1b3c1'

```
def compress_str(mystr: str) -> str:

	result = ''

	if mystr:
		prevchar = mystr[0]
	else:
		return result

	count = 1
	for nextchar in mystr[1:]:
		if nextchar == prevchar:
			count += 1
		else:
			result += prevchar + str(count)
			count = 1
			prevchar = nextchar

	result += prevchar + str(count)
	return result
```


2. Write a function that decompresses a given string
  - 'a4b2c3' -> 'aaaabbccc'
  - 'a1b3c1' -> 'abbbc'

```
def decompress_str(mystr: str) -> str:
	result = ''
	for index in range(0, len(mystr), 2):
		result += mystr[index] * int(mystr[index + 1])
	return result
```

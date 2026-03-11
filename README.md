# Lab 4: File Input and Output

These series of labs will cover the ways of reading from and writing to files in Python as well as string manipulation using a variety of string methods. 

The goal is to learn how to manipulate strings, store data, process information, and generate output files. 

Below is a summary of what was covered in chapter 4.

#### File Operations in Python

Function/Method | Description | Example Usage
---|---|---
`open(filename, mode)` | Opens a file and returns a file object. | `file = open('data.txt', 'r')`
`.read()` | Reads the entire contents of a file as a string. | `content = file.read()`
`.readline()` | Reads one line from the file at a time. | `line = file.readline()`
`.readlines()` | Reads all lines into a list of strings. | `lines = file.readlines()`
`.write(string)` | Writes a string to the file. | `file.write("Hello, World!")`
`.close()` | Closes the file to free up system resources. | `file.close()`
`with open() as ...` | Best practice: automatically closes the file. | `with open('file.txt', 'r') as f:`

#### Common File Modes

Mode | Description
---|---
`'r'` | **Read** - Default value. Opens a file for reading, error if the file does not exist.
`'w'` | **Write** - Opens a file for writing, creates the file if it does not exist. **This will overwrite the existing content.**
`'a'` | **Append** - Opens a file for appending, creates the file if it does not exist. New data is added to the end.
`'r+'` | **Read/Write** - Opens a file for both reading and writing.


#### Useful String Methods for File Processing

When working with text from files, you will frequently need to clean, split, or analyze strings. Here are some essential string methods to master:

Method | Description | Example | Result
---|---|---|---
`.strip()` | Removes leading and trailing characters (whitespace by default). | `"  hello world\n".strip()` <br> `"Hello World!".strip("!")` | `"hello world"` <br> `"Hello World"`
`.split()` | Splits a string into a list of substrings based on whitespace by default. | `"apple,banana,grape".split(',')` | `['apple', 'banana', 'grape']`
`.join()` | Joins elements of a list into a single string using a specified separator. | `"-".join(['2024', '03', '11'])` | `"2024-03-11"`
`.replace(old, new)` | Replaces occurrences of a substring with another substring. | `"I like cats".replace("cats", "dogs")` | `"I like dogs"`
`.lower()` | Converts all characters in the string to lowercase. | `"Hello World".lower()` | `"hello world"`
`.upper()` | Converts all characters in the string to uppercase. | `"Hello World".upper()` | `"HELLO WORLD"`
`.startswith(prefix)` | Checks if the string starts with the specified prefix. | `"report.txt".startswith("report")` | `True`
`.endswith(suffix)` | Checks if the string ends with the specified suffix. | `"report.txt".endswith(".txt")` | `True`
`.find(sub)` | Returns the lowest index where the substring is found, or -1 if not found. | `"hello world".find("world")` | `6`
`.isalpha()` / `.isdigit()` | Checks if all characters in the string are alphabetic / digits. | `"123".isdigit()` / `"abc".isalpha()` | `True` / `True`

## Grading Criteria

Like the previous labs, I will grade for functionality, but documentation will also be key components of your grade. Good documentation helps explain your logic, especially when processing data.

Lab | Description | Comments/Documentation | Functionality | Total
---|---|---|---|---
Lab4a | Palindrome | 5pts | 5pts | 10pts
Lab4b | Decimal to Hexademical  | 4pts | 6pts | 10pts
Lab4c | Hexadecimal to Decimal | 4pts | 6pts | 10pts
Lab4d | Clean lyrics! | 10pts | 10pts | 20pts
Lab4e | The grade reporter | 10pts | 15pts | 25pts
Lab4f | D̵̖͂E̶̯͂̈́Ć̶̼͔̎Ò̵͉͆D̶͒̅͜͜Ë̷͈̟́ ̵̯̙̆͒T̶̛͈̉H̴̭̎E̵̥̞̍̕ ̴̢̈͜V̶̫͈̈O̶͕͋̔I̵̪͝͝ͅD̵̖͑ ̴̣̤̅—̴̥̮̆͆ ̵̬͑̔O̷̦͓̿P̵̧̙̑Ę̷͗͜R̵̨͓͝A̷̠͝͝Ṫ̶̳̦Î̵̠͔Ò̷̩̤͑N̶͚̝̽̕:̴͍̱̓̅ ̸̹̔M̸͚͒A̷̦͛Ṋ̷̾̄ ̶͚̳͌͋Ȉ̴̫̭N̵̮̥̋̒ ̴͍͚͒Ť̴̡̯̎Ḥ̴̛͛Ę̸̖̽ ̷̟̽M̷̧͌̅Í̸̡̬̊D̷̘̩̈̉D̸͉̍L̷̻̒̏Ȩ̴̗́| 10pts | 15 pts | 25pts
Total | | | | **100pts**
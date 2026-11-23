**Python --**



* **Input / output in python--**



&#x09;**Input--**

&#x09;	**\* input() eg:- a = input("Enter name")**

&#x09;	**\* By default, input take value as string**

&#x09;	**\* We need to convert value to int or float by using float(input()) eg:- a = int(input("Enter number: ")**

&#x09;	**\* split() is used for getting multiple values in single line. eg:-  a, c = input("Enter two words: ").split()**



&#x09;**Output--**

&#x09;	**\* Print() used for displaying output**

&#x09;	**\* 'f' keyword is used to display the value of a variable. eg:- a = 1 print(f "Value of a is  : {a}")**

&#x09;

&#x09;**File input/output--**

&#x09;	**\* use open() function to open file to read and write specific files (csv, parquet, JSON) eg:- with open (" file\_name", "mode") as temp**

&#x09;	**\* Mode means what we are doing with the opened file. following are the modes we use for file handling.**

&#x09;	**\* 'r' - to read file. eg:- file.read(), file.readline(), file.readlines()**

&#x09;	**\* 'w' - to write file. eg:- file.write("Text"), file.writelines(list)**

&#x09;	**\* 'a' - to append to end of existing file. eg**

&#x09;	**\* 'a+' - to append and read.**

&#x09;



* **Datatypes--**

&#x09;**\* int**

&#x09;**\* float**

&#x09;**\* bool**

&#x09;**\* string**

&#x09;**\* list**

&#x09;**\* dictionary**

&#x09;**\* tuple**





* **Functions--**



&#x09;**\* 'def' is the keyword to define function in python**

&#x09;

&#x09;\* **A common beginner habit is putting print() inside a function when you actually want return—which makes the output harder to reuse later in your code. Think of return as giving data back to your program, and print() as showing something to a human.**





* **Loops--**



&#x09;**\* for---**



&#x09;	**\* For loop is for running statements for specific time.**

&#x09;	**\* used to iterate over sequences such as lists, tuples, strings and ranges.**

&#x09;	**\* Ore velaya again and again antha sequence la irukura every item kum panrathuku use aagum for loop**



* **Conditions--**



&#x09;**\* if--**

&#x09;	**\* If statement is used to execute a block of code only when a specified condition evaluates to true.**

&#x09;	**\* Condtion correct ah iruntha athula irukura statement run aagum. Illa na next one check panni athu run aagum.**

&#x09;	**\* Ethuvume correct ah illa na else part run aagum**



&#x09;

**String Handling--**



&#x09;**\* lower() — Converts all uppercase characters to lowercase.  eg:- print(text.lower())**

&#x09;**\* upper() - Converts all lowercase characters to uppercase.  eg:- print(text.upper())**

&#x09;**\* capitalize() - converts first character of the word then keep rest in lowercase.  eg:-print(text.capitalize())**

&#x09;**\* replace(old, new) - replace the words with new words eg:- print(text.replace("Python", "Java", 1) # 1 is for replacing first occurrence only**

&#x09;**\* split(separator) - splits the string into list using separator (default separator is white space). eg:- print(text.split())**

&#x09;**\* join(iterable) — Joins elements of an iterable (such as a list of strings) using the calling string as a separator. eg:- print("-".join(words))**

&#x09;**\* find(substring) — Returns the index of the first occurrence of a substring, or -1 if not found. eg:- print(text.find("Python"))**

&#x09;**\* count(substring) — Counts how many times a substring appears in the string. eg:- print(text.count("apple"))**

&#x09;**\* strip() — Removes leading and trailing whitespace (or specified characters). eg:- print(text.strip())**

&#x09;**\* startswith() - check whether a string starts with specified index. eg:- print(text.startswith("En"))**



**Open/Read/write file--**



* **open() - used to open the file to read or write.** 

&#x09;	**eg:- with open("input.txt", "r") as f:** 

&#x09;		**content = f.read()**

&#x09;     	     **Print(content)**

&#x09;	**(or)**

&#x09;    **Absolute or relative path vazhiya open pannalaam** 



&#x09;**-> file open pannum pothu absolute path or relative path vazhiya open pannalaam. absolute path na open panna pora file oda path ah from root directory la irunthu apdiye kudukrathu. relative path na antha file entha folder la iruko athuku munnadi irukura folder ah relative nu kuduthu file ah open panrathu.**



&#x09;**-> else we can use pathlib for more professional and to work across different OS**



&#x09;	**eg:- from pathlib import Path**

&#x09;	     **file\_path = Path(\_\_file\_\_).parent / "input.txt"**



**read() -  used to read entire file as a string. eg:- content = f.read()**

&#x09;

&#x09;**-> to read file line by line, we can use for loop inside.**



&#x09;**eg:- for line in file:**



&#x09;**-> Line by line processing uses less memory, faster for larger files and it is a common in ETL pipelines.**



* **Write() - Used to write data into a file.**

&#x09;

&#x09;**eg:- file.write("Hello")**



&#x09;**-> open("file.txt", "w") is to write the data into a file. it will create the .txt file if the file is not exists. if exists, it will overwrite it.**

&#x09;











&#x09;

&#x09;



&#x09;


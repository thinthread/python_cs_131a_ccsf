# Comments are written with a hash-tag notation in front of a line of text or code 
#  eg.: # Your comment here or code here



''' Docstrigs '''  """ Docstrings """

''' docstrings - <function_name>.__doc__

If the first thing after the function header is a string (some tools insist that it must be a 
triple-quoted string), it is called a docstring and gets special treatment in Python and in some 
of the programming tools.

Another way to retrieve this information is to use the interactive interpreter, and enter the 
expression <function_name>.__doc__, which will retrieve the docstring for the function. So the string you write as documentation at the start of a function is retrievable by python tools at runtime. This is different from comments in your code, which are completely eliminated when the program is parsed.

By convention, Python programmers use docstrings for the key documentation of their functions.

'''
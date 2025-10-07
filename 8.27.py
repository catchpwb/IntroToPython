'''Develop a class Textfile that provides methods to analyze a text file. The class
Textfile will support a constructor that takes as input a file name (as a string) and instantiates a Textfile object associated with the corresponding text file. 
The Textfile class should support methods nchars(), nwords(), and nlines() that return the number
of characters, words, and lines, respectively, in the associated text file. The class should
also support methods read() and readlines() that return the content of the text file as a
string or as a list of lines, respectively, just as we would expect for file objects.
Finally, the class should support method grep() that takes a target string as input and
searches for lines in the text file that contain the target string. The method returns the lines
in the file containing the target string; in addition, the method should print the line number,
where line numbering starts with 0.
>>> t = Textfile('raven.txt') File: raven.txt
>>> t.nchars()
6299
>>> t.nwords()
1125
>>> t.nlines()
126
>>> print(t.read())
Once upon a midnight dreary, while I pondered weak and weary,
...
Shall be lifted - nevermore!
>>> t.grep('nevermore')
75: Of `Never-nevermore.`
89: She shall press, ah, nevermore!
124: Shall be lifted - nevermore!'''

class Textfile:

    def __init__(self, file):
        self.textFile = file
        'print(self.textFile.read())'
    
    def nchars(self):
        'returns number of characters'
        print(len(self.textFile))

    def nwords(self):
        'returns number of words'
        print(self.textFile.split())

    def nlines(self):
        'returns number of lines'
        print(self.textFile.count('\n'))

    def read(self):
        'returns contents as string'
        print(self.textFile)

    def readlines(self):
        'returns contents as a list of lines'
        print(self.textFile.split('\n'))

    def grep(self, target):
        """takes a target string as input and searches for lines in the text file that contain the target string. The method returns the lines
        in the file containing the target string; in addition, the method should print the line number, where line numbering starts with 0"""
        

'Open file'
file = open("raven.txt")
'Read file into class Textfile as a string'
t = Textfile(file.read())
t.nchars()
t.nwords()
t.nlines()
t.nwords
t.read()
t.readlines()
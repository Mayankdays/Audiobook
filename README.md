# Audiobook

So this is a Python code that anyone can use to make their own book reader rather than buying audible or any other audiobook software. It is simple and not that complicated to understand.

So, before we begin, to write this code download [Pycharm](https://www.jetbrains.com/pycharm/) because it is easy for setting up your python file and writing in it.

Now let's get to the topic.

## File creation

When we try to make a new project, We get a screen for our project settings. Set your interpreter to Virtualenv because it will help later. You can put the project in any folder you want and after you have completed the file setup click start. There we will come up to a screen called main.py. We will use that screen for writing the code. Also, follow whatever is given on the code so that you understand how to use Pycharm.

## Installation and Import of packages

Before we begin writing our code, we have to install 2 packages. First go to Terminal and write `pip install pyttsx3` which will convert the text to speech. Then write `pip install PyPDF2` in the terminal that will read the pdf you will give to read. After installing these 2 go to your coding area and import both of those packages:

`import pyttsx3`

`import PyPDF2`

After we write these 2 we should make their names simpler. write these next:

`speaker = pyttsx3.init()`

`pdfreader = PyPDF2.PdfFileReader()`

Now let's go to the next step.

## The Start-up Code

Now we get to the exciting part. First let's bring in the book we want to read. Download a PDF of the book and put the PDF in the folder you write this code. Make a variable called book and write this down:

`book = open(Your pdf, 'rb')`

Write this after the import codes and then simplify the names. Also, change `pdfreader` to:

`pdfReader = PyPDF2.PdfFileReader(book)`

This will say `pdfreader` to read the book.

Now the real fun begins...

## The Real Code

Now we will start with the real code. First let's go simple. Write this:

`speaker.say("Hello World")`

And then:

`speaker.runAndWait()`

Run this. You will hear the speaker saying Hello world. Pretty cool right? Next we will write some more stuff.

let's make a new variable called `pages`.

`pages = pdfreader.numPages`

This will read how many pages are there. Now check your PDF file to know how many pages there are. Then write this just below simplified plugins:

`print(pages)`

This will be used to check if the pdfreader can read the book. Now let's make pdfreader to get the text from each page and make speaker read them.

`text = pdfreader.extractText()`

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

`pdfreader = `

# How to make a Termm custom command (with explanation)

First of all, make sure you have created your file in 'customcmds', name it whatever you want.

Before we start, let me make some things clear:

1. DO NOT `import termm`, YOU WILL REGRET
2. We will be learning how to make a file viewer (some sort of 'cat')
3. Its easy

Okay so now with everything said, lets begin.

## The basics

So first of all, how does a custom command work?
In the main code, they are referred as modules, because they are imported to the main code just like a normal Python package, the only difference is that it is going to be executed via an entry point.

The entry point is the `main` function of your code. If you checked the [example.py](customcmds/example.py) file, or the [clear.py](customcmds/clear.py) file, you should have noted they all have the __main__ function, that takes as an argument 't' (t stands for Termm). The 't' argument is the globals at the main file, being transferred to your main function for you to use.

There is a function and a class you should know (there are more, check the [termm.py](termm.py) file for more):

The class `t["Command"]`, which is the equivalent to `termm.Command`. The class takes 4 properties you must define: `name`, `desc`, `onexec` and `man`.

`name` is the name of the command, obviously. `desc` is the description, `onexec` is the function that will be executed once the command is called, which must have one argument (the args for the command, which will be called as a list). `man` is the command manual (will be displayed with the 'man' command). You are supposed to give it a clear explanation of what your command does.

---

You also should be familiarized with the `t["registerCommand"]` function, which is the equivalent to `term.registerCommand`. It takes one argument, `cmd`, which should be of the `t["Command"]` class.

This function will append the command to the known commands table.

---

## Making the command

So, knowing all of that above, and that we are gonna do a command that reads a file, lets get to work.

First, make a file. My file is going to be labeled *"cat.py"*. Now, you need to open your favorite text editor, and open your file in it.

Lets first of all make the skeleton for our file:

```python
import os

def onExecution(args):
    pass

def main(t):
    pass
```

So, let me explain everything there.

First, we `import os`, to check if the file exists or not that the user will input as an argument, to avoid any errors.

Then we declare the `onExecution` function, which takes as an argument `args`. This function is going to be executed when our command is called.

After that, we have our entry point, that is the `main` function. Remember that from the basics section? It is going to get `t` as an argument.

Now, we will proceed to make the command class, in the `main` function.

```python
import os

def onExecution(args):
    pass

def main(t):
    command_name = "cat" # The name of our command
    command_desc = "Shows the content of a file" # The description of our command
    command_manual = "This command will list the contents of the specified file.\nUsage: cat <path to file>" # What our command does and how to use it.

    command_class = t["Command"](command_name, command_desc, onExecution, command_manual) # Our command class    
```

Now there you go! We have our command class made. We have defined variables for each property of our class, to make the code more organized. Next up, we need to implement functionality to our command.

Lets do that by extending our `OnExecution` function.

```python
import os

def onExecution(args):
    if len(args) == 0:
        print("Usage: cat <path>")
        return

    path = args[0]    
    if not os.path.exists(path) or os.path.isdir(path): # Check if file exists or if it is a folder
        print("This file doesn't exist!")
        return
    with open(path) as f: # Open file as 'f' variable
        print(f.read())

def main(t):
    command_name = "cat" # The name of our command
    command_desc = "Shows the content of a file" # The description of our command
    command_manual = "This command will list the contents of the specified file.\nUsage: cat <path to file>" # What our command does and how to use it.

    command_class = t["Command"](command_name, command_desc, onExecution, command_manual) # Our command class    
```

There you go! Now we have functionality to our code! But one thing is missing? Can you guess what? (Hint: Read "The Basics" part again)

The thing is... Registering our command, so we can execute it!

So, at our main function, as you should have guessed, insert the following line:

```python
    t["registerCommand"](command_class) # Register our command so we can execute it
```

Once you do that, its time to test our code to see if its working.

## Testing our command

So we just finished our code, now lets get to the testing.

So once your Termm is open, you should see:

```log
Termm v0.0.1 (Pre-Release)
Did you know 'ex' also quits Termm?
--------------------------------------------------------------------

Loaded in module ' cat '
Loaded in module ' clear '
Loaded in module ' example '
>
```

Did you see the first module that loaded? Thats our module! This means our module has been loaded, so now what about the command? Lets test that by listing the commands, then using man on our command if its there.

```log
Termm v0.0.1 (Pre-Release)
Did you know 'ex' also quits Termm?
--------------------------------------------------------------------

Loaded in module ' cat '
Loaded in module ' clear '
Loaded in module ' example '
>cmds
---------------------------------------------------------
                   Command | Description
exit | Quits Termm
man | Manual
cmds | List of commands
sys | Execute OS command
modules | List of modules
cat | Shows the content of a file
clear | Clear the screen
example | An example command

---------------------------------------------------------
>man cat
This command will list the contents of the specified file.
Usage: cat <path to file>
>
```

It is there! So our command got loaded in, but does the command work? Lets find out!

I am going to create a new file called *"test.txt"*, then im gonna use our command on this file. The file content are as follows: *Hello, beautiful world!*

```log
Termm v0.0.1 (Pre-Release)
Did you know 'ex' also quits Termm?
--------------------------------------------------------------------

Loaded in module ' cat '
Loaded in module ' clear '
Loaded in module ' example '
>cmds
---------------------------------------------------------
                   Command | Description
exit | Quits Termm
man | Manual
cmds | List of commands
sys | Execute OS command
modules | List of modules
cat | Shows the content of a file
clear | Clear the screen
example | An example command

---------------------------------------------------------
>man cat
This command will list the contents of the specified file.
Usage: cat <path to file>
>cat test.txt
Hello, beautiful world!
>
```

So, our command works, just as expected!

## Conclusion

So, we learned the basics of how to make a custom command in Termm, and of how simple it is. If you got into some sort of issue, please revise your code. If you found an issue in Termm, please feel free to file it in the [issues](https://github.com/GabrielWindy/Termm/issues) tab!

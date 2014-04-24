# Sublime Text 3 for Python Development

[Sublime Text 3](http://www.sublimetext.com/3) (ST3) is lightweight, cross-platform text editor known for its speed, ease of use, and strong community support. It's an incredible editor right out of the box, but the real power comes from the ability to enhance its functionality using Package Control. In this article, we'll look at how to setup Sublime Text for Python development, enhance the basic functionality with custom themes and packages, and use many of the commands, features, and keyword shortcuts that make ST3 so powerful.

> This tutorial assumes you're using a Mac and are comfortable with the terminal. If you're using Windows or Linux many of the commands will vary, but you should be able to use Google to find the answers quickly given the info in this tutorial.

## Setting up ST3

After downloading ST3 ... 

### Install the `subl` command line tool

Like the `mate` command for TextMate, Sublime Text includes a command line tool called [`subl`](http://www.sublimetext.com/docs/3/osx_command_line.html) that allows you to open a file from the command line. 

To enable this command, create a symbolic link to the subl binary:

```bash
$ ln -s "/Applications/Sublime Text 3.app/Contents/SharedSupport/bin/subl" ~/bin/subl
```

Ensure that the link works by opening Sublime:

```bash
$ subl
```

If that didn't work, you probably need to add */bin* to your path:

```bash
$ echo "export PATH=~/bin:$PATH" >> ~/.profile
```

If you are still having trouble, check out [this](http://stackoverflow.com/questions/16199581/opening-sublime-text-on-command-line-as-subl-on-mac-os?lq=1) article for help. Also, here are links for help on creating the symbolic links in [Windows](http://stackoverflow.com/questions/9440639/sublime-text-from-command-line-win7?rq=1) and [Linux](http://askubuntu.com/questions/273034/lauching-sublime-text-from-command-line).

Now you can open a file or directory by adding the path as an argument on the command line. 

For example:

```bash
# open the current directory
$ subl .

#open directory called tests
$ subl ~/Documents/test

# open a file called text.txt
$ subl test.txt
```

> If there are spaces in the path, you must surround the entire path in double quotes.

To view all the commands, open up the help file: 

```bash
$ subl --help`
```


2. Install Package Control
3. Create a Settings File

## Themes

## Packages

anacanda
djanro
gitgutter
git
requirements.txt

## Custom Commands

1. Close all windows except the active

## Using ST3

## Features

1. Split layouts: Have your tests on one side and your code on another
2. Chrome-like Tabs
3. Command Palette
4. File Switching
5. Goto Symbols
6. Multi-Edit
7. Code Snippets

## Keyboard Shortcuts


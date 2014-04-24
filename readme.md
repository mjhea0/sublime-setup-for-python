# Sublime Text 3 for Python Development

[Sublime Text 3](http://www.sublimetext.com/3) (ST3) is lightweight, cross-platform text editor known for its speed, ease of use, and strong community support. It's an incredible editor right out of the box, but the real power comes from the ability to enhance its functionality using Package Control. In this article, we'll look at how to setup Sublime Text for Python development, enhance the basic functionality with custom themes and packages, and use many of the commands, features, and keyword shortcuts that make ST3 so powerful.

> This tutorial assumes you're using a Mac and are comfortable with the terminal. If you're using Windows or Linux many of the commands will vary, but you should be able to use Google to find the answers quickly given the info in this tutorial.

## Setting up ST3

After downloading ST3 ...

### Install the `subl` command line tool

Like the `mate` command for TextMate, Sublime Text includes a command line tool called **[`subl`](http://www.sublimetext.com/docs/3/osx_command_line.html)** that allows you to open a file from the command line.

1. To enable this command, create a symbolic link to the subl binary:

  ```bash
  $ ln -s "/Applications/Sublime Text 3.app/Contents/SharedSupport/bin/subl" ~/bin/subl
  ```

2. Ensure that the link works by opening Sublime:

  ```bash
  $ subl
  ```

  If that didn't work, you probably need to add */bin* to your Path:.


  ```bash
  $ echo "export PATH=~/bin:$PATH" >> ~/.profile
  ```

  Then repeat step one.

  *If you are still having trouble, check out [this](http://stackoverflow.com/questions/16199581/opening-sublime-text-on-command-line-as-subl-on-mac-os?lq=1) article for help. Also, here are links for help on creating the symbolic links in [Windows](http://stackoverflow.com/questions/9440639/sublime-text-from-command-line-win7?rq=1) and [Linux](http://askubuntu.com/questions/273034/lauching-sublime-text-from-command-line).*

3. Now you can open a file or directory using the following commands:

  ```bash
  # open the current directory
  $ subl .

  # open a directory called tests
  $ subl ~/Documents/test

  # open a file called text.txt
  $ subl test.txt
  ```

  If there are spaces in the path, you must surround the entire path in double quotes:

  ```bash
  $ subl "~/Documents/test/my test file.txt"
  ```

  To view all the commands, open up the help file:

  ```bash
  $ subl --help`
  ```

### Install Package Control

To begin taking advantage of the various [packages](https://sublime.wbond.net/) for extending Sublime's functionality, you need to install the package manager called **Package Control** - which needs to be installed manually. Once installed, you can use Package Control to install/remove/upgrade all other ST3 packages.

1. To install copy the Python code for Sublime Text 3 found [here](https://sublime.wbond.net/installation#st3). Click **View > Show Console** to open the ST3 console. Paste the code into the console. Press **enter**. Reboot ST3.

2. You can now install packages by using the keyboard shortcut **cmd+shift+P**. Start typing **install** until *Package Control: Install Package* appears. Press **enter** and search for available packages.

3. Some other relevant commands are:

   - *List Packages* shows all your installed packages
   - *Remove Packages* removes a specific package
   - *Upgrade Package* upgrades a specific package
   - *Upgrade/Overwrite All Packages* upgrades all your installed packages

   Check out the official [documentation](https://sublime.wbond.net/docs/usage) to view more commands.

### Create a Settings File

You can fully configure Sublime Text using JSON-based settings files, making it easy to transfer, or synchronize, your customized settings to another system. Simply upload your settings files to Dropbox and load them from there to sync all your machines. First, we need to create our customized settings. It's best to create a base file for all enviornments as well as language-specific settings files.

1. To set up a base file click **Sublime Text > Preferences > Settings - User**. Add an empty array to the file and add your settings within the array, including a comma after each one but the last.

  For example:

  ```json
  {
      // base settings
      "auto_complete": false,
      "sublimelinter": false,
      "tab_size": 2,
      "word_wrap": true
  }

2. For language specific settings click **Sublime Text > Preferences > Settings - More > Syntax Specific - User**. Then save the file using the following format: *LANGUAGE.sublime-settings*. So, for Python-specific settings, save the file as *Python.sublime-settings*.

3. You can obviously configure your settings to your liking; however, I highly recommend starting with my [base](http://link.here) and [Python-specific](http://link.here) settings - then making changes as you see fit.

## Themes

ST3 also gives you the option to change the overall theme and color schemes to better suit your personality. Or, if you're not artistically inclined, you can download one of the various custom [themes](https://sublime.wbond.net/browse/labels/theme) designed by the Sublime community.

## Packages

anacanda
djanro
gitgutter
git
requirements.txt
VenvPy3.sublime-build

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


# Setting up Sublime Text 3 for Full Stack Python Development

[Sublime Text 3](http://www.sublimetext.com/3) (ST3) is lightweight, cross-platform text editor known for its speed, ease of use, and strong community support. It's an incredible editor right out of the box, but the real power comes from the ability to enhance its functionality using Package Control. In this article, we'll look at how to setup Sublime Text for full stack Python development, enhance the basic functionality with custom themes and packages, and use many of the commands, features, and keyword shortcuts that make ST3 so powerful.

> This tutorial assumes you're using a Mac and are comfortable with the terminal. If you're using Windows or Linux, many of the commands will vary, but you should be able to use Google to find the answers quickly given the info in this tutorial.

Before we start, let's address what I mean exactly by "full stack".

In today's world of HTML5 and mobile development, Javascript is literally everywhere. Python coupled with a framework such as Django or Flask is not enough. To really develop a website from end to end, you must be familiar with Javascript (and the many Javascript freameworks), REST APIs, responsive design, and of course HTML and CSS. Thus, we need a development environment to handle not only Python but front end technologies as well - which I am going to show you how to setup.

Let's get to it.

## Setting up Sublime Text 3

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

You can fully configure Sublime Text using JSON-based settings files, making it easy to transfer, or synchronize, your customized settings to another system. Simply upload your settings files to [Dropbox](https://github.com/miohtama/ztanesh/blob/master/zsh-scripts/bin/setup-sync-sublime-over-dropbox.sh) and load them from there to sync all your machines. First, we need to create our customized settings. It's best to create a base file for all enviornments as well as language-specific settings files.

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

### Themes

ST3 also gives you the option to change the overall theme to better suit your personality. Design your own. Or, if you're not artistically inclined, you can download one of the various custom [themes](https://sublime.wbond.net/browse/labels/theme) designed by the Sublime community through Package Control. Check out [ColorSublime](http://colorsublime.com/) to preview themes before installing them.

The ever popular [Soda Dark Theme](https://sublime.wbond.net/packages/Theme%20-%20Soda) and the minimal [Flatland](https://sublime.wbond.net/packages/Theme%20-%20Flatland) are two of my personal favorites.

After installing a theme, make sure to update your base settings:

```json
{
  "theme": "Flatland Dark.sublime-theme",
  "color_scheme": "Packages/Theme - Flatland/Flatland Dark.tmTheme"
}
```

### Packages

Besides the themes, I take advantage of the following packages to speed up my workflow.

#### SideBarEnhancements

**[SideBarEnhancements](https://sublime.wbond.net/packages/SideBarEnhancements)** extends the number of menu options in the sidebar, speeding up your overall workflow. Options such as "New file" and "Duplicate" are essential and should be part of ST3 out of the box - but they aren't. The "Delete" option alone makes it worth downloading. This feature simply sends files to the Trash, which may seem trivial but if you delete a file without it, it's very difficult recover unless you're using a version control system.

Download this now!

#### Anacanda

**[Anacanda](https://sublime.wbond.net/packages/Anaconda)** is the ultimate Python package; it adds a number of IDE-like features to ST3 including:

  - **Autocompletion** works by default, but there are a number of configuration [options](https://github.com/DamnWidget/anaconda#anaconda-autocompletion).
  - **Code linting** uses either PyLint or PyFlakes with pep8. I personally use a different liting package, so I disable linting altogether within the user-defined Anaconda settings file, *Anaconda.sublime-settings*.

    ```json
    {
        "anaconda_linting": false,
    }
    ```

  - **McCabe code complexity checker** runs the [McCabe complexity checker](http://en.wikipedia.org/wiki/Cyclomatic_complexity) tool within a specific file.
  - **Goto Definitions** finds and displays the definition of any variable, function, or class throughout your entire project.
  - **Find Usage** quickly searches where a variable, function, or class has been used in a specific file.
  - **Show Documentation**: shows the Docstring for functions or classes (if defined, of course)

  You can view all of the features [here](https://github.com/DamnWidget/anaconda). Or within the README file in ST3's Package Settings: **Sublime Text > Preferences > Package Settings > Anaconda > README**.

#### Djaneiro

**[Djaneiro](https://sublime.wbond.net/packages/Djaneiro)** supports Django templating and keyword highlighting and provides useful code snippets (tab completions) for Sublime Text. The snippet system is an incredible timesaver. You can create common Django blocks with only a few keystrokes for templates, models, forms, and views. Check out the official [documenatation](https://github.com/squ1b3r/Djaneiro) to see a list of snippets.

My personal favorites are for templating: `var` creates `{{ }}` and `tag` creates `{% %}`

#### requirementstxt

**[Requirementstxt](https://sublime.wbond.net/packages/requirementstxt)** provides autocompletion and syntax highlightlighting as well as a nice version management system for your *requirements.txt* files.

#### SublimeLinter

**[SublimeLinter](https://sublime.wbond.net/packages/SublimeLinter)** is a framework for ST3 linters. The package itself does not include any actual linters; those must be installed seperately via Package Control using the **SublimeLinter-[linter_name]** naming syntax. You can view official linters [here](https://github.com/SublimeLinter). There are also a number of third party linters, which can be viewed in Package Control.

For Python linting, I recommend using **[SublimeLinter-pyflakes](https://sublime.wbond.net/packages/SublimeLinter-pyflakes)** and **[SublimeLinter-pep8](https://sublime.wbond.net/packages/SublimeLinter-pep8)**.

I also use **[SublimeLinter-jshint](https://sublime.wbond.net/packages/SublimeLinter-jshint)**, **[SublimeLinter-csslint](https://sublime.wbond.net/packages/SublimeLinter-csslint)**, **[SublimeLinter-html-tidy](https://sublime.wbond.net/packages/SublimeLinter-html-tidy)**, and **[SublimeLinter-json](https://sublime.wbond.net/packages/SublimeLinter-json)**.

> Most of these linters have dependencies associated with them, so please read the installation instructions before installing.

You can customize each linter in the user-defined *SublimeLinter.sublime-settings* file. For example, I ignore the following pep8 erros and warnings:

```json
"pep8": {
    "@disable": false,
    "args": [],
    "excludes": [],
    "ignore": "E501,C0301,W0142,W0402,R0201,E1101,E1102,C0103,R0901,R0903,R0904,C1001,W0223,W0232,W0201,E1103,R0801,C0111",
    "max-line-length": 100,
    "select": ""
},
```

#### GitGutter

**[GitGutter](https://sublime.wbond.net/packages/GitGutter)** shows little icons in ST3's gutter area that indicate whether a line has been insereted, modified, or deleted since the last commit.

#### FTPSync

**[FTPSync](https://sublime.wbond.net/packages/FTPSync)** syncs your project with your remote files. Simply *open* the file to download it (if the remote file is newer than your local file) and upload it to your remote server with every *save*. Great way to keep your local and remotes in sync. You'll want to make sure to add at least one remote connection by clicking **Sublime Text > Preferences > Package Settings > FTPSync > Setup FTPSync**.

Sample settings:

```json
{
  'primary': {
    host: 'ftp.mywebsite.com',
    username: 'johnsmith',
    password: 'secretpassword',
    path: '/www/',

    upload_on_save: true,
    tls: true
  }
}
```

I personally set the password to `null` because I don't want it visible in that file. FTPSync just asks for my password after each save.

#### AdvancedNewFile

**[AdvancedNewFile](https://sublime.wbond.net/packages/AdvancedNewFile)** is used to create a new folder or file from within ST3 completely with key bindings:

*Simply bring up the AdvancedNewFile input through the appropriate key binding. Then, enter the path, along with the file name into the input field. Upon pressing enter, the file will be created. In addition, if the directories specified do not yet exists, they will also be created. ... By default, the path to the file being created will be filled shown in the status bar as you enter the path information.*

I replaced the normal "cmd+n" command to create a new file with AdvancedNewFile by adding the following code to the *Key Bindings - User* file (**Sublime Text > Preferences > Package Settings > AdvancedNewFile > Key Bindings - User**):

```json
[
  { "keys": ["cmd+n"], "command": "advanced_new_file_new"}
]
```

#### Emmet

**[Emmet](https://sublime.wbond.net/packages/Emmet)**, previously known as Zen Coding, uses simple abbreviations to generate HTML or CSS code snippets.

For example, if your type a bang, `!`, then press tab in an HTML file the HTML5 doctype and a few basic tags are generated:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

Check out the offical [documentation](http://docs.emmet.io/)** as well as this handy [cheat sheet](http://docs.emmet.io/cheat-sheet/) for more info.

#### Markdown Preview

**[Markdown Preview](https://sublime.wbond.net/packages/Markdown%20Preview)** is used for previewing and building markdown files.

To use, open the Package Manager then type **Markdown Preview** to show the available commands:

- Markdown Preview: Python Markdown: Preview in Browser
- Markdown Preview: Python Markdown: Export HTML in Sublime Text
- Markdown Preview: Python Markdown: Copy to Clipboard
- Markdown Preview: Github Flavored Markdown: Preview in Browser
- Markdown Preview: Github Flavored Markdown: Export HTML in Sublime Text
- Markdown Preview: Github Flavored Markdown: Copy to Clipboard
- Markdown Preview: Open Markdown Cheat sheet

Once converted, the output file is updated on each subsequent save.

### Custom Commands

1. Close all windows except the active

## Using Sublime Text 3

### Features

1. Split layouts: Have your tests on one side and your code on another
2. Chrome-like Tabs
3. Command Palette
4. File Switching
5. Goto Symbols
6. Multi-Edit
7. Code Snippets
8. Vim mode (perfect for pairing)
9. Saved history if you accidently close


### Keyboard Shortcuts

1. **Goto Anything ("cmd+p")**: is used for quickly finding and opening files. Just type in a part of a path and filename within a project and you can easily open that file. This is great for quickly opening files in large Django projects.
2. **Goto Line Number ("ctrl+g")**: takes you to specific line number in an active file.
3. **Goto Symbol ("cmd+r")**: lists all functions and classes within a file to make them easier to find. Simply start typing the one you want.
4. **Multi-Edit** is by far my favorite shortcut:
  - Select a word, press **"cmd+d"** to select the next same word, then press **ctrl+d** again to select the next same word...
  - Press **"cmd+click"** to create a cursor for editing every where you click

> For more shortcuts, take a look at [this](http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/reference/keyboard_shortcuts_osx.html) article.

## Additional Resources

1. Community-maintained documentation: [http://docs.sublimetext.info/en/latest/index.html](http://docs.sublimetext.info/en/latest/index.html)


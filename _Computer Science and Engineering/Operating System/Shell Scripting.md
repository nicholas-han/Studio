# Shell Scripting
A script is a list of commands that can be interpreted and run by a program called scripting language. Commands can be entered interactively at the command line, or listd line by line in a text file. Scripting languages are usually not compiled. They are interpreted at runtime. Scripts are generally slower to run than compiled languages, but they are also much easier and faster to develop. Scripts are widely used to automate processes, such as ETL jobs (extract, transform and load), file backups and archiving and general system administration tasks. You can use scripts for nearly any computational task, including application integration and plug-in and web application development.

A shell script is an executable text file in which the first line usually has the form of an interpreter directive, which is also known as a "shebang" directive and takes the form of `#!interpreter [optional-arg]`. Interpreter is an absolute path to an executable program, and the optional argument is a string representing a single argument. Shell scripts are scripts that invoke a shell program. For example, `#!/bin/sh` invokes the Bourne shell or other compatible shell program, from the bin directory. "Shebang" directives aren't limited to shell programs. For example, you could create a python script with the following directive `#!/bin/env python3`.


## Filters and Pipes
Filters are shell commands which take their input from standard input, normally the keyboard and return their output to standard output, which is normally the terminal. We can think of filters as a program that transforms input data into output data. There are many examples such as `wc`, `cat`, `more`, `head`, `sort`, `grep` and so on. The value of filters is that they can be chained together, which brings to the pipe command.

The pipe command, denoted by a vertical slash `|`, immensely extends the functionality of shells. It allows you to chain together sequences of filter commands. The output of command 1 becomes the input of command 2. Pipe is short for pipeline.

## Shell Variables
Shell variables are variables that are limited in scope to the shell in which they were created. Accordingly, shells cannot see each other's shell variables. You can invoke the `set` command to list all variables and their definitions that are visible to the current shell. To delete a variable, use `unset <variable name>`.

Shell variables offer a powerful way to store and later access or modify information such as numbers, character strings and other data structures by name.

```bash
$ firstname=Nicholas # NOTE: no space around the equal size
$ echo $firstname
Nicholas
```

Another way to create a shell variable is to use the `read` command.

``` bash
$ read lastname
$ Han
$ echo $lastname
$ Han
```

The command `read` is particularly useful in shell scripting. You can use it within a shell script to prompt users to input information, which is stored in a shell variable and available for use by the shell script while it's running.

## Environmental Variables
Environmental variables are just like shell variables, except that they have extended scope. They persist in any child processes spawned by the shell in which they originate. You can extend any shell variable to an environment variable by applying `export <variable name>`. To list all environment variables, use the `env` command.

## Features of Bash Shell
### Metacharacters
Metacharacters are special characters that have meaning to the shell. 

- `#`: The pound symbol is used to include comments that the shell ignores. 
- `;`: The semicolon is a metacharacter that separates commands typed on the same line.
- `*`: The asterisk represents any number of consecutive characters within a filename pattern. - `?`: The question mark acts as a single character version of the asterisk metacharacter.

### Quoting
- `\`: Quoting specifies whether the shell should interpret special characters as metacharacters or "escape" them.
- `""`: Double quotes interpret the text literally, except for any metacharacters, which will be interpreted according to their special meanings.
- `''`: Single quotes interpret everything literally

### I/O Redirection
I/O redirection refers to a set of features used for redirecting either the standard input, the keyboard or the standard output, the terminal.

- `>` is used to redirect the standard output of a command to a file. It also creates the file if it doesn't exist and overwrites its contents if it already exists.
- You can avoid overwriting by using `>>`, whicih appends output to existing content.
- The combination `2>` redirects an error message to a file.
- To append the error message, use `2>>`.
- `<` is a redirection that passes file contents as input to the standard input.

### Command Substitution
You can use command substitution to replace a command with its output. There are two equivalent notations `$(command)` and ``` `command` ```.

### Command Line Arguments
Command line arguments are arguments used by a program specified on the command line. In particular, they provide a way to pass arguments to a shell script, a program.

### Batch vs Concurrent Modes
Bash has two main modes of operation. Batch mode, which is the usual mode, runs commands sequentially; the syntax is two commands separate by semicolon `;`. In concurrent mode, commands run in parallel. The ampersand operator `&` is used in between two commands.

## Scheduling Jobs Using Cron
When you want to schedule certain jobs to run automatically at certain times, the cron utility on Linux and Unix-like oerating systems allow you to do it. Cron is the general name of the tool that runs scheduled jobs consisting of shell commands or shell scripts. Crond is the daemon or service that interprets "crontab files" every minute and submits the corresponding jobs to cron at scheduled times. A crontab, short for "cron table", is a file containing jobs and schedule data. Crontab is also the command that invokes at text editor that allows you to edit a crontab file.

`crontab -e` opens the default text editor. The job syntax is `m h dom mon dow command`; `dom` stands for "day of month" and `dow` for "day of week". All five positions must have either a numeric entry or an asterisk, which is a wildcard symbol that means "any".
# Linux Commands
A shell is a powerful user interface for Unix-like operating systems. It can interpret commands and run other programs. A shell, which enables access to files, utilities, and applications, is also an interactive language. A shell is also a scripting language. And it can also be used to automate tasks.

The default shell on Linux is usually Bash. Other shells include `sh` "Bourne shell", `ksh` "Korn shell", `tcsh` "TC shell", `zsh` "Z shell" and `fish`. Bash shell stands for "bourne again shell". To find out what the default is, enter "printenv SHELL" in the command line, and it returns the path to the default shell program. If the default shell is not bash, you can always switch to it simply by entering "bash" on the command line.

Common shell commands for getting information include

- `whoami` returns username
- `id` returns user ID and group IDs
- `uname` returns the operating system name
- `ps` (process status) displays running processes and their IDs
- `top` (table of processes) displays the task manager of running processes and resource usage including memory, CPU and IO
- `df` (disk free) shows information about mounted file systems
- `man` (manual) fetches the reference manual for shell command
- `date` prints today's date
- `ctrl+R` to search for a previously inputted command

Common shell commands for working with files include

- `cp` (copy) to copy a file
- 	`cp -r` to recursively copy files in a directory
- `mv` (move) to change the file name or path
- `rm` (remove) to remove a file
	- `rm -r` to recursively remove a folder
	- `rm -rf` to recursively remove a folder, forcing to
- `touch` to create an empty file or update file timestamp
	- `touch <existing file.txt>` will update the last-modified date time to the current time
- `chmod` (change mode) to change or modify file permissions (read, write and execute)
- `wc` (word count) to get count of lines, words and characters in file

Common shell commands for wrangling text files include

- `sort` sorts the lines of a file in alphabetic order and prints the sorted result to standard output
- `uniq` (unique) filters out repeated lines (only when they are consecutive)
- `grep` (global regular expression print) returns lines in file matching pattern
- `cut` extracts a section from each line
- `paste` merges lines from different files


Common shell commands for navigating and working with directories include

- `pwd` (print working directory) to print the current, or present, working directory
- `ls` (ls) to list the files and directories in the current directory
	- `ls -a`, `ls -l`, `ls <directory path>`
- `find` to find files matching a pattern in the current directory tree
- `mkdir` (make directory) to make a new directory
- `cd` (change directory) to change directory
- `rmdir` (remove directory) to remove an empty directory, and it guarantees that you will never accidentally delete any important files or directories
- `open` to open the file management GUI (such as Finder on MacOS)

Common shell commands for printing file and strings include

- `cat` (catenate) to print the entire contents of a file
- `more` to print file contents one page at a time (and press space bar to move to next page)
- `head` to print just the first 10 lines of a file
- `tail` to print the last 10 lines of a flie
- `echo` to print string or the value of a variable, which can be used for troubleshooting or scripting
	- `echo "My Project" > README.md` create a file named "README.md" with contents "My Project"

Common shell commands for networking applications include

- `hostname` prints the hostname
- `ping` sends ICMP (Internet Control Message Protocol) packages to URL and prints response
- `ifconfig` (interface configuration) displays or configures network interfaces on the system
- `curl` (client URL) displays the contents of a file located at a URL
- `wget` (web get) downloads a file from a URL

## Archiving and Compression
Archiving and compression are distinct processes, which are usually combined. Archiving is the process of storing information that you don't use regularly but want to preserve. An "archive file" is a collection of data files and directories that are stored as a single file. Archiving makes the collection more portable and serves as a backup in case of loss or corruption.

File compression, on the other hand, involves reducing the size of a file by taking advantage of redundancy in its information content. The main advantages of compression include preserving storage space, speeding up file transfers, and reducing bandwidth loads.

Zip first compresses the files and then bundles them, whereas tar bundles the files and then compresses it (optional).

Common shell commands for file compression and archiving applications include

- `tar` (tape archiver) to archive and extract a set of files
	- `tar -cf <tar ball.tar> <directory>`, where `c` stands for creating a new tar and `f` stands for file input (as opposed to standard input)
	- `tar -tf <tar ball.tar>` lists all the directories in this tar ball
	- `tar -xf <tar ball.tar> <destination directory>` de-archives the tar ball
- `zip` to compress a set of files
- `upzip` to extract files from a compressed or zipped archive

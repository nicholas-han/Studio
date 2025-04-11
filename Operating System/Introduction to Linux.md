# Introduction to Linux
## Operating Systems, Unix and Linux
An operating system is a software that manage computer hardware and resources and allows interaction with hardware. Unix is a family of operating systems. Some popular Unix-based operating systems include Oracle Solaris, FreeBSD, HP-UX, IBM AIX and Apple MacOS.

In the 1960s, the original Unix PS was created at AT&T Bell Labs. But it was first made for a specific hardware system, the PDP-7 computer. In the 1970s, the Unix OS was rewritten in C, distinguishing it from other systems and making it portable to many hardware architectures. In the late 1970s, UC Berkley developed Berkley Software Distribution (BSD), an add-on to Unix providing additional software and capabilities. The famous MacOS was later derived from BSD.

Linux is a family of Unix-like operating systems. However, when referring to Linux, people are usually talking about a specific distribution or flavor. Linux was originally developed as an effort to create a free, open-source Unix OS. Key Linux features include free and open-source, secure, multi-user, multitasking and portable.

In the 1980s, GNU was developed at MIT. GNU stands for "GNU's not Unix" and was made as a free, open-source set of the existing Unix system tools. In 1991, Linus Torvalds developed a free, open-source version of the Unix kernel called Linux. The kernel is the core component of an OS that enables components to communicate with the machine's hardware. In 1992, the potential of unifying GNU and te Linux kernel was realized as popular Linux operating systems began to appear. In 1996, a computer scientist named Larry Ewing created "Tux" the penguin, which was later adopted by Linus Torvalds as the official Linux mascot. Today, billions of Linux instances run on servers, seriving the modern web.

Today Linux is used on Andriod devices, super computers, data centers and cloud services, and PCs.


## Linux Distributions
A Linux distribution is a specific flavor of the Linux operating system. It's also referred to as a "distro". All Linux distributions must use the Linux kernel, which is the core component of the Linux OS that enables the system to properly use the computer's hardware.

Today, there are hundreds of Linux distros, each tailored for a specific audience or task. Each Linux distro includes a unique set of default utilities that are part of the operating system, such as commands and applications that come prepackaged with the distribution. Each distro has its own graphical user interface (GUI), a specific set of commands that you can use in a shell, a window for entering and receiving output from commands. Each distro also provides different levels of supporting, including community vs enterprise and long-term supporting (LTS) vs rolling release.

### Debian
First released in 1993, Debian is one of the earliest rooted distros. It's stable, reliable and fully open-source. It supports many computer architectures and hardware, and thus makes it highly regarded in the server space. Debian is also the largest community-run distro currently available.

### Ubuntu
Ubuntu is also an early rooted distro, with its first official release in 2004. Ubuntu is Debian-based, meaning that it's built on top of Debian and uses a lot of the same tools as the Debian OS. Ubuntu is developed and managed by Canonical and has three official editions, Ubuntu Desktop, Ubuntu Server and Ubuntu Core (for the Internet of Things).

### Red Hat
Red Hat Linux, like Debian, is a "core" Linux distro, meaning that it is not derived from another Linux distro. It's open-sourced and managed by Red Hat, an IBM subsidiary. Today, it ships as Red Hat Enterprise Linux (RHEL), an edition focused entirely on enterprise customers.

### Fedora
Fedora is a known as a stable operating system that supports many architectures. It's also very reliable and secure, offering unique firewall and security features. It's sponsored by Red Hat, and consequently Red Hat uses much of Fedora's code base.

### SUSE Enterprise
SUSE Linux Enterprise (SLE) is available in two editions,  Server (SLES) and Desktop (SLED). It supports many architectures such as ARM for Raspberry Pi and uses the SUSE Package Hub, which enables users to install packages that aren't officially part of SLE. It's mantained by the small German open-source software company, SUSE.

### Arch
The unique, do-it-yourself approach of Arch Linux allows users to customize every part of their system, making it highly configurable. It thus requires a strong understanding of Linux and system tools in order to use it effectively. Because Arch isn't focused on stability in the same way as other distros, it has easy access to the newest software, which has little guarantee of being completely stable.

## Linux Architecture
Linux architecture consists of five layers. The outmost layer is UI, which allows users to interact with the system using a keyboard or mouse. The application layer includes system daemons, shells, user apps, and tools used to perform tasks. The operating system layer is in charge of vital jobs for system stability such as job scheduling and keeping track of time. The next layer is kernel; all Linux operating systems are built on top of the Linux kernel, which performs the most vital lower-level jobs. The kernel is the core component of the operating system and is responsible for managing memory, processing and security. The kernel interacts with the hardware layer, which includes all the physical or electonic devices in the computer such as processors, mmemory modules, input devices and storage.

### User Interface
The UI allows users to perform tasks by controlling applications with the keyboard. Desktop versions of Linux include a GUI layer, which is similar to Windows.

### Applications
Applications are the software that enables a user to perform a task in a Linux system. Applications include system tools (such as compilers), programming langauges, shells (which are special applications that are often part of the operating system itself), and user apps.

### Operating System
The operating system controls the jobs and programs that are vital to system health and stability. Its functions also include, assigning software to users, detecting errors and implementing measures to prevent complete system failures, and performing file management.

### Kernel
In a Linux system, the operating system is built on top of the Linux kernel, which performs the most vital operations. The kernel is the lowest-level software in a Linux system and has complete control of the system. It starts as soon as your computer boots and remains in your computer's memory while the system is running. It also acts as a bridge betweew your apps and your machine hardware, enabling the two to communicate effectively using "system calls". The kernel has four key jobs, memory management, process management, managing device driver for proper hardware support, and assuring the system remains secure.

### Hardware
The final layer in the Linux system is the hardware, consisting of the physical or electronic devices that make up your computer. It includes, CPU (which is responsible for executing most calculations), RAM (which is a fast storage unit used to hold the temporary information your applications need to rurn), storage for data that needs to persist when your computer is powered off, screen, USB devices such as a keyboard, mouse and USB drive.

### Linux File System
The Linux file system is the collection of files on your machine. It includes the files needed to run the machine and applications as well as your own files containing your work. The top level of the file system is the root directory, symbolized by a forward slash (/). Below this is a tree-like structure of the directories and files in the system. And the file system assigns appropriate access rights to the directories and files.

The very top of the Linux file system is the root directory, which contains many other directories and files. One of the key directories is /bin, which contains user binary files. Binarry files contain the code your machine reads to run programs and execute commands. It's called "slash bin" to signify that it exists directly below the root directory. Other key directories include /usr, which contains user programs, /home, which is your personal working directory where you should store all your personal files, /boot, which contains your system boot files, the instructions vital for system startup, /media, which contains files related to temporary media such as CD or USB drives that are connected to the system. There are several other directories in the root directory as well. All the files and directories in a Linux system are organized into one of these designated folders, depending on the purpose of the file or directory.

## Linux Terminal
The Linux shell is an OS-level application that interprets commands. In early versions of Unix and Linux, the shell was the only way to interact with the operating system. Today, you can also use GUIs, but the shell remains a popular and flexible choice and an easy way to run script files. You can use shell commands to perform tasks such as moving and copying files, writing to and from files, extarcting and filtering data, and searching for data.

Some popular shell versions include Bash and Zsh. You interact with the Linux shell through a Linux terminal. A terminal is an application, or user interface, where you enter the commands you want to run and receive any output from those commands. 

Special paths:
- A single slash "/" at the beggining of a path refers to the home directory
- A tilda "~" refers to the user's home directory
- Two periods ".." refers to the parent of the current directory
- A single period "." refers to the current directory

Many commands located in the bin folder are also built into the shell, so you can run them from other locations as well (such as "./ls" in the "/bin" directory can simply be run as "ls" anywhere).

## Text Editors
You use text editors to write code in your Linux environment. They are grouped into two categories, command-line text editors and GUI-based text editors.

Command-line text editors include
- GNU nano, a small and friendly modeless text editor
- vi, a traditional command-line editor originally created for Unix
- vim, a powerful mode-based command-line editor based on vi

GUI-based text editors include
- gedit, the default editor from the GNOME environment
- emac, one of the oldest free, open-source project still under development (also has GUI version)

### Gedit
Gedit is a popular, modern text editor that comes preinstalled on most Linux distros. It's designed as a general-purpose text editor and in keeping with the philosophy of the GNOME project, it emphasizes simplicity and ease of use, with a clean and simple GUI. Gedit provides many features to enhance your text editing experience, including

- Integrated file browser
- Undo and redo
- Search and replace functions with support for regular expressions in the search string
- Extendability using plugins from the gedit-plugins package
- Syntax color codingg to help interpret and focus on different aspects of your code.

### GNU nano
GNU nano is a command-line text editor that provides

- Undo and redo
- Search and replace with support for regex
- Syntax highlighting
- Line indentation
- Line numbers
- Line-by-line scrolling
- Multiple buffers so as to work with many files simultaneously

### Vim
Vim is a traditional and very powerful command-line editor. It takes some time to get accustomed to how it works, but with some practice your fingers will develop muscle memory to accomplish all of your text editing tasks at speed.

Vim has two basic modes, insert and command. Press *i* to enter the insert mode and press *Esc* to exit the insert mode and switch to command mode.

```shell
vim # enter vim (command mode by default)
i # enter insert mode
u # undo
ctrl+R # redo
yy # copy one line
dd # cut one line
p # paste down
P # past up
v # 选取模式，选好按一次y或d进行复制或剪切
/ # search
n # next result
N # last result
:set
nu # show line number
gg # jump to top
G # jump to bottom
{ # jump to previous block
} # jump to next block
b # jump to previous word
w # jump to next word
$ # jump to the end of the line
0 # jump to the beginning of the line
q+<字母> # start recording
q # end recording
[数字]@q<字母> #自动重复操作[数字]次
:help tutor

ESC #swith from insert mode to command mode
:wq # save and quit
:q! # quit without saving

```

## Installing Software and Updates
Both software updates and software installation files for Linux operating systems are distributed in files known as packages. These packages are archive files containing the required components for either installing new software or updating existing software. You use package managers to manage the download and installation of packages. Different Linux distros provide different package managers, some are GUI-based and some are command-line tools.

Deb and RPM packages are used by package managers in Linux operating systems. They are distinct file types containing software or updates for different Linux operating systems. Files of type .deb are used for Debian-based distributions such as Debian, Ubuntu and Mint. And .rpm files are used for Red Hat based distributions such as CentOS/RHEL, Fedora and openSUSE. RPM stands for Red Hat Package Manager. Deb and RPM formats are equivalent, so the contents of the file can be used on other types of Linux OSs. If a package is only available in one format, you can convert it using an alien tool.

Benefits of package managers include 

- Automatically resolve dependencies between packages
- Notify you when updates are available
- GUI-based package managers can automatically check for updates on a regular basis
- Automatic or manual installation

GUI-based Linux distro package managers include PackageKit and Update Manager. Update Manager is a GUI tool for updating deb-based Linux systems. `apt` is a command-line tool for updating deb-based Linux systems. You use `sudo apt update` to find available packages for your distro. PackageKit is a GUI tool for updating RPM-based Linux systems. `yum` is a command-line tool for updating RPM-based systems; it stands for "Yellowdog Updater, Modified". Python package managers include pip and conda.
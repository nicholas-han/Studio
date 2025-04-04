# Introduction to Git and GitHub

## Version Control
**Distributed Version Control Systems (DVCS)** have become a critical tool in software development and a key enabler for social and collaborative coding. They are not only being used by software engineers and DevOps professionals but also by many other technology practitioners such as data scientists and engineers.

A version control system allows you to keep track of changes to your documents. This makes it easy for you to recover older versions of your document if you make a mistake, and it makes collaboration with others much easier. Version control systems are widely used for things involving code, but you can also version control images, documents and any number of file types.

While there are many distributed versioning systems, Git is amongst the most popular ones. And GitHub is a highly popular Git-based hosted version control platform.


## Git
Linux development in the early 2000's was managed under a free-to-use system known as BitKeeper. In 2005, BitKeeper changed to a for-fee system which was problematic for Linux developers for many reasons. Linus Torvalds led a team to develop a replacement source-version control system, in order for distribution of Linux kernels. The project ran in a short timeframe and the key characteristics were defined by a small group, including:

- Strong support for non-linear development: Linus patches were then arriving at a rate of 6.7 patches per second
- Distributed development: each developer can have a local copy of the full development history
- Compatibility with existing systems and protocols: this was necessary to acknowledge the diversity of the Linux community
- Efficient handling of large projects
- Cryptographic authentication of history: this makes certain that distributed systems all have identical code updates
- Pluggable merge strategies: many pathways of development can lead to complex integration decisions that might require explicit integration strategies

Git is a free and open-source software distributed under the GNU General Public License. Git is designed as a distributed version control system, primarily focusing on tracking source code during development. It contains elements to coordinate among programmers, track changes, and support non-linear workflows. It serves as a central point for collaboration with a particular focus on agile development methodologies. In a central version control system, every developer needs to checkout code from the central system and commit back to it. As Git is a distributed version control, each developer has a local copy of the full development history, and changes are copied from one such repository to another. Each developer can act as a hub.

When used correctly, the main branch should always correspond to the deployable code. Teams can continuously integrate changes that are ready to be released adn can simultaneously work on separate branches in between releases. Git also allows centralized administration of tasks with access-level controls.

Git isn't the only version control system out there, but the distributed aspect is one of the main reasons it's become one of the most common version control systems available.

## GitHub
You can use Git without a web interface by using your command line interface, but GitHub is one of the most popular web-hosted services for Git repositories. Others include GitLab, BitBucket and Beanstalk.

GitHub is an online hosting service for Git repositories. It is hosted by a subsidiary of Microsoft. GitHub offers free, professional and enterprise accounts. As of August 2019, GitHub had over 100 million repositories.

## GitLab
GitLab is a complete DevOps platform, delivered as a single application. GitLab provides access to Git repositories, controlled by source code management. GitLab enables developers to streamline testing and delivery with CI/CD.


## Git Workflow
### Repositories
The heart of a Git-based project is the repository. A repository is a data structure that contains application source code and related artifacts, including a README file describing the purpose of the project and a license to express the ways in which people can use your code

You can make your repository public, namely searchable and visible to everyone, or private, only available to people with accounts that have permissions to see it.

**A working directory** contains the files and subdirectories on your computer that are associated with a Git repository.

### Cloning
Cloning creates a copy of the project's code and its complete version history from the remote repository on your local computer. The connection established during cloning enables you to push code changes to the remote repository. You can also pull any changes from the remote repository to your local repository and update it.

As a developer, you might try multiple ways to code the feature. You may not want the changes to affect the main branch until the code is ready. A good practice is to create a branch from the main branch and then work on the newly created branch. 

### Branches
A branch in git is an isolated development space based on the main branch where you can make changes.

The main branch is definitive and stores the deployable version of your code. When you plan to change things, you create a new branch and give it a descriptive name. The new branch starts with an exact copy of the original branch. As you make changes, the branch you created holds the changed code.

### Staging and Committing
After developing the feature, the next step is to select the changed files and move them to a staging area. The staging area is a temporary storage space where you collect the selected files before asking git to save them in the local repository. You can now commit the files to the newly created branch. Committing files allows you to record the changes and ensure your new features become a part of the branch. When you commit files, including a commit message provides context for project members to understand the change.

The commit message should be meaningful and descriptive. Best practices of a commit message include not ending with a period, limiting it to 50 characters (you can use the extended description field for additional details), and always writing in an active voice.

### Pull Request
The next step is pushing the changes in the branch to the remote repository. Most often, the code is reviewed by a maintainer who is responsible for managing the repository before it is merged into the main branch in the remote repository.

To merge the branch, you create a pull request. It is a request to the maintainer to review and approve the proposed (committed) changes in the branch. GitHub automatically makes a pull request if you make a change on a branch that you don't own. After the maintainer merges the pull request, the changes in the branch will be reflected in the main branch. Similarly, if you have maintainer access, you will receive pull request from team members, and review and approve their requests. Since the log files are immutable, it's always possible to find the person who approved the merge of the change.

When the two streams of work are ready to merge, each branch's code is identified as a (feature) tip, and the two tips are merged into a third combined branch.

## Git Commands
- `git config --global user.email <your github email>` sets a global email configuration for git. This needs to be executed before doing a commit to authenticate the user's email ID.
- `git config --global user.name <your github username>` sets a global user name configuration for git. This needs to be executed before doing a commit to authenticate the user's username.
- `git init` sets up the necessary files and data structure for git to start managing your project's version control.
- `git clone` copies a repository from a remote source to your local machine.
	- `git clone <repository URL>`
	- `git clone <repository url> <myRepoName>` clones a repo and gives it a local name
- `git add` moves changes from the working directory to the staging area.
	- `git add <filename.txt>` adds a specific file
	- `git add .` adds all files that are new or changed in the current working directory
	- `git add -A` adds all changes in the entire working tree, from the root of the repository, regardless of where you are in the directory structure
- `git stash` archives changes
	- `git stash pop` recovers archived changes
- `git status` enables you to view the status of your working directory and the staged snapshot of your changes.
	- 	`git status -s` or `--short` shows a shorter status summary
- `git reset`: undoes the changes that you've made to the files in your working directory.
	- `git reset`
	- `git reset --hard HEAD` discards all changes made to the working directory and staging area and resets the repository to the last commit (HEAD)
- `git diff` shows changes between branches, commits, or commit and working tree.
	- `git diff` shows the difference between the working directory and the last commit
	- `git diff HEAD~1 HEAD` shows the difference between the last and second-to-the-last commits
	- `git diff <branch-1> <branch-2>` compares the specific branches
- `git commit` takes the staged snapshot of changes and saves them to the project.
- `git revert` reverts a commit by applying a new commit.
	- `git revert HEAD`
- `git log` enables you to review the commit history, e.g. to confirm a commit is recorded.
- `git branch` enables you to create a branch.
	- `git branch` lists branches
	- `git branch <new-branch>` creates a new branch
	- `git branch -d <branch-name>` deletes a branch (to delete a branch, first use `git checkout` and then run this command to delete the branch locally) 
- `git checkout` enables you to switch to between existing branches.
	- `git checkout main` switches your current branch to the main branch
- `git remote` lists the names of all remote repositories associated with your local repository.
- `git merge` lets you to put everything back together again and merge the feature branch with the main branch.
- `git push` uploads local repository content to a remote repository. Make sure you are on the branch that you want to push by running the `git checkout` command first, then push the branch to the remote repository.
	- `git push origin <branch-name>`
- `git pull` fetches changes from a remote repository and merges them into your local branch.
	- `git pull origin main`

<img src="Git Diagram.png" alt="Git Diagram" style="display: block; margin: 0 auto;">

## Forking and Cloning Repositories
Cloning generally refers to creating a copy of a repository on your local machine. Cloned copies can be kept in sync between the two locations.

Remote repositories are those stored elsewhere, on the internet, on your network, or even on your local computer. You can have several remote repositories, each of which is generally either read-only or read/write for you. Collaborating with others involves managing these remote repositories and involves push, pull and fetch operations to and from them when you need to share work.

Developers use the terms upstream and origin when talking about remote repos. Origin generally refers to your fork, and upstream refers to the original work. But these are merely the norms.

Forking allows you to modify or extend a project without affecting the original project. Frequently, this is used to take an existing project and make it the starting point for your new project. You can also use forking to submit back changes into the original repository. To keep a fork in sync with the original work from a local clone, first create a local clone of the project. To configure git to sync the fork, open a terminal and change to the directory containing the clone. Typing `git remote -v` gives you the remote repository. Typing `git remote add upstream <clone directory>`. Adding upstream adds the original repository as a new remote repository labelled upstream.

## Managing a GitHub Project
As mentioned above, GitHub is a popular platform for version control and project management. Managing GitHub projects enables effective collaboration and project organization. Multiple roles are involved in managing a project, a developer, an integrator and a repository administrator.

An integrator receives changes made by others, reviews and responds to pull requests, and publishes the result for others to use.

A repository administrator structures repository organization and interaction. They also manage communities, asset types, relationships, categories and attributes. A repository administrator sets up and maintains access to the repository for developers. They also configure the servers needed for accessing the web services and documentation, define email and index settings, and manage the look and feel of the application. Repository admins can use GitHub actions to automate software workflows including CI/CD.
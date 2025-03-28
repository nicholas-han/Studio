# Introduction to Software Development


## Pair Programming

Pair programming is an extension of teamwork where two developers work side-by-side at 
one computer. They can either be physically at the same computer or work virtually via video link or shared screens. The former is the preferred option, but virtual pair programming can also be productive.

Pair programming is a type of Agile development where two developers can plan and discuss 
their ideas continually as they create a solution, generally resulting in a better end product. There are various styles of pair programming.

### Driver/Navigator Style
Driver/navigator style is the most common style, where one developer is the driver, typing in the code, and the other is the navigator, reviewing the code as it’s written and giving directions where to go next. The navigator also keeps an eye on the bigger picture of the overall solution. When working in this way, it’s important to regularly swap roles to keep both of the pair engaged across the whole task. 

### Ping-Pong Style
Ping-pong style incorporates test-driven development. For each task, one developer writes a test and then the second developer writes code to pass that test. For each new task, they swap roles, so regularly changing who writes the test and who writes the implementation. The two developers work together at the end of each task refactoring the successful code to refine and improve it.

### Strong Style
Strong style pair programming is a good way for junior software engineers to learn from 
more experienced ones. The defining rule for this is that for an idea to go from your head to the computer, it must go through someone else’s hands. So the more experienced of the pair is the navigator and the driver learns from witnessing their implementation and thought processes. 

For this to work well, the driver shouldn’t challenge any ideas until the full implementation 
is complete so as not to interrupt the flow of ideas from the navigator. 

### Benefits of Pair Programming
Pair programming has many benefits. 

It’s a good way to share knowledge and skills from one developer to another or between the 
two and a great way for a new team member to get up to speed on a project. As well as enhancing the technical skills of the pair, it’s also a good way of building soft skills such as communication and problem solving. Having two sets of eyes on the code often results in fewer typos, logic errors, and bugs. And it enables code reviews to be done on the fly.

While this doesn’t replace formal code reviews, it does enable another layer of review. Having two people thinking about a problem can result in multiple initial ideas, but is likely to result in the optimal approach being chosen earlier in the process.

Although pair programming can take longer than individuals writing the same solutions, it’s likely to result in better code with less time spent reviewing, testing, and bug fixing. 

### Challenges of Pair Programming
There are also a few challenges to overcome. 

Working in a pair requires long periods of focus which can be exhausting for the two 
programmers. And personal or other work commitments can impact the pair schedule. Sometimes one of the pair can end up controlling the entire process, resulting in a more typist/programmer pairing which doesn’t benefit from any of the positives of pair programming.

At other times, individual personalities may not work well together. When multiple sets of pair programmers are present, their discussions can result in a noisy environment for the other workers in the room.

## Application Development Tools
A cloud application developer's workbench includes version control, libraries and frameworks.

### Version Control
When many developers are working on the same project, knowing what order changes were made, thereby creating a new version of the source code, becomes overridingly important. Version control systems keep track of what changes were made, when and by whom, and resolve any conflicts between changes. For developing your code, version control can be useful when you are the sole contributor on a project. Properly used, it can give you a way to revert to an older version of your code if something goes wrong, and give you some basic information about how the code developed over time. Version control functionality is generally tied to the storage system you are using, which is why a code repository is recommended, even for beginners.

Git and Github are extremely popular for source code storage and management. Git stores files in repositories where you can track changes, split code into different branches for more focused development, and then merge them back into the main body of code.

### Libraries
Libraries are collections of code, like standard programs and subroutines, that you can use within your code. For example, you may want to include a navigational feature. Like a carousel, a code library can supply you with the code for that so that you don't have to spend time and energy creating one from scratch. Being able to reuse code in this way makes developing your app much quicker and easier.

Multiple code libraries can be integrated into your existing project. As you discover a need for a specific function of feature, you can research an appropriate library. Code libraries are generally used to solve a specific problem or add a specific feature set.

Examples of code libraries are:

- jQuery is a JavaScript library that simplifies DOM manipulation
- Email-validator checks if email address is correctly constructed and valid
- Apache Commons Proper is a repository of reusable Java components

### Frameworks
Frameworks provide a standard way to build and deploy applications. A framework is like a skeleton that can be extended by adding your own code, providing a scaffold on which to build your apps. The framework you intend to use must be determined early in your development planning and used right from the beginning. New frameworks can't be incorporated into an existing project. Your chosen framework dictates the architecture of your program and controls the program flow.

When working with a framework, there is a specific structure that you must follow. The framework calls on your code, rather than you calling on the framework. Frameworks are less flexible than libraries, allowing you less control, but they provide good standardization and can help you create efficient code.

Example of frameworks are:

- AngularJS is a JavaScript-based framework for dynamic web applications
- Vue.js is a JavaScript framework focused on the user interface
- Django is a framework that uses Python for web development

Frameworks define the workflow that you must follow, unlike libraries, which allow you to call functions as and when required. When using a framework, it can sometimes feel like you, as a developer, are not in full control of the development process. This sense of the framework and its predefined workflow controlling the development process is referred to as inversion of control. Frameworks that have a lot of control are known as opinionated; that is, they have opinions on how their workflow should be used and remove a lot of the decisions you would otherwise have to make about how code is written, the location of files and even file names. Frameworks often include their own libraries. Inversion of control allows you to create standardized apps, and takes away a lot of the tedious configuration work, so you can focus on the code for your app.

### CI/CD 
CI/CD refers to the practices of continuous integration and continuous delivery/deployment. CI/CD is a best practice for DevOps teams enabling developers to deliver frequent changes reliably. Implemented through a build-automation server, continuous integraion ensures that all the code components work together smoothly. A CI build environment enables you to integrate newly developed code frequently, at least every day, if not every hour, depending on how quickly the project changes. Continuous delivery begins where CI ends. The CI process automatically builds and tests your code, and then CD deploys all code changes in a build to a testing or staging environment.

### Build Tools
A build tool transforms your source code into the binaries needed for installation. Build tools organize your source code, set complile flags, and manage dependencies. They are most important in environments where there are many inter-connected projects, with multiple developers contriburting to each project. In these environments, it can be very difficult to keep track of what changes were made, in what order, what dependencies exist, and what needs to be incorporated in the next build, so automation is key to keeping everything running smoothly.

Build automation can automate a wide variety of tasks that developers do in their day-to-day activities, such as downloading dependencies, compiling source code into binary code, packaging binary code, running tests, and deploying to production systems.

You can initiate a build from the command line or from an IDE. There are two categories of build tools widely in use:

- Build-automation utilities, which generate build artifacts like executables, by compiling and linking source code.
- Build-automation servers, which execute build-automation utilities on a scheduled or triggered basis.

Examples of build tools are:

- Webpack is a module bundler for JavaScript
- Babel is a JavaScript compiler
- Web Assembly is a binary instruction format that runs in your browser

### Packages
Now that you have your app developed and tested, you are ready to deploy. The app needs to be simple and trouble-free for the user to install, so a commonly used techniqe is to collect all the necessary files and bundle them together into a package. Packages are archive files that contain the app files, instructions for installation, and any metadata that you choose. They have their own metadata too, including the package description, package version and any dependencies like other packages that need to be installed beforehand.

### Package Managers
Once you have bundled your app into a package, you can use a package manager to distribute it. Package managers take care of the tasks of finding, installing, maitaining or uninstalling software packages at the user's request. Package management systems coordinate with file archivers to extract package archives. They also verify checksums and digital certificates to ensure the integrity and authenticity of the package. They can locate, download, install or update existing software from a software repository, and manage dependencies to ensure a package is installed with all packages it requires.

Some commonly used package managers for the major platforms are:

- Linux
	- Debian Package Management System (DPKG)
	- Red Hat Package Manager (RPM)
- Windows
	- Chocolatey
- Andriod
	- Package Manager
- MacOS
	- Homebrew
	- MacPorts

Any libraries or utility code that is developed as part of the application is managed with the cloud application package managers. Examples of package managers for popular languages are:

- npm for Node.js/JavaScript
- Gradle and Maven for Java
- RubyGems for Ruby
- pip and conda for Python

## Software Stacks
A software stack is a combination of technologies that includes software and programming languages. Developers use a software stack to create applications and solutions such as web and mobile apps. The set of individual technologies is stacked in a hierarchy and work together to support the execution of an application. The higher levels in the stack provide tasks or services for the user, and the lower levels interact with the computer hardware.

Software stacks typically include front-end technologies such as programming languages, frameworks and user interface tools, and back-end technologies such as programming languages, frameworks, web servers, app servers, operating systems, messaging applications and databases.

The term technology stack may be used in place of software stack. However, a technology stack is a broader term that includes hardware and infrastructure like virtual machines, containers, storage and load balancers, as well as the software stack.

The simplest implementation of a software stack consists of a presentation layer, a business logic layer and a data layer. However, more complex applications use more complex stacks, which could include software for visualization, scheduling and orchestration, runtime environments, database connectivity, networking and security. The software and services that make up a stack can be from a variety of sources, from internal resources to third party providers and cloud providers. There is no formal definition of the structure of a stack, with the only rule being that the software and services included must support an application's development, functionality or deployment.

Examples of software stacks are:

- Python-Django stack uses the popular Python programming language alongside the Django web framework. This combination is all open source and commonly used for large-scale, fast-changing web applications.
- Ruby on Rails uses the Ruby programming language with a server-side web application framework. It is great with JSON or XML for data transfer and HTML, CSS and JavaScript for front-end development.
- ASP.NET stack includes Microsoft technologies such as the ASP.NET MVC framework, the IIS web server, SQL server and Azure.
- LAMP
- MEAN
- MEVN
- MERN

### LAMP Stack
The LAMP stack runs on the Linux operating system. It uses the Apache HTTP or web server, MySQL databases and the PHP programming language. LAMP is an example of an early incarrnation of a software stack designed for building websites and cloud applications. All its constituent parts are open source and loosely coupled, so it's easy to swap different options into the stack. For example, you could choose to use PostgreSQL instead of MySQL for your database server, changing the LAMP stack to be the LAPP stack. Similarly, you could use the Python programming language instead of PHP.

### MEAN Stack
The MEAN stack uses a MongoDB database with an Express.js web application server framework, the Angular.js framework for front-end JavaScript development, and the Node.js platform for server-side scripting. The MEAN software and services are platform agnostic, free and open source. There are other stacks related to the MEAN stack, including;

- MERN stack, which replaces Angular.js with React, and is a flexible and high-performing framework for developing front-ends.
- MEVN stack, which replaces Angular.js with Vue.js, where Vue is a lighter-weight JavaScript framework with less capabilities, but it can provide better performance than Angular.js.

### Comparison of MEAN, MEVN and LAMP

- MEAN
	- All parts use JavaScrippt, so developers only need to know a single language.
	- There is a lot of documentation and reusable code for developers.
	- However, it may not be well-suited for large-scale applications or relational data.
- MEVN
	- Similar to MEAN but is a much newer technology and doesn't have as many reusable libraries.
- LAMP
	- LAMP is one of the oldest software stack, so it's easy to find support and reusable solutions.
	- However, because Linux is an integral part of the stack, it's only available on Linux and thus less flexible.
	- Not suitable for non-relational data
	- Another disadvantage is that the back-end runs on PHP, Perl or Python, wherease the front-end uses JavaScript and HTML, making it harder for developers to switch back and forth.
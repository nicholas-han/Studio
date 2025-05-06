# Introduction to Cloud Computing
## Overview of Cloud Computing
Cloud computing is a business model or service that combines technology like virtualization with a few of the latest trends and if you require extra bandwidth, a Cloud-based service can address that need promptly, rather than waiting for a complex and costly update to your IT infrastructure. Users can customize their applications using Cloud services from anywhere if they have an Internet connection. In addition, Cloud computing enables efficient marketing of applications regardless of maintenance and cost.

### History of Cloud Computing
Cloud computing is an evolution of technology over time. The concept of cloud computing dates to the 1950s when large-scale mainframes with high-volume processing power became available. The practice of time sharing (or resource pooling) evolved to make efficient use of the computing power of mainframes. Using dumb terminals, whose sole purpose was facilitating access to the mainframes, multiple users could access the same data storage layer and CPU power from any terminal.

In the 1970s, with the release of an operating system called Virtual Machine (VM), it became possible for mainframes to have multiple virtual systems, or virtual machines, on a single physical node. The virtual machine operating system evolved from the 1950s application of shared access of a mainframe. By allowing multiple distinct computing environments to exist on the same physical hardware. Each virtual machine hosted guest operating systems that behaved like they had their own memory, CPU, and hard drives, even though these were shared resources. Virtualization thus became a technological driver and a massive catalyst for some of the most significant evolutions in communications and computing. Even 20 years ago, physical hardware was quite expensive.

With the internet becoming more accessible, and the need to make hardware costs more viable, servers were virtualized into shared hosting environments, virtual private servers, and virtual dedicated servers, using the same functionality the virtual machine operating system provided. So, for example, if a company needed an ‘x’ number of physical systems to run their applications, they could split one physical node into multiple virtual systems.

A hypervisor is a small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources. A hypervisor also separates the Virtual Machines logically, assigning each slice of the underlying computing power, memory, and storage, preventing the virtual machines from interfering with each other. So if, for example, one operating system suffers a crash or a security compromise, the others can keep working. As technologies and hypervisors improved and could share and deliver resources reliably, some companies decided to make the cloud’s benefits accessible to users. These users did not have an abundance of physical servers to create their cloud computing infrastructure. Since the servers were already online, spinning up a new instance was instantaneous. Users could now order cloud resources from a larger pool of available resources and pay for them on a per-use basis, also known as pay-as-you-go or utility computing model. This model became one of the key drivers behind cloud computing's launching. The pay-per-use model allowed companies and even individual developers to pay for the computing resources as and when they used them, just like units of electricity. This allowed them to switch to a more cash-flow friendly OpEx model from a CapEx model. This model appealed to all sizes of companies, those who had little or no hardware, and even those that had lots of hardware, because now, instead of making substantial capital expenditures in hardware, they could pay for compute resources as and when needed. It also allowed them to scale their workloads during usage peaks, and scale down when usage subsided. And this gave rise to modern-day cloud computing.

### Definition of Cloud Computing
The US National Institute of Standards and Technology (NIST) defines Cloud computing as a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or service provider interaction. Examples of computing resources include networks, servers, storage, applications, and services. This Cloud model is composed of five essential characteristics, four deployment models and three service models.

### Five Essential Characteristics
The five essential characteristics of the Cloud are on-demand self service, broad network access, resource pooling, rapid elasticity, and measured service.

- **On-demand self-service** means you can access Cloud resources whenever required. Services are always available on all days of the year. There are no exceptions other than when services are unable due to an outage or security breach.
- **Broad network access** means that Cloud computing resources can be accessed through the network. Public Cloud services could generally be accessible from anywhere and on any device with Internet connectivity and browser capabilities. Internet access is mandatory for accessing public Cloud services.
- With **resource pooling**, consumers save on costs when using a shared model, which provides Cloud providers economies of scale, making the Cloud cost efficient. Computing resources are pulled to serve multiple consumers using a multi-tenant model, Cloud resources are dynamically assigned and reassigned according to demand without customers needing to concern themselves with the physical location of these resources.
- **Rapid elasticity** implies that you can increase or decrease resources as per your demand. Because of the elastic property of the Cloud, resources can be scaled up or down vertically scaling or scaled out as in horizontal scaling.
- **Measured service** means that you only pay for what you use or reserve as you go. Measured service is also termed as **a utility model of billing**, where you are charged after the usage and at the end of the predefined period, like monthly electric charges.

## Cloud Computing Service Models
### Overview
Three service models available on the cloud: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).

IaaS is a set of compute networking and storage resources that have been virtualized by a vendor so that a user can access and configure them any way they want. The user of IaaS is usually a system admin or an IT admin.

Software as a Service is just software that you don't have to install on your machine and you don't have to manually update. So the user for Software as a Service could be anyone. It's usually charged on a subscription model, rather than a one-time license fee.

PaaS takes advantage of all the virtualized resources from Iaas and then just abstracts them away, so the user doesn't have to worry about managing any of those virtualized resources. The user for PaaS is usually a developer, not a system admin. As you move down the pyramid from SaaS to PaaS and then to IaaS, you're increasing complexity in terms of your knowledge and management of infrastructure resources, and as you move up, you're increasing the ease of use. 

Another metaphor is with a car. IaaS is like leasing a car. So if you've ever leased a car, you probably did a lot of research, and you care about the specs of the car and the performance. You care about the color of the car, what kind of car it is. You're the one driving and you're paying for it. You're also paying for the gas and any tolls or maintenance. PaaS is more like renting a car. So say you're on vacation and you just got off the airport and you're going to pick up your rental car. You don't really care what color it is. You don't really even care about the specs of it, but you're still driving and you're paying for the gas and any tolls you go through. SaaS is more like getting a taxi or an Uber. You don't care at all about what kind of car it is, what color it is and in fact, you're not even the one driving, or paying for gas, or any tolls because that's baked into the price.

In terms of cloud computing, with IaaS, the cloud provider manages the physical resources, data centers, cooling, power, network and security, as well as computing resources that include servers and storage. With PaaS, the provider, in addition to the computing resources, also manages the platform infrastructure which includes the operating systems, development tools, databases, and business analytics. With SaaS, in addition to the infrastructure and the platform resources, the provider also hosts and manages the applications and data.

### IaaS
Infrastructure-as-a-Service, commonly referred to as “IaaS,” is a form of cloud computing that delivers fundamental compute, network, and storage resources to consumers on-demand, over the internet, on a pay-as-you-go basis. The cloud provider hosts the infrastructure components traditionally present in an on-premises data center as well as the virtualization or hypervisor layer. In an IaaS Cloud environment, customers can create or provision virtual machines (VMs) in their choice of Region and Zone available from the Cloud Provider. These VMs typically come pre-installed the customer’s choices of operating systems. The customers can then deploy middleware, install applications, and run workloads on these VMs. They can also and create storage for their workloads and backups. Cloud providers often provide customers the ability to track and monitor the performance and usage of their cloud services and manage disaster recovery.

Some key components of cloud infrastructure include:

- Physical data centers: IaaS providers manage large data centers that contain the physical machines required to power the various layers of abstraction on top of them. In most IaaS models, end users do not interact directly with the physical infrastructure but experience it as a service provided to them.
- Compute: IaaS providers manage the hypervisors and end-users programmatically provision virtual instances with desired amounts of compute, memory, and storage resources. Cloud compute typically comes with supporting services like auto scaling and load balancing that provide scalability and high performance.
- Network: Users get access to networking resources on the cloud through virtualization or programmatically, through APIs.
- Storage: There are three types of cloud data storage: object, file, and block storage. Object storage is the most common mode of storage in the cloud, given that it is highly distributed and resilient. IaaS supports a wide array of use cases.

Some typical use cases include

- **Test and development**: organizations today are using cloud infrastructure services to enable their teams to set up test and development environments faster, helping create new applications more quickly. By abstracting the low-level components, cloud infrastructure is helping developers focus more on business logic than infrastructure management.
- **Business continuity and disaster recovery** require a significant amount of technology and staff investments. IaaS is helping organizations reduce this cost and make applications and data accessible as usual during a disaster or outage.
- **Faster deployment and scaling**: Organizations are using cloud infrastructure to deploy their web applications faster and also scale infrastructure up and down as demand fluctuates.
- **High performance computing**: organizations are leveraging the high-performance computing capabilities of cloud infrastructure to solve complex problems involving millions of variables and calculations such as climate and weather predictions and financial modeling.
- **Big data analysis**: Mining massive data sets to locate valuable patterns, trends, and associations requires a huge amount of processing power. Cloud infrastructure not only provides the required high-performance computing but also makes it economically viable.

While there are some concerns regarding the lack of transparency in the cloud infrastructure’s configuration and management, and dependency on a third-party for workload availability and performance, Infrastructure-as-a-Service is the fastest growing cloud model today.

### PaaS

### SaaS


## Cloud Computing Deployment Models

### Public Cloud

### Private Cloud


### Hybrid Cloud





## Components of Cloud Computing



## Emergent Trends and Practices



## Cloud Security and Monitoring



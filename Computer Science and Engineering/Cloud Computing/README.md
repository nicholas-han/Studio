# Introduction to Cloud Computing
## Overview of Cloud Computing
Cloud computing is a business model or service that combines technology like virtualization with a few of the latest trends and if you require extra bandwidth, a cloud-based service can address that need promptly, rather than waiting for a complex and costly update to your IT infrastructure. Users can customize their applications using cloud services from anywhere if they have an Internet connection. In addition, cloud computing enables efficient marketing of applications regardless of maintenance and cost.

### History of Cloud Computing
Cloud computing is an evolution of technology over time. The concept of cloud computing dates to the 1950s when large-scale mainframes with high-volume processing power became available. The practice of time sharing (or resource pooling) evolved to make efficient use of the computing power of mainframes. Using dumb terminals, whose sole purpose was facilitating access to the mainframes, multiple users could access the same data storage layer and CPU power from any terminal.

In the 1970s, with the release of an operating system called Virtual Machine (VM), it became possible for mainframes to have multiple virtual systems, or virtual machines, on a single physical node. The virtual machine operating system evolved from the 1950s application of shared access of a mainframe. By allowing multiple distinct computing environments to exist on the same physical hardware. Each virtual machine hosted guest operating systems that behaved like they had their own memory, CPU, and hard drives, even though these were shared resources. Virtualization thus became a technological driver and a massive catalyst for some of the most significant evolutions in communications and computing. Even 20 years ago, physical hardware was quite expensive.

With the internet becoming more accessible, and the need to make hardware costs more viable, servers were virtualized into shared hosting environments, virtual private servers, and virtual dedicated servers, using the same functionality the virtual machine operating system provided. So, for example, if a company needed an ‘x’ number of physical systems to run their applications, they could split one physical node into multiple virtual systems.

A hypervisor is a small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources. A hypervisor also separates the Virtual Machines logically, assigning each slice of the underlying computing power, memory, and storage, preventing the virtual machines from interfering with each other. So if, for example, one operating system suffers a crash or a security compromise, the others can keep working. As technologies and hypervisors improved and could share and deliver resources reliably, some companies decided to make the cloud’s benefits accessible to users. These users did not have an abundance of physical servers to create their cloud computing infrastructure. Since the servers were already online, spinning up a new instance was instantaneous. Users could now order cloud resources from a larger pool of available resources and pay for them on a per-use basis, also known as pay-as-you-go or utility computing model. This model became one of the key drivers behind cloud computing's launching. The pay-per-use model allowed companies and even individual developers to pay for the computing resources as and when they used them, just like units of electricity. This allowed them to switch to a more cash-flow friendly OpEx model from a CapEx model. This model appealed to all sizes of companies, those who had little or no hardware, and even those that had lots of hardware, because now, instead of making substantial capital expenditures in hardware, they could pay for compute resources as and when needed. It also allowed them to scale their workloads during usage peaks, and scale down when usage subsided. And this gave rise to modern-day cloud computing.

### Definition of Cloud Computing
The US National Institute of Standards and Technology (NIST) defines cloud computing as a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or service provider interaction. Examples of computing resources include networks, servers, storage, applications, and services. This cloud model is composed of five essential characteristics, four deployment models and three service models.

### Five Essential Characteristics
The five essential characteristics of the cloud are on-demand self service, broad network access, resource pooling, rapid elasticity, and measured service.

- **On-demand self-service** means you can access cloud resources whenever required. Services are always available on all days of the year. There are no exceptions other than when services are unable due to an outage or security breach.
- **Broad network access** means that cloud computing resources can be accessed through the network. Public cloud services could generally be accessible from anywhere and on any device with Internet connectivity and browser capabilities. Internet access is mandatory for accessing public cloud services.
- With **resource pooling**, consumers save on costs when using a shared model, which provides cloud providers economies of scale, making the cloud cost efficient. Computing resources are pulled to serve multiple consumers using a multi-tenant model, cloud resources are dynamically assigned and reassigned according to demand without customers needing to concern themselves with the physical location of these resources.
- **Rapid elasticity** implies that you can increase or decrease resources as per your demand. Because of the elastic property of the cloud, resources can be scaled up or down vertically scaling or scaled out as in horizontal scaling.
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
Infrastructure-as-a-Service, commonly referred to as “IaaS,” is a form of cloud computing that delivers fundamental compute, network, and storage resources to consumers on-demand, over the internet, on a pay-as-you-go basis. The cloud provider hosts the infrastructure components traditionally present in an on-premises data center as well as the virtualization or hypervisor layer. In an IaaS cloud environment, customers can create or provision virtual machines (VMs) in their choice of Region and Zone available from the cloud Provider. These VMs typically come pre-installed the customer’s choices of operating systems. The customers can then deploy middleware, install applications, and run workloads on these VMs. They can also and create storage for their workloads and backups. Cloud providers often provide customers the ability to track and monitor the performance and usage of their cloud services and manage disaster recovery.

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
Platform as a Service, commonly referred to as PaaS, is a cloud computing model that provides customers a complete platform to develop, deploy, manage and run applications created by them or acquired from a third party. The PaaS provider hosts everything: servers, networks, storage, operating system, application runtimes, APIs, middleware, databases and other tools at their data center. The provider also takes responsibility for the installation, configuration, and operation of the application infrastructure, leaving the user responsible for only the application code and its maintenance. Customers pay for this service on a usage basis and purchase resources on demand. With IaaS, the cloud provider offers access to raw computing resources such as servers, storage, and networking, while the user is responsible for the platform and application software. With PaaS, the cloud service provider delivers and manages the entire platform infrastructure, abstracting users from the lower level details of the environment.

Some essential characteristics of PaaS include:

- PaaS clouds are distinguished by the **high level of abstraction** they provide to the users, eliminating the complexity of deploying applications, configuring infrastructure, and provisioning and configuring supporting technologies like load balancers and databases.
- PaaS clouds provide **services and APIs** that help simplify the job of developers in delivering elastically scalable and highly available cloud applications. These services typically include a variety of capabilities such as APIs for distributing, caching, queuing and messaging, file and data storage, workload management, user identity, and analytics, thus eliminating the need to integrate disparate components.
- The PaaS **runtime environment** executes end user code according to policies set by the application owner and cloud provider.
- Many of the PaaS offerings provide developers with **rapid deployment mechanisms** or push and run mechanism for deploying and running applications.
- PaaS offerings support a range of **application infrastructure and middleware capabilities** such as application servers, database management systems, business analytics servers, mobile backend services, integration services, business process management systems, rules engines, and complex event processing systems. Such an application infrastructure assists developers by reducing the amount of code that must be written while expanding the application's functional capabilities.

The most important use case for PaaS is strategic, build, test, deploy, enhance and scale applications rapidly and cost effectively.

- **API development and management.** Organizations are using PaaS to develop, run, manage and secure APIs and microservices, which are loosely coupled, independently deployable components and services.
- **Internet of Things (IoT).** PaaS clouds support a broad range of application environments, programming languages, and tools used for IoT deployments.
- **Business analytics and business intelligence.** PaaS tools allow organizations to analyze their data to find business insights that enable more informed business decisions and predictions.
- **Business Process management (BPM).** Organizations are using the PaaS cloud to access BPM platform delivered as a service.
- **Master data management (MDM).** Organizations are leveraging the PaaS cloud to provide a single point of reference for critical business data, such as information about customer transactions and analytical data to support decision-making.

Some advantages of using PaaS include:

- **Scalability**, made possible because of the rapid allocation and deallocation of resources with a pay-as-you-use model offered by PaaS.
- The APIs support services and middleware capabilities that PaaS clouds provide assist developers in focusing their efforts on application development and testing, resulting in **faster time-to-market** for their products and services. Middleware capabilities also reduce the amount of code that need to be written while expanding the application's functional capabilities.
- **Greater agility and innovation**, because using PaaS platforms means that you can experiment with multiple operating systems, languages and tools without having to invest in these resources. You can evaluate and prototype ideas with very low risk exposure, resulting in faster, easier, less risky adoption of a wider range of resources.

Some of the key PaaS offerings available in the market today include AWS Elastic Beanstalk, cloud Foundry, IBM cloud Paks, Windows Azure, Red Hat OpenShift, Magento Commerce cloud, force.com, and Apache Stratos.

PaaS clouds do come with some risks, risks that all cloud offerings have in general, such as information security threats and dependency on the service provider's infrastructure. Services can get impacted when a service provider's infrastructure experiences downtime. Customers also don't have any direct control over the changes that may take place when a provider makes changes in its strategy, service offerings or tools. But the benefits can far outweigh these risks. PaaS continues to experience strong growth and is predicted to become the prevailing platform delivery model moving forward.

### SaaS
Software-as-a-Service, or “SaaS,” is a cloud offering that provides users with access to a service provider’s cloud-based software. SaaS providers maintain the servers, databases, and code that constitute an application. They also manage access to the application, including security, availability, and performance. Applications reside on a remote cloud network, and users use these applications without having to maintain and update the infrastructure.

Core business processes supported by SaaS today include email and collaboration via offerings such as Microsoft's Office 365 and Google's Gmail, Customer Relationship Management via services such as NetSuite CRM and Salesforce, Human Resource Management via services from Workday and SAP SuccessFactors, financial management, billing and collaboration, and many more. According to Forrester Research, SaaS has overtaken on-premises solutions in categories such as human capital management (HCM), customer relationship management (CRM), and collaboration. Solutions once available with several different deployment options are now SaaS-only.

Let’s look at key characteristics of Software-as-a-Service: SaaS clouds have a multitenant architecture. Infrastructure and code are maintained centrally and accessed by all users. SaaS makes it easy for users to manage privileges, monitor data use, and ensure everyone sees the same information at the same time. Security, compliance, and maintenance are all part of the offering. In SaaS, customizations are often limited, however some SaaS applications may allow certain types of customizations like branding; they can modify data fields and enable or disable features within the business process. These customizations are preserved through upgrades. Users pay for the use of the services via a subscription model. The use of resources can be scaled easily, depending on service needs.

Key benefits of adopting SaaS: Businesses can directly procure solutions without upfront capital and assistance from IT, greatly reducing the time from decision to value from months to days. SaaS greatly increases workforce productivity and efficiency. Users can access core business apps from wherever; they can also buy and deploy apps in minutes reducing the typical obstacles enterprises have to test the products they might use. Using SaaS applications, individuals and small enterprises can spread out their software costs over time.

Organizations are moving to SaaS for their core business needs as part of their strategic transformation to

- Reduce on-premises IT infrastructure and reduce capital expenditure
- Avoid the need for ongoing upgrades, maintenance, and patching, done traditionally by internal IT resources
- Run applications reliably with minimal input, for example, email servers and office collaboration and productivity tools
- Opt for SaaS eCommerce Platforms to manage their websites, marketing, sales, and operations
- Take advantage of the resilience and business continuity of the cloud provider

Enterprises are now developing SaaS integration platforms (or SIPs) for building additional SaaS applications, moving SaaS beyond standalone software functionality to a platform for mission-critical applications.

SaaS does evoke some concerns, as well. Primary among them being data ownership and data safety. Security is an important consideration when you’re allowing a third-party to maintain business-critical data. And application access relies on a good network connection. But the benefits far outweigh the concerns, with SaaS making up the largest segment of the cloud market today.

## Cloud Computing Deployment Models
Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. The four cloud deployment models include—Public cloud, Private cloud, Community cloud and Hybrid cloud.

### Public Cloud
In a public cloud model, users get access to servers, storage, network, security, and applications as services delivered by cloud service providers over the internet. Using web consoles and APIs, users can provision the resources and services they need. The cloud provider owns, manages, provisions, and maintains the infrastructure, renting it out to customers either for a subscription charge or usage-based fee. Users don’t own the servers their applications run on or storage their data consumes, or manage the operations of the servers, or even determine how the platforms are maintained. In very much the same way that we consume and pay for utilities such as water, electricity, or gas in our everyday lives, we don’t own any of these cloud resources—we make an agreement with the service provider, use the resources, and pay for what we use within a certain period. Public clouds offer significant cost savings in terms of Total Cost for Ownership (TCO) as the provider bears all the capital, operational, and maintenance expenses for the infrastructure and the facilities they are hosted in. It makes scalability as easy as requesting more capacity. However, with a public cloud, the user does not have any control over the computing environment and is subject to the performance and security of the cloud provider’s infrastructure.

There are several public cloud providers in the market today, such as Amazon Web Services, Microsoft Azure, IBM cloud, Google cloud Platform, and Alibaba cloud. While all providers include a common set of core services, such as servers, storage, network, security, and databases, they also offer a wide spectrum of niche services with varied payment options. 

A public cloud is a virtualized multi-tenant architecture enabling tenants or users to share computing resources, residing outside their firewalls. The cloud provider's pool of resources, including infrastructure, platforms, and software, are NOT dedicated for use by a single tenant or organization. Resources are distributed on an as-needed basis offered through a variety of subscription and pay-as-you-go models.

Public clouds have significant benefits.

- Vast **on-demand resources** are available, allowing applications to respond seamlessly to fluctuations in demand.
- Considering the large number of users that share the centralized cloud resources on-demand, the public cloud offers **the most significant economies of scale**.
- The sheer number of server and network resources available on the public cloud means that a public cloud is **highly available**. If one physical component fails, the service still runs unaffected on the remaining available components.

It’s also important to note some concerns users have regarding public clouds.

- **Security.** Security issues such as data breaches, data loss, account hijacking, insufficient due diligence, and system and application vulnerability seem to be some of the fears users continue to have concerning security in the public cloud.

- **Data sovereignty compliance.** With data being stored in different locations and accessed across national borders, it has also become increasingly critical for companies to be compliant with data sovereignty regulations governing the storage, transfer, and security of data.

A service provider’s ability to not just keep up with the regulations, but also the interpretation of these regulations, is a concern shared by many businesses

Organizations are increasingly opting to access cloud-based applications and platforms so their teams can focus on building and testing applications, and reducing time-to-market for their products and services. Businesses with fluctuating capacity and resourcing needs are opting for the public cloud. Organizations are using public cloud computing resources to build secondary infrastructures for disaster recovery, data protection, and business continuity. More and more organizations are using cloud storage and data management services for greater accessibility, easy distribution, and backing up their data. IT departments are outsourcing the management of less critical and standardized business platforms and applications to pubic cloud providers.

### Private Cloud
The National Institute of Standards and Technology defines private cloud as cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers, such as the business units within the organization. It may be owned, managed, and operated by the organization, a third party or some combination of them, and it may exist on or off premises.

Private cloud platforms can be implemented internally or externally. When the platform is provisioned over an organization's internal infrastructure, it runs on-premises and is owned, managed, and operated by the organization. When it is provisioned over a cloud providers infrastructure, it is owned, managed, and operated by the service provider. This external private cloud offering that resides on a cloud service providers infrastructure is called a **Virtual Private cloud (VPC)**. A VPC is a public cloud offering that lets an organization establish its own private and secure cloud-like computing environment in a logically isolated part of a shared public cloud. Using a VPC, organizations can leverage the dynamic scalability, high availability, and lower cost of ownership of a public cloud, while having the infrastructure and security tailored to the organization's unique needs. Virtual Private cloud are offered by most public cloud providers, such as IBM and Amazon.

A private cloud is a virtualized environment modeled to bring in the benefits of a public cloud platform without the perceived disadvantages of an open-end shared public platform. Users of a private cloud, such as developers and business units in an organization still get to leverage benefits such as economies of scale, granular scale, operational efficiencies, and users self-service while exercising full control over access, security and compliances specific to their organization and business.

Private cloud provide you with

- The ability to leverage the value of cloud computing using systems that are directly managed or under perceived control of the organization's internal IT.
- The ability to better utilize internal computing resources, such as the organization's existing investments in hardware and software, thereby reducing costs.
- Better scalability through virtualization and cloud bursting, that is, leveraging public cloud instances for a period of time, but returning to the private cloud when the surge is meet.
- Controlled access and greater security measures customized to specific organizational needs.
- The ability to expand and provision things in a relatively short amount of time, providing greater agility.

Organizations may choose to opt for private cloud because of various reasons, because their applications provide a unique competitive advantage. There are security and regulatory concerns, or because their data is highly sensitive and subject to strict industry or governmental regulations.

Some common use cases for a private cloud include:

- A private cloud is an opportunity for organizations to modernize and unify their in-house and legacy applications. Moving these applications from their dedicated hardware to the cloud also allows them to leverage the power of the compute resources and multiple services available on the cloud.
- Using the private cloud, organizations are integrating data and application services from their existing applications with public cloud services. This allows them to leverage their private cloud's compute capability for the larger jobs while pulling data into an application on a private cloud to leverage public cloud services. Essentially, opening their data centers to work with cloud services.
- Application portability is a key feature of cloud platforms. Using the private cloud gives organizations the ability to build applications anywhere and move them anywhere without having to compromise security and compliance in the process.
- Some of the key reasons that may prevent an organization for moving to a public cloud include security and regulatory concerns and data sensitivity. A private cloud offers these organizations the benefits of on-demand enterprise resources while exercising full control over critical security and compliance issues from within the environment of their dedicated cloud.

### Hybrid Cloud
Hybrid cloud is a computing environment that connects an organization's on-premise private cloud and third-party public cloud, into a single flexible infrastructure for running the organizations applications and workloads. The mix of public and private cloud resources gives organizations the flexibility to choose the optimal cloud for each application or workload. Workloads move freely between the two clouds as needs change, organizations can choose to run the sensitive, highly regulated, and mission-critical applications or workloads with reasonably constant performance and capacity requirements on private cloud infrastructure, while deploying the less sensitive and more dynamic workloads on the public cloud. With proper integration and orchestration between the public and private clouds, you can leverage both clouds for the same workload. For example, you can leverage public cloud instances for a period of time, but returned to the private cloud when the search is met, also known as cloud bursting.

The key tenants of a hybrid cloud are interoperability, scalability, and portability. Hybrid cloud is interoperable, which means that the public and private cloud services can understand each other's APIs, configuration, data formats, and forms of authentication and authorization. When there's a spike in demand, a workload running on the private cloud can leverage the additional public cloud capacity making it scalable. A hybrid cloud is also portable. Since you're no longer locked in with a specific vendor, you can move applications and data not just between on-premise and cloud systems, but also between cloud service providers. Hybrid is about taking the best of both worlds.

There are two common types of hybrid clouds, hybrid monocloud and hybrid multicloud. Hybrid monocloud is a hybrid cloud with one cloud provider while a hybrid multicloud is an open standards-based stack that can be deployed on any public cloud infrastructure. The difference lies in the flexibility that the hybrid multicloud offers organizations to move workloads and environments from one vendor to another. There's also a variant of hybrid multicloud called the composite multicloud, which makes this flexibility even more granular as it distributes single applications across multiple providers, allowing you to move application components across cloud services and vendors as needed.

Hybrid cloud offers significant benefits in areas of security and compliance, scalability and resilience, resource optimization and cost-saving. A hybrid cloud lets organizations deploy highly regulated or sensitive workloads in a private cloud while running the less sensitive workloads on a public cloud. Using a hybrid cloud, you can scale up quickly, inexpensively, and even automatically using the public cloud infrastructure, all without impacting the other workloads running on your private cloud. Because you're not locked in with a specific vendor and also don't have to make either/or decisions between the different cloud models, you can make the most cost efficient use of your infrastructure budget. You can maintain workloads where they are most efficient, spin up environments using Pay-As-You-Go in the public cloud, and rapidly adopt new tools as you need them. However, hybrid clouds are complex and challenging to deploy and maintain since they involve synchronization, redirection, latency, security, portability, interoperability, and compatibility of policies, applications and data and so on. A typical organization will have a range of applications and workloads spread across private, public, and traditional IT environments. This represents a range of opportunities for optimization via a hybrid cloud approach.

Let's look at some increasingly common Hybrid cloud use cases.

- **Software-as-a-service integration.** Through Hybrid Integration, Organizations are connecting software-as-a-service applications available in the public cloud to their existing public cloud, private cloud and traditional IT applications to deliver new solutions.
- **Data and AI integration.** Organizations today are creating richer and more personal experiences by combining new data sources on the public cloud, such as weather, social, the Internet of Things, CRM, and ERP, with existing data and analytics, machine learning and AI capabilities.
- **Enhancing legacy apps.** An increasing number of organizations are using public cloud services to upgrade the user experience of their on-premises applications and deploy them globally to new devices while incrementally modernizing their core business systems.
- **VMware migration.** More and more organizations are lifting and shifting their on-premises virtualized workloads to a public cloud without conversion or modification to reduce their on-premises datacenter footprint, and position themselves to scale without added capital expense. 
- **Leveraging public cloud services.** Using the private cloud, organizations are integrating data and application services from their existing applications with public cloud services. This allows them to leverage their private cloud compute capability for the larger jobs while pulling data into an application on a private cloud to leverage public cloud services, essentially, opening their datacenters to work with cloud services.

### Community Cloud
#### What is a community cloud?
A community cloud is defined by NIST SP 800-145 as:
“Cloud infrastructure [that] is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.”

#### Why community cloud?
Community cloud approach is used by organizations for the following reasons:

- The community cloud members work under the same set of security controls.
- The approach provides the members the same attributes like citizenship and authorization controls while giving limited physical and/or logical access to resources.
- It also supports data localization and some data sovereignty requirements based on the location of the community cloud’s data centers. 
- The approach defines a perimeter security model encompassing the community cloud. 

#### Implementation of software-defined community cloud 
To establish a security perimeter, most legacy community clouds depend on physical separation from other clouds. However, this implementation could not meet the advanced security, manageability, or compliance requirements of the industry.

In the modern architecture, a software-defined community cloud is designed to deliver the required benefits. Google Cloud is a software-defined approach that provides security and compliance assurances without the strict physical infrastructure constraints of legacy approaches. The Google community clouds use a combination of technologies referred to as “assured clouds” that can:

- Define communities around common projects, security and compliance requirements, and policy.
- Separate shared community projects from other projects.
- Modify capabilities of a community’s boundary based on policy-controlled and audited configuration changes.

#### Comparison between traditional and software-defined community cloud
The software-defined community cloud provides many benefits to the users in comparison to the traditional community cloud implementation. The following table depicts the comparison between the two implementations based on the characteristics as stated in the definition given by NIST.

| Characteristic | NIST Definition SP 800-145 | Traditional Cloud Community Implementation | Software-Defined Community Cloud |
|-------|-------|-------|-------|
| Infrastructure Exclusivity | The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns | Separate data centers with separate infrastructure | Each project is effectively a private cloud with isolated infrastructure primitives |
| All users subject to common security controls | (implied) | Same security controls apply across exclusive infrastructure shared by the community | Assured Workloads controls are scoped to the community and enforced through terms of service | 
| Personhood and citizenship of support staff | It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them | Personnel must be physically located at dedicated facilities | Access management service restricts support to personnel with required attributes (personhood, citizenship, work location, and more) | 
| Data localization | and it may exist on or off premises | Community dedicated storage devices  | Enforced by software | 
| Defined security parameter | (implied) | The community is the enclave | Each project is its own enclave | 

#### Software defined community cloud as a new type of “Government Cloud”
In Google Cloud Platform (GCP), a project is a unique, logical grouping of “infrastructure primitives.” In this context, an infrastructure primitive is any atomic unit of capacity in GCP – a virtual machine (VM), a persistent disk (PD), a storage bucket, and others. Projects are “global resources” that can be assigned infrastructure primitives from any region or zone.

Every project is an individual project separate from other customers’ projects. Low-level resources like hypervisors, blocks in our distributed blockstore that underlies Google Cloud Storage (GCS), and other components are isolated with resource abstractions that enforce the isolation both logically and cryptographically. 

A Private Cloud deployment model is defined in NIST SP 800-145 as:

Cloud infrastructure [that] is provisioned for exclusive use by a single organization comprising multiple consumers (such as business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.

When a project is created within GCP, the infrastructure primitives that are assigned to that project are scoped to only that project. This scoping of infrastructure primitives effectively creates an “enclave” per Project.

When overlaid with Assured Workloads constraints for data residency, support personnel attributes, and security controls common to that community, these per-project private cloud enclaves become software-defined community clouds.

#### Benefits of a software-defined community cloud
The approach Google Cloud has taken brings multiple benefits such as meeting security and compliance requirements. New hardware, new services, and improvements to existing services are accessed faster than in traditional community clouds. The process by which new cloud technology can be onboarded and made available is also faster. Overall efficiency is improved in this model due to the scale of infrastructure available to the community; this can translate to improved availability and performance. Security enhancements can be scaled and implemented more quickly.

### Summary of Deployment Models
As a summary, deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. There are four main deployment models available on the cloud—public, private, hybrid, and community.

In the public cloud model, the service provider owns, manages, provisions, and maintains the physical infrastructure such as data centers, servers, networking equipment, and storage, with users accessing virtualized computing, networking and storage resources as services.

In the private cloud model, the provider provisions the cloud infrastructure for exclusive use by a single organization. The private cloud infrastructure can be internal to the organization and run or on-premises. Or it can be on a public cloud, as in the case of Virtual Private Clouds (VPC), and be owned, managed, and operated by the cloud provider.

In the hybrid cloud model, an organization’s on-premise private cloud and a third-party, public cloud are connected as a single, flexible infrastructure that leverages the features and benefits of both Public and Private clouds.

In the community cloud model, the provider provisions the cloud infrastructure for use by a community of organizations with shared concerns. One or more of the organizations in the community, a third-party provider, or both are responsible for the ownership, management, and operation of this infrastructure.

## Overview of Cloud Infrastructure
After choosing the cloud service model and the cloud type offered by vendors, customers need to plan the infrastructure architecture. The infrastructure layer is the foundation of the cloud. This layer consists of physical resources that are housed in Regions, Zones and Data Centers.

A Cloud provider’s IT environment is typically distributed across many Regions around the world. A cloud Region, is a geographic area or location where a Cloud provider’s infrastructure is clustered, and may have names like NA South or US East. The cloud Regions are isolated from each other so that if one Region was impacted by a natural disaster like an Earthquake, the Cloud operations in other Regions would keep running. Each Cloud Region can have multiple Zones (or Availability Zones or AZ for short), which are typically distinct Data Centers with their own power, cooling and networking resources. These Zones can have names like DAL-09 or us-east-1. The isolation of zones improves the cloud’s overall fault tolerance, decreases latency, and avoids creating a single shared point of failure. The Availability Zones (and DataCenters within them) are connected to other AZs and regions, private datacenters and the Internet using very high bandwidth network connectivity. A cloud Data center is a huge room or a warehouse containing cloud infrastructure. These data centers contain pods and racks or standardized containers of computing resources such as servers, as well as storage, and networking equipment - virtually everything that a physical IT environment has.

**Computing Resources**: Cloud providers offer several compute options – Virtual Servers, Bare Metal Servers, and “Serverless” computing resources. Most of the servers in a cloud datacenter run hypervisors to create virtual servers or virtual machines (also called VMs for short), that are software-based computers, based on virtualization technologies. Other servers in the racks are bare metal servers that are physical servers that aren’t virtualized. Customers can provision VMs and Bare Metals servers as and when they need them and run their workloads on them. Cloud users can also run their workloads on serverless computing resources, which are an abstraction layer on top of virtual machines. We will talk about all three compute options in greater detail in subsequent videos. 

**Storage**: Information and data can consist of files, code, documents, images, videos, backups, snapshots, and databases and can be stored in many different types of storage options on the cloud. Bare Metal Servers and Virtual Servers are provisioned with default storage in local drives.

**Networking**: Networking infrastructure in a cloud datacenter includes traditional networking hardware like routers and switches, but more importantly for users of the cloud, the cloud providers have Software Defined Networking (or SDN) options where certain networking resources are virtualized or made available programmatically, through APIs. This allows for easier network provisioning, configuration, and management in the cloud. When servers in the cloud are provisioned, you need to setup their public and private network interfaces. The public network interfaces, as the name suggests, connect the servers to the public internet, whereas the private ones provide connectivity to your other cloud resources and help keep them secure. As in the physical IT world, network interfaces in the cloud need to have IP addresses and subnets either assigned automatically or configured. In a cloud environment it is even more important to configure which network traffic and users can access your resources, which can be done by setting up Security Groups and Access Control Lists (or ACLs). For further security and isolation of your resources in the cloud, most cloud providers provide Virtual Local Area Networks (VLANs), Virtual Private Clouds (VPCs), and Virtual Private Networks (VPNs). Some of the traditional hardware appliances such as firewalls, load balancers, gateways and traffic analyzers can also be virtualized and made available as services in the cloud. Another networking capability provided by the cloud providers is Content Delivery Networks (CDNs), that distribute content to multiple points throughout the world so users accessing the content can access it more quickly by getting it from a point nearest to them.

## Computing Resources
### Virtualization and Virtual Machines (VMs)
Virtualization is a fairly old technology, but it's still super relevant to building our cloud computing strategy today. Simply put, virtualization is the process of creating a software based, or virtual, version of something, whether that be compute, storage, networking, servers or applications.

What makes virtualization feasible is something called the hypervisor. A hypervisor is simply a piece of software that runs above the physical server or host. It essentially pulls the resources from the physical server and allocates them to your virtual environments. There are two main types of hypervisors, type 1: bare metal and type 2: hosted.

Bare-metal hypervisors are installed directly on top of the physical server. These are the most frequently type of used hypervisors and are most secure, low latency, and most commonly found in the market. Some examples are VMware, ESXi, Microsoft Hyper-V and open-source KVM.

The other type of hypervisor is hosted. What makes these different is that there is a layer of host OS that sits between the physical server and the hypervisor. These are a lot less frequent. They're mostly used for end-user virtualization, and examples includ Oracle VirtualBox or VMware Workstation. They have a higher latency than bare metal hypervisors.

Once you have your hypervisor installed, you can build virtual environments, or virtual machines (VMs). A VM is simply a software based computer, and runs like a physical computer. Each VM has an operating system and applications, and is completely independent of one another, but you can run multiple VMs on a hypervisor that manages the resources and allocates to different virtual environments from the physical server. Because they're independent, you can run different operating systems on different virtual machines. Because they're independent, they're also extremely portable. You can move a virtual machine from one hypervisor to another hypervisor on a completely different machine almost instantaneously, which gives you much flexibility and portability within your environment.

Some key benefits include 

1. **Cost savings.** When you think about this and the fact that you can run multiple virtual environments from one piece of infrastructure, means that you can drastically reduce your physical infrastructure footprint. This is consolidation at its core, and the fact that you don't have to maintain nearly as many servers, run as much electricity, save on maintenance costs, means that you save on your bottom line at the end of the day.
2. **Agility and speed.** Spinning up a virtual machine is relatively easy and quick - a lot simpler than provisioning an entire new environment if developers want to spin up a new environment to run a dev test scenario. 

3. **Lowers downtime.** When a host goes out unexpectedly, you can move virtual machines from one hypervisor to another on a different physical server.

Virtual Machines or VMs are also known as Virtual Servers or Virtual Instances, or simply instances, depending on the cloud provider. The various cloud providers make VMs available in a variety of configurations and deployment options to serve different use cases. When you create a virtual server in the cloud, you specify the Region and Zone or Data Center you want the server to be provisioned in and the Operating System you want on it. You can choose between shared (that is, a multi-tenant) VMs or dedicated (that is, a single-tenant) VMs. You can also choose between hourly or monthly billing and select storage and networking options for the virtual server.

#### Shared or Public Cloud VMs
Shared or public cloud VMs are provider-managed, multi-tenant deployments that can be provisioned on-demand with predefined sizes. Being multi-tenant means that the underlying physical server is virtualized and is shared across other tenants or users. To satisfy different workloads, cloud providers offer predefined sizes and configurations ranging from a single virtual core and a small amount of RAM to multiple virtual cores and much larger amounts of RAM. For example, there can be configurations for Compute Intensive workloads, Memory intensive workloads, or High Performance I/O. Rather than pick from only pre-defined sizes, some providers also offer custom configurations that allow users to define the number of cores and RAM and local storage characteristics.

Public VMs are usually priced by the hour (or in some cases even seconds) and configurations start as low as pennies per hour. Some providers also let you get monthly VMs, which can result in some cost savings if you know you will run the VM for at least a month, but if you decide to de-commision the VM in the middle of the month, you will still be charged for the full month.

#### Transient or Spot VMs
Transient or Spot VMs take advantage of unused capacity in a cloud data center. Cloud providers make this unused capacity available to users at a much lower cost than regular VMs of similar sizes. Although the Transient VMs are available at a huge discount, the cloud provider can choose to de-provision them at any time and reclaim the resources for provisioning regular, higher-priced, VMs. Because you run the risk of losing these VMs when capacity in the data center decreases, these VMs are great for non-production workloads such as testing and developing applications. They are also useful for running stateless workloads, testing scalability, or running big data and high performance computing (HPC) workloads at a low cost.

#### Reserved Virtual Servers
Reserved virtual server instances allow you to reserve capacity and guarantee resources for future deployments. You reserve desired amount of virtual server capacity, provision instances from that capacity when you need them, and choose a term, such as 1 year or 3 years, for your reserved capacity. You're guaranteed this capacity within the data center of your choice for the life of the contract term. By committing to a longer term, you can also lower your costs compared to hourly or monthly instances. This can be useful when you know you require at least a certain level of cloud capacity for a specific duration.

If you exceed your reserved capacity, you can always choose to supplement your unplanned usage and capacity requirements with hourly or monthly VMs. Note however that not all predefined VMs families or configurations may be available as reserved. Dedicated hosts offer single-tenant isolation. This means that only your VMs run on a given host so they can make exclusive use of full capacity and resources of the underlying hardware. When provisioning a dedicated host, you need to specify the data center and POD in which you want your host placed. You then assign instances, or virtual machines, to a specific host. This allows for maximum control over workload placement. Dedicated hosts are typically used for meeting compliance and regulatory requirements or meet specific licensing terms.

### Bare Metal Servers
A bare metal server is a single tenant, dedicated physical server. In other words, it's dedicated to a single customer. The cloud provider actually takes the physical server and plugs it into a rack in a data center for customers. The cloud provider manages the server up to the operating system or OS, which means if anything goes wrong with the hardware or rack connection, they will fix or replace it, and then reboot the server. The customer is responsible for administering and managing everything else on the server.

Bare metal servers are either pre-configured by the cloud provider to meet workload packages or they can be custom-configured as per customer specifications. This includes the processors, RAM, hard drives, specialized components, and the OS. Customers can also install their own OS and can install certain hypervisors that aren't available from the cloud provider, and thus create their own virtual machines and farms. With bare metal servers, you can also add GPUs, which are designed for accelerating scientific computation, data analytics, and rendering professional grade virtualized graphics.

Because bare metal servers are physical machines, they take longer to provision than virtual servers. Preconfigured builds of bare metal can take 20-40 minutes to provision and custom builds can take around three or four hours. But these provisioning times can vary by cloud provider. As bare metal servers are dedicated for use by a single client at any given time, they tend to be more expensive than similarly sized virtual machines. Also note that unlike virtual servers, not all cloud providers provide bare metal servers. 

Since bare metal servers are fully customizable, they can do what a customer wants in the most demanding environments. Bare metal servers are dedicated and intended for long-term high-performance use in highly secure and isolated environments. Clients have full access and control of bare metal servers because there's no hypervisor required. As there is no sharing underlying server hardware with other customers, bare metal servers fulfill the demanding needs of high-performance computing (HPC), and data intense applications that require minimal latency related delays. These servers also excel in big data analytics applications and GPU-intensive solutions.

Some workload examples that bare metal servers satisfy are ERP, CRM, AI, deep learning, and virtualization. If you use any applications that require high degrees of security control or apps that you've typically run in an on-premises environment, then a bare metal server is a good alternative in the cloud. When comparing bare metal servers to virtual servers, some of the most important considerations are found in customer need. Bare metal servers work best for CPU and I/O intensive workloads, excel with highest performance and security, satisfy strict compliance requirements, and offer complete flexibility, control, and transparency, but come with added management and operational overhead. Whereas virtual servers are rapidly provisioned, provide an elastic and scalable environment, and are low cost to use. However, since they share underlying hardware with other virtual servers, they can be limited in throughput and performance.

### Containers


## Storage


### File Storage

### Block Storage


### Object Storage


## Networks

### Content Delivery Networks


## Hybrid Multicloud, Microservices and Serverless

## Cloud Native Applications and DevOps



## Cloud Security and Monitoring



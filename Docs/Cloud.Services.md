# Cloud Services

## Overview: 

Services running remotely as an alternate to locally installed infrastructure or hardware. Typically using servers located near the regions of users.

**SaaS**(Software as a Service): When a cloud provider delivers an entire application or program to the customer

**PaaS**(Platform as a Service): When a cloud provider offers a preconfigured platform to the customer

**IaaS**(Infrastructure as a Service): When a cloud provider supplies only the bare-bones computing experience

* Amazon's EC2
* Google Compute Engine
* Microsoft Azure Compute

## Scaling Deployments

In this context, Capacity is the how much the service can deliver.  The available capacity is tied to the number and size of servers involved.

Ways to measure capacity:
<table>
    <th>System</th><th>Metric</th>
    <tr><td>Data</td><td>total disk space</td></tr>
    <tr><td>Web Server</td><td>QPS (queries per second)</td></tr>
    <tr><td>Web Server</td><td>total bandwidth per hour</td></tr>
</table>

We can measure capacity in other fun ways, like the number of cat videos served in an hour or the number of digits of pi a system can calculates.  Scaling refers to capacity expanding and contracting based on the needs of the customer.  Specifically, upscaling when increasing capacity and downscaling when decreasing it.

* Horizontal Scaling: Say your web service is using Apache to serve web pages. By default, Apache is configured to support a 150 concurrent connections. If you want to be able to serve 1,500 connections at the same time, you can deploy 10 Apache web servers and distribute the load across them. This is called horizontal scaling. You add more servers to increase your capacity. If the traffic goes up you could just add more servers to keep up with it.

* Vertical Scaling: Making your nodes bigger. When we say bigger here we're talking about the resources assigned to the nodes like memories, CPU, and disk space. For example, a database server with a 100 gigabytes of disk space can store more data than with only 10 gigabytes of space. To scale this deployment we can just add a bigger disk to the machine and the same idea works for a CPU and memory too.

This approach to scaling isn't too different from what you'd need to do if you have your servers running on-premise. Instead of sending someone to change the physical deployment, for example adding more physical RAM to a server or adding 10 more physical machines in a server rack, we just modify our deployment by clicking some buttons in a web UI or using a configuration management system to automate the scaling for us.

* Automatic Scaling: When we set our service to use automatic scaling, we're using a service offered by the Cloud provider. This service uses metrics to automatically increase or decrease the capacity of the system.

* Manual Scaling: Changes that are controlled by humans instead of software.

## Cloud Types

*Public Cloud*: Cloud Services provided to you by a third party

*Private Cloud*: When your company owns the services and the rest of your infrastructure, whether that's on-site or in a remote data center

*Hybrid Cloud* A mixture of both private and public clouds

*Multi-Cloud* A mixture of both private and public clouds across different vendors

## Spinning up VMs

*Reference Images*:(disk image) Store the contents of a machine in reusable format 

*Templating*: The process of capturing all of the system configuration to let us create VMs in a repeatable way


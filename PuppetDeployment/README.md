# IT-Automation

Google IT Automation Course

# Puppet Deployment Project

This project exposes us to common Puppet tasks performed by a DevOps/SysAdmin.  


## Introduction
You want to automatically manage the computers in your company's fleet, including a number of different machines with different operating systems. You've decided to use Puppet to automate the configurations on these machines. Part of the setup is already done, but there are more rules that need to be added, and more operating systems to consider.

Prerequisite
Understands the basics of Puppet, including:

* How to create Puppet classes and rules
* How Puppet interacts with different OSs
* How to use the DSL to create complex rules

TASKS:
1. Understanding Puppet rules
2. Fetch machine information
3. Reboot machine exercise

## Understanding Puppet rules:

The goal of this exercise is for you to see what Puppet looks like in action. During this lab, you'll be connecting to two different VMs. The VM named puppet is the Puppet Master that has the Puppet rules that you'll need to edit. The VM named linux-instance is a client VM that you'll use to test that your catalog was applied successfully.

The manifests used for the production environment are located in the directory /etc/puppet/code/environments/production/manifests, which contains a site.pp file with the node definitions that will be used for this deployment. On top of that, the modules directory contains a bunch of modules that are already in use. You'll be extending the code of this deployment to add more functionality to it.

Our first micro task is to install packages on the existing Puppet VM instance.  There's a module named 'packages' on the Puppet VM instance that takes care of installing the packages that are needed on the machines in the fleet. 

Here is the package location:
`/etc/puppet/code/environments/production/modules/packages`

The `init.pp` file is located inside the:
manifests folder within the package directory.  This module already has a resource entry specifying that python-requests is installed on all machines.  Let's add descriptive code to ensure the golang package gets installed on all machines that belong to the Debian, family of operating systems. 

To install the package on Debian systems only, you'll need to use the os family fact, like this:

```
if $facts[os][family] == "Debian" {
# Resource entry to install golang package
}
```
After specifying the resource entry for the golang package:

```
if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
```
The complete `init.pp` file to this point:
```
class packages {
   package { 'python-requests':
       ensure => installed,
   }
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
}
```
As our second micro task, lets add descriptive code to ensure that the nodejs package is installed on machines that belong to the RedHat family.  After adding this, this is what our `init.pp` file looks like:

```

class packages {
   package { 'python-requests':
       ensure => installed,
   }
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
   if $facts[os][family] == "RedHat" {
     package { 'nodejs':
       ensure => installed,
     }
  }
}
```

Once you've edited the file and added the necessary resources, you'll want to check that the rules work successfully. We can do this by connecting to another machine in the network and verifying that the right packages are installed.

We will be connecting to linux-instance using its external IP address. To fetch the external IP address of linux-instance, use the following command:

```
gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

This command outputs the external IP address of linux-instance. Copy the linux-instance external IP address, open another terminal and connect to it. Follow the instructions given in the section Accessing the virtual machine by clicking on Accessing the virtual machine from the navigation pane at the right side.

Now manually run the Puppet client on your linux-instance VM instance terminal:

```
sudo puppet agent -v --test
```
Now verify whether the golang package was installed on this instance. This being an machine of the Debian family should have golang installed. Use the following command to verify this:

```
apt policy golang
```

<hr>

## Fetch machine information

It's now time to navigate to the machine_info module in our Puppet environment. In the Puppet VM terminal, navigate to the module.

`/etc/puppet/code/environments/production/modules/machine_info`

The machine_info module gathers some information from the machine using Puppet facts and then stores it in a file. Currently, the module is always storing this information in:

`/tmp/machine_info`

after viewing the contents of the `manifests/init.pp` file, we discover that the path listed does not work for windows machines.  Let's adapt the rule for windows.  

Now we will be using `$facts[kernel]` fact to check if the kernel is `windows`. If so, set a `$info_path` variable to `C:\Windows\Temp\Machine_Info.txt`, otherwise set it to `/tmp/machine_info.txt`:
```
class machine_info {
   file { '/tmp/machine_info.txt':
       content => template('machine_info/info.erb'),
   }
   if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
}
```

By default the file resources are stored in the path defined in the name of the resource (the string in the first line) within the class. We can also set different paths, by setting the path attribute.

We will now be renaming the resource to "machine_info" and then use the variable in the path attribute. The variable we are using to store the path in the above rule is $info_path.  After amending the file to customize the path:

```
class machine_info {
  if $facts[kernel] == "windows" {
       $info_path = "C:\Windows\Temp\Machine_Info.txt"
   } else {
       $info_path = "/tmp/machine_info.txt"
   }
 file { 'machine_info':
       path => $info_path,
       content => template('machine_info/info.erb'),
   }
}
```
Finally, let's adjust the template for the machine_info module.  First a quick overview of templates:

### Puppet Templates
Templates are documents that combine code, data, and literal text to produce a final rendered output. The goal of a template is to manage a complicated piece of text with simple inputs.

In Puppet, you'll usually use templates to manage the content of configuration files (via the content attribute of the file resource type).

Templates are written in a templating language, which is specialized for generating text from data. Puppet supports two templating languages:

**Embedded Puppet (EPP)** uses Puppet expressions in special tags. It's easy for any Puppet user to read, but only works with newer Puppet versions. (≥ 4.0, or late 3.x versions with future parser enabled.)
**Embedded Ruby (ERB)** uses Ruby code in tags. You need to know a small bit of Ruby to read it, but it works with all Puppet versions.

Puppet templates generally use data taken from Puppet variables. Templates are files that are pre-processed, some values gets replaced with variables. In this case, the file currently includes the values of three facts. We will be adding a new fact in this file now to add logging of the network interfaces:

```
Machine Information
-------------------
Disks: <%= @disks %>
Memory: <%= @memory %>
Processors: <%= @processors %>
Network Interfaces: <%= @interfaces %>
}
```

Run the following to check if everything worked correctly:

```
sudo puppet agent -v --test
cat /tmp/machine_info.txt
```

## Reboot machine

For the last exercise, we will be creating a new module named reboot, that checks if a node has been online for more than 30 days. If so, then reboot the computer.

Our first step is to create a directory to hold the new reboot module:
```
sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
```

The way to reboot a computer depends on the OS that it's running. So, you'll set a variable that has one of the following reboot commands, based on the kernel fact:

* shutdown /r on windows
* shutdown -r now on Darwin (macOS)
* reboot on Linux.

Inside this directory, create a file called `init.pp` and add the following content:

```
class reboot {
  if $facts[kernel] == "windows" {
    $cmd = "shutdown /r"
  } elsif $facts[kernel] == "Darwin" {
    $cmd = "shutdown -r now"
  } else {
    $cmd = "reboot"
  }
  if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
     }
   }
}
```

Finally, to get this module executed, make sure to include it in the site.pp file:
`/etc/puppet/code/environments/production/manifests/site.pp`

Let's add a line to include the reboot module:

```
node default {
   class { 'packages': }
   class { 'machine_info': }
   class { 'reboot': }
}
```
...and then run the client on linux-instance:
```
sudo puppet agent -v --test
```

This completes this project.
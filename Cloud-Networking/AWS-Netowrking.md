# AWS Networking

## Overview
This document provides an overview of key AWS networking concepts and services that are essential for building and managing networks in the cloud.

Overview: Brief introduction to the document.
* Key Networking Services: Detailed explanations of important AWS networking services:
* Virtual Private Cloud (VPC)
* Subnets
* Internet Gateway
* NAT Gateway
* AWS Transit Gateway
* VPC Peering
* AWS PrivateLink
* Route 530
* Elastic Load Balancing (ELB)
* AWS Global Accelerator
* AWS Shield
* AWS Firewall Manager
* AWS Network Manager
* Service Quotas

## Key Networking Services

### 1. Virtual Private Cloud (VPC)
- **Definition**: A service that allows you to create a private network within AWS.
- **Features**:
  - Define your own IP address range.
  - Create subnets and configure route tables and network gateways.
  - Control access to your VPC resources through security groups and network ACLs.

### 2. Subnets
- **Definition**: Segments of your VPC's IP address range where you can place groups of isolated resources.
- **Types**:
  - **Public Subnet**: A subnet that is accessible from the internet.
  - **Private Subnet**: A subnet that is not accessible from the internet.
- **Usage**: Organize resources based on their accessibility requirements.

### 3. Internet Gateway
- **Definition**: A horizontally scaled, redundant, and highly available VPC component.
- **Function**: Allows communication between instances in your VPC and the internet.

### 4. NAT Gateway
- **Definition**: Allows instances in a private subnet to connect to the internet while preventing the internet from initiating connections with those instances.
- **Use Case**: Enable software updates or access to external services from private instances.

### 5. AWS Transit Gateway
- **Definition**: A service that enables you to connect multiple VPCs and on-premises networks through a central hub.
- **Benefits**: Simplifies network architecture and management across multiple VPCs.

### 6. VPC Peering
- **Definition**: A method to connect two VPCs privately using the AWS backbone network.
- **Use Case**: Allow resources in different VPCs to communicate with each other as if they were in the same network.

### 7. AWS PrivateLink
- **Definition**: Provides private connectivity between VPCs and services hosted on AWS, without exposing your traffic to the public internet.
- **Use Case**: Securely connect to third-party services and applications.

### 8. Route 53
- **Definition**: AWS's scalable Domain Name System (DNS) web service.
- **Features**:
  - Domain registration and DNS management.
  - Health checking and routing end-user requests to optimal endpoints.

### 9. Elastic Load Balancing (ELB)
- **Definition**: Distributes incoming application traffic across multiple targets (EC2 instances, containers, etc.).
- **Benefits**:
  - Provides high availability and fault tolerance.
  - Automatically scales to handle varying traffic loads.

### 10. AWS Global Accelerator
- **Definition**: A service that improves the availability and performance of your applications for global users.
- **Function**: Routes user traffic to optimal endpoints over the AWS global network.

### 11. AWS Shield
- **Definition**: A managed DDoS protection service to safeguard applications running on AWS.
- **Benefits**:
  - Provides protection against common network and application layer attacks.

### 12. AWS Firewall Manager
- **Definition**: A security management service that allows you to centrally configure and manage firewall rules across your accounts and applications in AWS.
- **Use Case**: Simplifies security management and compliance across multiple AWS accounts.

### 13. AWS Network Manager
- **Definition**: Provides a global view of your network across AWS and on-premises locations.
- **Benefits**:
  - Simplifies monitoring and management of your network resources.

### 14. Service Quotas
- **Definition**: Understanding service limits related to networking, such as the number of VPCs, security groups, and network interfaces per region.
- **Importance**: Helps in planning and scaling your AWS infrastructure efficiently.

## Conclusion
This document serves as a foundational guide to AWS networking concepts and services. For further information, refer to the [official AWS documentation](https://aws.amazon.com/documentation/).


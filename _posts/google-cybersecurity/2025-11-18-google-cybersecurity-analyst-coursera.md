---
categories:

    - cs
    - cybersecurity

description: My notes from the google cybersecurity analyst certification on coursera.
title: Course - Google Cybersecurity Analyst Certification on Coursera
---

# Course 1: Foundations of Cybersecurity

## Module 1: Welcome to the exciting world of cybersecurity

1. Responsibilities of an entry-level cybersecurity analyst

    1. Protecting computer and network systems

    1. Installing prevention software on systems

    1. Possibly work with dev teams to improve product security

    1. Conducting periodic security audits. 

1. Nikki: A day in the life of a security engineer

    1. Common tasks in day of entry level cybersecurity professional

        1. Operations

            Responding to deteections and doing investigations. 

        1. Projects

            Working with other teams to build new detections or improve current detections. 

    1. Cybersecurity analyst v/s Cybersecurity engineer

        1. Analyst focus on operations.
        1. Engineer can do both operations and projects. 

1. Core skills for cybersecurity professionals

    1. Technical skills for Cybersecurity analyst

        1. Programming languages

        1. Security Information and Event Management (SIEM) tools

        1. Computer Forensics

## Module 2: The evolution of cybersecurity

1. Past cybersecurity attacks

    1. Malware and Viruses

        1. Malware
        
            Malware (short for malicious software) is a broad category of any software deliberately designed to damage, disrupt, or gain unauthorized access to a computer system.

        1. Virus

            Malicious code written to interfere with computer operations and cause damage to data and software. <ins>Computer virus is a specific type of malware</ins> that attaches itself to other programs or files and replicates in order to spread.

    1. CERT (Computer Emergency Response Teams) and CSIRT (Computer Security Incident Response Teams)

1. Attacks in the digital age

    1. Social engineering

        A manipulation technique that exploits human error to gain private information, access or valuables. 

    1. Phishing

        The use of digital communications to trick people into revealing sensitive data or deploying malicious software. 

    1. PII and SPII

        1. PII (Personally identifiable information)

            Data like Names, Date of births, Emails etc. In short, any data that can be used to identify a person. 

        1. SPII (Sensitive personally identifiable information)

            Data like bank accounts, credit card numbers, biometric data etc. 

1. Common attacks and their effectiveness

    1. Malware (Malicious software)

        Commong types of malware attacks include: 

        1. Viruses:

            Malicious code written to interfere with computer operations and cause damage to data and software. A virus needs to be initiated by a user (i.e., a threat actor), who transmits the virus via a malicious attachment or file download. When someone opens the malicious attachment or download, the virus hides itself in other files in the now infected system. When the infected files are opened, it allows the virus to insert its own code to damage and/or destroy data in the system.

        1. Worms:

            Self replicating malware that duplicates itself across systems on its own. In contrast to a virus, a worm does not need to be downloaded by a user.

        1. Ransomeware:

            Encrypts organization data and demands payment to restore access. 

        1. Spyware

    1. Social engineering

        A manipulation technique that exploits human error to gain unauthorized access to sensitive, private, and/or valuable data.

        1. Phishing

            Some common types of phishing attack are: 

            1. Business Email Compromise (BEC)

            1. Spear phishing: 
            
                A malicious email attack that targets a specific user or group of users. The email seems to originate from a trusted source.

                1. Whaling:

                    Form of spear phishing. Threat actors target company executives to gain access to sensitive data. 

            1. Vishing: Voice phishing

            1. Smishing: Sms phishing. 

            1. Social media phishing:

                Threat actor collects data from social media and then initiates attack.

        1. Watering hole attack:

            Threat actor attacks a website frequented by specific group of users. 

        1. USB baiting:

            Threat actor leaves around an unattended USB for someone to find it and plug in to their systems. The victim's system (and the network) gets infected with virus. 

        1. Physical social engineering:

            A threat actor impersonates an employee, customer, or vendor to obtain unauthorized access to a physical location.
        
1. Introduction to the eight CISSP security domains, Part 1

    CISSP divides the tasks a security professional does into 8 domains. They sometimes might overlap but in general, these 8 categories refer to 8 career paths. 

    1. Security and risk management

        - Set policies
        - Compliance

    1. Asset security

        - Protecting digital and physical assets. 
        - Old equipment properly disposed off. 

    1. Security architecture and engineering

        - Ensure data security by using effective tools and systems. 

        - Eg: Configuring firewalls

    1. Communication and network security

        - Secure physical networks and wireless communications.

1. Introduction to the eight CISSP security domains, Part 2

    1. Identity and access management

        - Ensuring authorized user access.

        - eg: Setting up employee key card access

    1. Security assessment and testing

        - Conducting security audits.

        - eg: Audits of user permissions. 

    1. Security operations

        - Implement preventative measures. 

    1. Software development security

        - Secure coding


## Module 3: Protect against threats, risks, and vulnerabilities

1. Introduction to security frameworks and controls

    1. Security frameworks
    
        Guidelines used for building plans to help mitigate risk and threats to data and privacy. 

1. Secure design

    1. CIA (Confidentiality, Integrity and Availability) triad

        - It is a foundational cybersecurity model that helps inform how organizations consider risk.

    1. NIST Cybersecurity Framework (CSF)

        - A voluntary framework consisting of best practice to manage security risks. 

1. Controls, frameworks, and compliance

    1. Security lifecycle

        A security lifecycle is a constantly evolving set of policies and standards.

    1. Security control

        Safeguards designed to reduce **specific** security risks.
    
    1. Security frameworks

        Guidelines used for building plans to help mitigate risks and threats to data and privacy.

1. Glossary terms from module 3

    1. Protected health information (PHI)

        Data relating to health condition of patients. 

## Module 4: Cybersecurity tools and programming languages

1. Common cybersecurity tools

    1. SIEM 

        An app that collects and analyzes log data to monitor critical activities in an organization. 

        Eg: Splunk, Google Chronicle

    1. Playbook

        Manual that provides details about any operational action. Eg: How to deal with a security breach before, during and after it. Playbooks can also be created for compliance. 

    1. Network protocol analyzer (Packet sniffer)

        Captures and analyzes data traffic within a network. 

# Course 2: Play It Safe: Manage Security Risks

## Module 1: Security domains

1. Explore the CISSP security domains, Part 1

    <a id="cissp_domains"></a>

    ![CISSP domains part 1]({%link assets/images/posts/google-cybersecurity/CISSP_domains_part1.png%})

    1. Security posture

        Org's ability to manage its defense of critical assets and data, and react to change. 

    1. Domains

        1. Security and risk management

            - Defining security goals and objectives

            - Risk mitigation: Reduce impact of a breach

            - Compliance

            - Business continuity: Establish risk disaster recovery plans. 

            - Legal regulations

            - Infosec

                - Incident response

                - Vulnerability management

                - Application security

                - Cloud security

                - Infrastructure security

        1. Asset security

            - Securing digital and physical assets. 

                Includes PII, SPII. 

            - Storage, maintanence, retention and destruction of data. 

        1. Security Architecture and Engineering

            - Optimizing data security by ensuring effective tools, systems and processes are in place. 

            Eg: Shared responsibility (All individuals within org responsible for lowering risk and maintaining security).

        1. Communication and network security

            - Securing physical networks and wireless communications. 

1. Explore the CISSP security domains, Part 2

    1. Identity and access management (IAM)

        - Access and authorization to keep data secure
        
        - Components

            - Identification

            - Authentication

            - Authorization

            - Accountability

    1. Security assessment and testing

        - Security control testing

            Evaluate org policies.

        - Collecting and analyzing data
        
        - Conducting security audits to monitor for risks, threats and vulnerabilities. 

    1. Security operations

        - Conducting investigations and implementing preventative measures. 

        - Occurs once a threat has been identified. 

        - Includes digital forensics. 

    1. Software development security

        - Secure coding practices

1. 
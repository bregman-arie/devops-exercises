# Security

<details>
<summary>What is DevSecOps? What its core principals?</summary><br><b>

A couple of quotations from chosen companies:

[Snyk](https://snyk.io/series/devsecops): "DevSecOps refers to the integration of security practices into a DevOps software delivery model. Its foundation is a culture where development and operations are enabled through process and tooling to take part in a shared responsibility for delivering secure software."

[Red Hat](https://www.redhat.com/en/topics/devops/what-is-devsecops): "DevSecOps stands for development, security, and operations. It's an approach to culture, automation, and platform design that integrates security as a shared responsibility throughout the entire IT lifecycle."

[Jfrog](https://jfrog.com/devops-tools/what-is-devsecops): "DevSecOps principles and practices parallel those of traditional DevOps with integrated and multidisciplinary teams, working together to enable secure continuous software delivery. The DevSecOps development lifecycle is a repetitive process that starts with a developer writing code, a build being triggered, the software package deployed to a production environment and monitored for issues identified in the runtime but includes security at each of these stages."
</b></details>

<details>
<summary>What the "Zero Trust" concept means? How Organizations deal with it?</summary><br><b>

[Codefresh definition](https://codefresh.io/security-testing/codefresh-runner-overview): "Zero trust is a security concept that is centered around the idea that organizations should never trust anyone or anything that does not originate from their domains. Organizations seeking zero trust automatically assume that any external services it commissions have security breaches and may leak sensitive information"
</b></details>

<details>
<summary>Explain the principle of least privilege</summary><br><b>

The principle of least privilege refers to the practice of providing minimal permissions to users, roles, and service accounts that allow them to perform their functions. If an entity does not require an access right then it should not have that right.
</b></details>

<details>
<summary>What it means to be "FIPS compliant"?</summary><br><b>
</b></details>

<details>
<summary>What is a Certificate Authority?</summary><br><b>
 
 [wikipedia](https://en.wikipedia.org/wiki/Certificate_authority) : A certificate Authority that stores, singns and issues certificates.
 
 A certificate certifies the authenticity of the public key delivered by the website. It prevents [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks by providing a lot of information which identifie the public key. Importante information provided inside a [X.509](https://www.ssl.com/faqs/what-is-an-x-509-certificate/) certificate are like :
  * Version Number
  * Serial Number
  * Signature Algorithm ID
  * Issuer Name 
  * Validity period
  * Subject name
  * Subject Public Key info
 
Every certificates must be signed by a trusted authority, a certificate chain is a concatenation of mutilple certificates signed by a more trusted authority from the one delivered by the website to the root Certificate Authority (CA). The root Certificate Authority is the top most trusted authority and every browsers embark their certificate natively.
 
</b></details>

<details>
<summary>Explain RBAC (Role-based Access Control)</summary><br><b>

Access control based on user roles (i.e., a collection of access authorizations a user receives based on an explicit or implicit assumption of a given role). Role permissions may be inherited through a role hierarchy and typically reflect the permissions needed to perform defined functions within an organization. A given role may apply to a single individual or to several individuals.

- RBAC mapped to job function, assumes that a person will take on different roles, overtime, within an organization and different responsibilities in relation to IT systems.
</b></details>

#### Security - Authentication and Authorization

<details>
<summary>Explain Authentication and Authorization</summary><br><b>

Authentication is the process of identifying whether a service or a person is who they claim to be.
Authorization is the process of identifying what level of access the service or the person have (after authentication was done)
</b></details>

<details>
<summary>What authentication methods are there?</summary><br><b>
</b></details>

<details>
<summary>Give an example of basic authentication process</summary><br><b>

A user uses the browser to authenticate to some server. It does so by using the authorization field which is constructed from the username and the password combined with a single colon. The result string is encoded using a certain character set which is compatible with US-ASCII. The authorization method + a space is prepended to the encoded string.
</b></details>

<details>
<summary>What are the three primary factors of authentication? Give three examples of each</summary><br><b>

Something you have
- Smart card
- Physical authentication device
- Software token

Something you know
- Password
- PIN
- Passphrase

Something you are
- Fingerprint
- Iris or retina scan
- Gait analysis
</b></details>

<details>
<summary>Explain Token-based authentication</summary><br><b>
</b></details>

<details>
<summary>Explain Risk-based authentication</summary><br><b>
</b></details>

<details>
<summary>Explain what is Single Sign-On</summary><br><b>

SSO (Single Sign-on), is a method of access control that enables a user to log in once and gain access to the resources of multiple software systems without being prompted to log in again.
</b></details>

<details>
<summary>Explain how the Kerberos authentication protocol works as a SSO solution</summary><br><b>

Kerberos works as a SSO solution by only requiring the user to sign in using their credentials once within a specific validity time window. Kerberos authentication grants the user a Ticket Granting Ticket (TGT) from a trusted authentication server which can then be used to request service tickets for accessing various services and resources. By passing around this encrypted TGT instead of credentials, the user does not need to sign-in multiple times for each resource that has been integrated with Kerberos.
</b></details>

<details>
<summary>Does Kerberos make use of symmetric encryption, asymmetric encryption, both, or neither?</summary><br><b>

Symmetric Encryption - Kerberos uses exclusively symmetric encryption with pre-shared keys for transmitting encrypted information and authorizing users.
</b></details>

<details>
<summary>Explain MFA (Multi-Factor Authentication)</summary><br><b>

Multi-Factor Authentication (Also known as 2FA). Allows the user to present two pieces of evidence, credentials, when logging into an account.

- The credentials fall into any of these three categories: something you know (like a password or PIN), something you have (like a smart card), or something you are (like your fingerprint).  Credentials must come from two different categories to enhance security.
</b></details>

<details>
<summary>Explain OAuth</summary><br><b>
</b></details>

#### Security - Passwords

<details>
<summary>How do you manage sensitive information (like passwords) in different tools and platforms?</summary><br><b>
</b></details>

<details>
<summary>What password attacks are you familiar with?</summary><br><b>

  * Dictionary
  * Brute force
  * Password Spraying
  * Social Engineering
    * Whaling
    * Vishing
    * Phising
    * Whaling
</b></details>

<details>
<summary>How to mitigate password attacks?</summary><br><b>

  * Strong password policy
  * Do not reuse passwords
  * ReCaptcha
  * Training personnel against Social Engineering
  * Risk Based Authentication
  * Rate limiting
  * MFA
</b></details>

<details>
<summary>What is password salting? What attack does it help to deter?</summary><br><b>

Password salting is the processing of prepending or appending a series of characters to a user's password before hashing this new combined value. This value should be different for every single user but the same salt should be applied to the same user password every time it is validated.

 This ensures that users that have the same password will still have very different hash values stored in the password database. This process specifically helps deter rainbow table attacks since a new rainbow table would need to be computed for every single user in the database.
</b></details>

#### Security - Cookies

<details>
<summary>What are cookies? Explain cookie-based authentication</summary><br><b>
</b></details>

<details>
<summary>True or False? Cookie-based authentication is stateful</summary><br><b>

True. Cookie-based authentication session must be kept on both server and client-side.
</b></details>

<details>
<summary>Explain the flow of using cookies</summary><br><b>

1. User enters credentials
2. The server verifies the credentials -> a sessions is created and stored in the database
3. A cookie with the session ID is set in the browser of that user
4. On every request, the session ID is verified against the database
5. The session is destroyed (both on client-side and server-side) when the user logs out
</b></details>

#### Security - SSH

<details>
<summary>What is SSH how does it work?</summary><br><b>

[Wikipedia Definition](https://en.wikipedia.org/wiki/SSH_(Secure_Shell)): "SSH or Secure Shell is a cryptographic network protocol for operating network services securely over an unsecured network."

[Hostinger.com Definition](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work): "SSH, or Secure Shell, is a remote administration protocol that allows users to control and modify their remote servers over the Internet."

[This site](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work) explains it in a good way.
</b></details>

<details>
<summary>What is the role of an SSH key?</summary><br><b>
 
[Wikipedia definition](https://en.wikipedia.org/wiki/Secure_Shell) : SSH uses public-key cryptography to authenticate the remote computer and allow it to authenticate the user. Two keys are created, private is stored inside user's computer to decrypt the communication then the public key is stored inside the remoted computer where user want to connect with and it is used to encrypt the communication.
 
</b></details>

#### Security - Cryptography

<details>
<summary>Explain Symmetrical encryption</summary><br><b>

A symmetric encryption is any technique where a key is used to both encrypt and decrypt the data/entire communication.
</b></details>

<details>
<summary>Explain Asymmetrical encryption</summary><br><b>

A asymmetric encryption is any technique where the there is two different keys that are used for encryption and decryption, these keys are known as public key and private key.
</b></details>

<details>
<summary>What is "Key Exchange" (or "key establishment") in cryptography?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Key_exchange): "Key exchange (also key establishment) is a method in cryptography by which cryptographic keys are exchanged between two parties, allowing use of a cryptographic algorithm."
</b></details>

<details>
<summary>True or False? The symmetrical encryption is making use of public and private keys where the private key is used to decrypt the data encrypted with a public key</summary><br><b>

False. This description fits the asymmetrical encryption.
</b></details>

<details>
<summary>True or False? The private key can be mathematically computed from a public key</summary><br><b>
False.
</b></details>

<details>
<summary>True or False? In the case of SSH, asymmetrical encryption is not used to the entire SSH session</summary><br><b>

True. It is only used during the key exchange algorithm of symmetric encryption.
</b></details>

<details>
<summary>What is Hashing?</summary><br><b>

Hashing is a mathematical function for mapping data of arbitrary sizes to fixed-size values. This function produces a "digest" of the data that can be used for verifying that the data has not been modified (amongst other uses)
</b></details>

<details>
<summary>How is hashing different from encryption?</summary><br><b>

Encrypted data can be decrypted to its original value. Hashed data cannot be reversed to view the original data - hashing is a one-way function.
</b></details>

<details>
<summary>How hashes are part of SSH?</summary><br><b>

Hashes used in SSH to verify the authenticity of messages and to verify that nothing tampered with the data received.
</b></details>

#### Security - Attacks, Threats, and Vulnerabilities
<details>
<summary>Explain the following:

  * Vulnerability
  * Exploits
  * Risk
  * Threat</summary><br><b>
</b></details>

<details>
<summary>Are you familiar with "OWASP top 10"?</summary><br><b>

Read about it [here](https://owasp.org/www-project-top-ten)
</b></details>

<details>
<summary>What is XSS?</summary><br><b>

Cross Site Scripting (XSS) is an type of a attack when the attacker inserts browser executable code within a HTTP response. Now the injected attack is not stored in the web application, it will only affect the users who open the maliciously crafted link or third-party web page. A successful attack allows the attacker to access any cookies, session tokens, or other sensitive information retained by the browser and used with that site 

You can test by detecting user-defined variables and how to input them. This includes hidden or non-obvious inputs such as HTTP parameters, POST data, hidden form field values, and predefined radio or selection values. You then analyze each found vector to see if their are potential vulnerabilities, then when found you craft input data with each input vector. Then you test the crafted input and see if it works.
</b></details>

<details>
<summary>What is an SQL injection? How to manage it?</summary><br><b>

SQL injection is an attack consists of inserts either a partial or full SQL query through data input from the browser to the web application. When a successful SQL injection happens it will allow the attacker to read sensitive information stored on the database for the web application. 

You can test by using a stored procedure, so the application must be sanitize the user input to get rid of the risk of code injection. If not then the user could enter bad SQL, that will then be executed within the procedure
</b></details>

<details>
<summary>What is Certification Authority?</summary><br><b>
</b></details>

<details>
<summary>How do you identify and manage vulnerabilities?</summary><br><b>
</b></details>

<details>
<summary>Explain "Privilege Restriction"</summary><br><b>
</b></details>

<details>
<summary>How HTTPS is different from HTTP?</summary><br><b>
The 'S' in HTTPS stands for 'secure'. HTTPS uses TLS to provide encryption of HTTP requests and responses, as well as providing verifaction by digitally signing requests and responses. As a result, HTTPS is far more secure than HTTP and is used by default for most modern websites.
</b></details>

<details>
<summary>What types of firewalls are there?</summary><br><b>
</b></details>

<details>
<summary>What is DDoS attack? How do you deal with it?</summary><br><b>
</b></details>

<details>
<summary>What is port scanning? When is it used?</summary><br><b>
</b></details>

<details>
<summary>What is the difference between asynchronous and synchronous encryption?</summary><br><b>
</b></details>

<details>
<summary>Explain Man-in-the-middle attack</summary><br><b>
</b></details>

<details>
<summary>Explain CVE and CVSS</summary><br><b>
 
  [Red Hat](https://www.redhat.com/en/topics/security/what-is-cve#how-does-it-work) : "When someone refers to a CVE (Common Vulnerabilities and Exposures), they mean a security flaw that's been assigned a CVE ID number. They don’t include technical data, or information about risks, impacts, and fixes." So CVE is just identified by an ID written with 8 digits. The CVE ID have the following format:  CVE prefix + Year + Arbitrary Digits.
 Anyone can submit a vulnerability, [Exploit Database](https://www.exploit-db.com/submit) explains how it works to submit.
  
Then CVSS stands for Common Vulnerability Scoring System, it attempts to assign severity scores to vulnerabilities, allowing to ordonnance and prioritize responses and resources according to threat. 
 
</b></details>

<details>
<summary>What is ARP Poisoning?</summary><br><b>
</b></details>

<details>
<summary>Describe how do you secure public repositories</summary><br><b>
</b></details>

<details>
<summary>What is DNS Spoofing? How to prevent it?</summary><br><b>

DNS spoofing occurs when a particular DNS server’s records of “spoofed” or altered maliciously to redirect traffic to the attacker. This redirection of traffic allows the attacker to spread malware, steal data, etc.

**Prevention**
- Use encrypted data transfer protocols - Using end-to-end encryption vian SSL/TLS will help decrease the chance that a website / its visitors are compromised by DNS spoofing.
- Use DNSSEC - DNSSEC, or Domain Name System Security Extensions, uses digitally signed DNS records to help determine data authenticity.
- Implement DNS spoofing detection mechanisms - it’s important to implement DNS spoofing detection software. Products such as XArp help product against ARP cache poisoning by inspecting the data that comes through before transmitting it.
</b></details>

<details>
<summary>What can you tell me about Stuxnet?</summary><br><b>

Stuxnet is a computer worm that was originally aimed at Iran’s nuclear facilities and has since mutated and spread to other industrial and energy-producing facilities. The original Stuxnet malware attack targeted the programmable logic controllers (PLCs) used to automate machine processes. It generated a flurry of media attention after it was discovered in 2010 because it was the first known virus to be capable of crippling hardware and because it appeared to have been created by the U.S. National Security Agency, the CIA, and Israeli intelligence.
</b></details>

<details>
<summary>What can you tell me about the BootHole vulnerability?</summary><br><b>
</b></details>

<details>
<summary>What can you tell me about Spectre?</summary><br><b>

Spectre is an attack method which allows a hacker to “read over the shoulder” of a program it does not have access to. Using code, the hacker forces the program to pull up its encryption key allowing full access to the program
</b></details>

<details>
<summary>Explain "Format String Vulnerability"</summary><br><b>
</b></details>


<details>
<summary>Explain DMZ</summary><br><b>
</b></details>

<details>
<summary>Explain TLS</summary><br><b>
</b></details>

<details>
<summary>What is CSRF? How to handle CSRF?</summary><br><b>

Cross-Site Request Forgery (CSRF) is an attack that makes the end user to initiate a unwanted action on the web application in which the user has a authenticated session, the attacker may user an email and force the end user to click on the link and that then execute malicious actions. When an CSRF attack is successful it will compromise the end user data 

You can use OWASP ZAP to analyze a "request", and if it appears that there no protection against cross-site request forgery when the Security Level is set to 0 (the value of csrf-token is SecurityIsDisabled.) One can use data from this request to prepare a CSRF attack by using OWASP ZAP
</b></details>

<details>
<summary>Explain HTTP Header Injection vulnerability</summary><br><b>

HTTP Header Injection vulnerabilities occur when user input is insecurely included within server responses headers. If an attacker can inject newline characters into the header, then they can inject new HTTP headers and also, by injecting an empty line, break out of the headers into the message body and write arbitrary content into the application's response.
</b></details>

<details>
<summary>What security sources are you using to keep updated on latest news?</summary><br><b>
</b></details>

<details>
<summary>What TCP and UDP vulnerabilities are you familiar with?</summary><br><b>
</b></details>

<details>
<summary>Do using VLANs contribute to network security?</summary><br><b>
</b></details>

<details>
<summary>What are some examples of security architecture requirements?</summary><br><b>
</b></details>

<details>
<summary>What is air-gapped network (or air-gapped environment)? What its advantages and disadvantages?</summary><br><b>
</b></details>

<details>
<summary>Explain what is Buffer Overflow</summary><br><b>

A buffer overflow (or buffer overrun) occurs when the volume of data exceeds the storage capacity of the memory buffer. As a result, the program attempting to write the data to the buffer overwrites adjacent memory locations.
</b></details>

<details>
<summary>What is Nonce?</summary><br><b>
</b></details>

<details>
<summary>What is SSRF?</summary><br><b>

SSRF (Server-side request forgery) it's a vulnerability where you can make a server make arbitrary requests to anywhere you want.

Read more about it at [portswigger.net](https://portswigger.net/web-security/ssrf)
</b></details>

<details>
<summary>Explain MAC flooding attack</summary><br><b>

MAC address flooding attack (CAM table flooding attack) is a type of network attack where an attacker connected to a switch port floods the switch interface with very large number of Ethernet frames with different fake source MAC address.
</b></details>

<details>
<summary>What is port flooding?</summary><br><b>
</b></details>

<details>
<summary>What is "Diffie-Hellman key exchange" and how does it work?</summary><br><b>

Have you heard of [The Two General's Problem](https://en.wikipedia.org/wiki/Two_Generals%27_Problem)? The Diffie-Hellman key exchange is a solution to this problem to allow for the secure exchange of cryptographic keys over an encrypted channel.

It works using public/private key pairs (asymmetric encryption). Two parties that wish to communicate securely over a public channel will each generate a public/private key pair and distribute the public key to the other party (note that public keys are free to be exchanged over a public channel). From here, each party can derive a shared key using a combination of their personal private key and the public key of the other party. This combined key can now be used as a symmetric encryption key for communications.
</b></details>

<details>
<summary>Explain "Forward Secrecy"</summary><br><b>
</b></details>

<details>
<summary>What is Cache Poisoned Denial of Service?</summary><br><b>

CPDoS or Cache Poisoned Denial of Service. It poisons the CDN cache. By manipulating certain header requests, the attacker forces the origin server to return a Bad Request error which is stored in the CDN’s cache. Thus, every request that comes after the attack will get an error page.
</b></details>

<details>
<summary>What is the difference if any between SSL and TLS?</summary><br><b>
</b></details>

<details>
<summary>What's SSL termination (or SSL offloading)?</summary><br><b>

SSL termination is the process of decrypting encrypted traffic. The advantage in SSL termination is that the server doesn't have to perform it, we can use SSL termination to reduce the load on the server, speed up some processes, and allow the server to focus on its core functionality (e.g. deliver content)
</b></details>

<details>
<summary>What is SNI (Server Name Indication)?</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Server_Name_Indication): "an extension to the Transport Layer Security (TLS) computer networking protocol by which a client indicates which hostname it is attempting to connect to at the start of the handshaking process"
</b></details>

<details>
<summary>What benefits SNI introduces?</summary><br><b>

SNI allows a single server to serve multiple certificates using the same IP and port.<br>
Practically this means that a single IP can server multiple web services/pages, each using a different certificate.
</b></details>

<details>
<summary>Explain "Web Cache Deception Attach"</summary><br><b>

[This blog post](https://omergil.blogspot.com/2017/02/web-cache-deception-attack.html) explains it in detail.
</b></details>

#### Security - Threats

<details>
<summary>Explain "Advanced persistent threat (APT)"</summary><br><b>
</b></details>

<details>
<summary>What is a "Backdoor" in information security?</summary><br><b>
</b></details>

#### Software Supply Chain & Security 

<details>
<summary>Briefly describe what a software supply chain is. </summary><br><b>

A company’s software supply chain consists of any third party or open source component which could be used to compromise the final product. Such component is usually an API provided by an actor. For instance Twilio who offers mobile communication APIs to their customers. 

[WhiteSource](https://www.whitesourcesoftware.com/resources/blog/software-supply-chain-security-the-basics-and-four-critical-best-practices/): "Enterprise software projects increasingly depend on third-party and open source components. These components are created and maintained by individuals who are not employed by the organization developing the primary software, and who do not necessarily use the same security policies as the organization. This poses a security risk, because differences or inconsistencies between these policies can create overlooked areas of vulnerability that attackers seek to exploit." 
</b></details>

<details>
<summary>What're some benefits of a software supply chain? </summary><br><b>

[Increment](https://increment.com/apis/apis-supply-chain-software/): Resource-saving. Using and paying for existing solutions to resource-heavy problems saves time as well as money. Hence resulting in efficient, cheap and greater opportunities to develop and deploy software products for consumers. 
</b></details>

<details>
<summary> Give three examples of three potential security threats related to the software supply chain and describe them.</summary><br><b>

[IEEE](https://ieeexplore.ieee.org/abstract/document/9203862): 

  * Sensitive data being exposed or lost.
    * In a software supply chain, sensitive data may be passed throughout the chain. Security threats involve loss or exposure of this data, such as customer credit card details.
  * Cloud technology.
    * Data sharing in the cloud might jeopardize the privacy of the data within the chain.
  * Third-party vendors.
    * Third-party vendors’ code solutions might not provide sufficient cybersecurity and risk being a potential subject to data breaches.
</b></details>

#### Package management & Security 

<details>
<summary> What is a package manager?
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): "A tool that allows you to easily download, add and thus reuse programming libraries in your project." E.g. npm or yarn.
</b></details>

<details>
<summary> What is a build tool?
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): "A tool that fetches the packages (dependencies) that are required to compile, test and deploy your application." 
</b></details>

<details>
<summary> Describe bloated dependencies.
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): 
An application usually has different dependencies. Typically, not all of them are required for building and running the application. Bloated dependencies is the concept of including the unnecessary dependencies for building and running your application. 
</b></details>

<details>
<summary> Explain a few cons of bloated dependencies.
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): 

  * Challenging to manage.
  * Decreases performance of the application.
  * Risk for malicious code that a threathening actor can take advantage of. 
</b></details>

<details>
<summary> What solutions are there for managing project dependencies?
</summary><br><b>

[Npm.js documentation](https://docs.npmjs.com/cli/v8/commands/npm-prune): Use clean-up commands that are usually provided by the package manager authors. For instance, npm prune will remove any extraneous package. Another command is npm audit which will scan your repository and report any vulnerable dependencies found.
</b></details>

<details>
<summary> What is a threatening actor and how can this actor take advantage of open source or third party vendor's packages/libraries? 
</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Threat_actor): A threatening actor is one or more people who target technical artifacts such as software, networks and/or devices with the purpose of harming it.

[Aquasec](https://www.aquasec.com/cloud-native-academy/devsecops/supply-chain-security/): An attacking actor may identify, target and inject malicious software in a vulnerable part of an open source package or a third party vendor’s code. The consumer of this code may consequently and unknowingly deploy the malicious code throughout their pipelines, thus infecting their own projects. An example of this happening is the hack of [SolarWinds](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack).
</b></details>

<details>
<summary> How can you make sure that you use trustworthy packages for your project?
</summary><br><b>

You can’t. You will always be exposed to security risk once you start using open source or vendor packages. The goal is to minimize the risk in order to avoid security breaches. This could be done by:

  * Regularly update the project's dependencies to apply latest bug fixes and vulnerability clean-ups.
  * However, unless you trust the author, do not update your dependencies instantly, since package updates recently have been a common target by hackers.
  * Check for changes of the file content in previous versions. 
</b></details>

<details>
<summary> Explain checksum.
</summary><br><b>

[Fred Cohen (permission needed)](https://reader.elsevier.com/reader/sd/pii/0167404887900319?token=D5339ABC064AD9A2B50B74D8CE890B0E22A302A0BC461A50078D407BEA01052737DC6AAEF95A854E72A73B6D0C67E260&originRegion=eu-west-1&originCreation=20220502180611): Checksum is a way to verify the integrity of information in systems with no built-in protection. In other words, it provides a way of validating that the content of a file or a package / library is intact. This is useful since attacks or errors may occur during transmission of files. However, it requires that the package author has run a checksum function for the file / package which creates a specific hash for that version of the file. A minor change of the file content will result in a different checksum. If you have access to the original checksum of the file, you may run checksum on your own. In case the resulting checksum matches the original one, no changes have been made in the file. You can now conclude that no error or malicious injection was done during transmission of the file. 
</b></details>

## Microsegmentation

<details>
<summary>What is Microsegmentation?</summary><br><b>

- Security method
- Managing network access between endpoints (processes, devices, instances)
- A method in which security policies are applied to limit traffic
  - based on concepts such as "Zero Trust" and "Least Privileged"
- The result of Microsegmentation should be:
  - Reduced attack ability
  - Better breach containment
</b></details>

<details>
<summary>Why do we need Microsegmentation solutions? Why using something such as firewalls isn't enough?</summary><br><b>

- Firewalls focused on north-south traffic. Basically traffic that is outside of the company perimeter
- Traffic that is considered west-east, internal workflows and communication, is usually left untreated
</b></details>

<details>
<summary>How Microsegmentation is applied?</summary><br><b>

 There are different ways to apply Microsegmentation:

- Cloud Native: Using cloud embedded capabilities such as security groups, firewalls, etc.
- Agent: Agents running on the different endpoints (instances, services, etc.)
- Network: Modify network devices and their configuration to create microsegmentation 

</b></details>

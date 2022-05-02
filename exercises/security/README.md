## Security

<details>
<summary>What is DevSecOps? What its core principals?</summary><br><b>

[Devopsonline definition](https://www.devopsonline.co.uk/how-to-put-the-sec-in-your-devsecops/): DevSecOps is the process of incorporating security into the development process. It includes the process of assessing and addressing potential threats and hardening attack surfaces, and commonly includes: penetration testing, code scanning and analysis, threat modeling and vulnerability assessments, compliance auditing, and all of the associated training that these require. The core principles are:

  * deliver small, frequent releases using agile methodologies
  * wherever possible, make use of automated testing
  * empower developers to influence security changes
  * ensure you are in a continuous state of compliance
  * be prepared for threats, always invest in advanced training for your engineers.
</b></details>

<details>
<summary>What the "Zero Trust" concept means? How Organizations deal with it?</summary><br><b>

[Codefresh definition](https://codefresh.io/security-testing/codefresh-runner-overview): "Zero trust is a security concept that is centered around the idea that organizations should never trust anyone or anything that does not originate from their domains. Organizations seeking zero trust automatically assume that any external services it commissions have security breaches and may leak sensitive information"
</b></details>

<details>
<summary>What it means to be "FIPS compliant"?</summary><br><b>
To be FIPS compliant means an organization adheres to the Federal Information Processing Standards (FIPS) in order to act in accordance with the Federal Information Security Management Act of 2002 (FISMA) and the Federal Information Security Modernization Act of 2014 (FISMA2014).
</b></details>

<details>
<summary>What is a Certificate Authority?</summary><br><b>
</b></details>

[Thesslsstore](https://www.thesslstore.com/blog/what-is-a-certificate-authority-ca-and-what-do-they-do/): A certificate authority, also known as a certification authority, is a trusted organization that verifies websites (and other entities) so that you know who you’re communicating with online. Their objective is to make the internet a more secure place for organizations and users alike. This means that they play a pivotal role in digital security.
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

[Idrnd, Sailpoint](https://www.idrnd.ai/5-authentication-methods-that-can-prevent-the-next-breach/)(https://www.sailpoint.com/identity-library/authentication-methods-used-for-network-security/):

* Password-based authentication. 
* Multi-factor authentication.
* Certificate-based authentication.
* Biometric authentication.
* Token-based authentication.
</b></details>

<details>
<summary>Give an example of basic authentication process</summary><br><b>

A user uses the browser to authenticate to some server. It does so by using the authorization field which is constructed from the username and the password combined with a single colon. The result string is encoded using a certain character set which is compatible with US-ASCII. The authorization method + a space is prepended to the encoded string.
</b></details>

<details>
<summary>Explain Token-based authentication</summary><br><b>

[Fortinet](https://www.fortinet.com/resources/cyberglossary/authentication-token#:~:text=Token%2Dbased%20authentication%20is%20a,a%20unique%20encrypted%20authentication%20token):
Token-based authentication is a protocol that generates encrypted security tokens. It enables users to verify their identity to websites, which then generates a unique encrypted authentication token. That token provides users with access to protected pages and resources for a limited period of time without having to re-enter their username and password. Token-based authentication works through this five-step process:

  * Request: The user logs in to a service using their login credentials, which issues an access request to a server or protected resource.
  * Verification: The server verifies the login information to determine that the user should have access. This involves checking the password entered against the username provided.
  * Token submission: The server generates a secure, signed authentication token for the user for a specific period of time.
  * Storage: The token is transmitted back to the user’s browser, which stores it for access to future website visits. When the user moves on to access a new website, the authentication token is decoded and verified. If there is a match, the user will be allowed to proceed.
  * Expiration: The token will remain active until the user logs out or closes the server.
</b></details>

<details>
<summary>Explain Risk-based authentication</summary><br><b>

[Wikipedia](https://en.wikipedia.org/wiki/Risk-based_authentication):
In Authentication, risk-based authentication is a non-static authentication system which takes into account the profile (IP address, User-Agent HTTP header, time of access, and so on[1]) of the agent requesting access to the system to determine the risk profile associated with that transaction. The risk profile is then used to determine the complexity of the challenge. Higher risk profiles lead to stronger challenges, whereas a static username/password may suffice for lower-risk profiles. Risk-based implementation allows the application to challenge the user for additional credentials only when the risk level is appropriate.
</b></details>

<details>
<summary>Explain what is Single Sign-On</summary><br><b>

SSO (Single Sign-on), is a method of access control that enables a user to log in once and gain access to the resources of multiple software systems without being prompted to log in again.
</b></details>

<details>
<summary>Explain MFA (Multi-Factor Authentication)</summary><br><b>

Multi-Factor Authentication (Also known as 2FA). Allows the user to present two pieces of evidence, credentials, when logging into an account.

- The credentials fall into any of these three categories: something you know (like a password or PIN), something you have (like a smart card), or something you are (like your fingerprint).  Credentials must come from two different categories to enhance security.

</b></details>

#### Security - Passwords

<details>
<summary>How do you manage sensitive information (like passwords) in different tools and platforms?</summary><br><b>

[Digitalguardian](https://digitalguardian.com/blog/101-data-protection-tips-how-keep-your-passwords-financial-personal-information-safe):

  * Encrpyt sensitive data
  * Use backups 
  * Anti-malware protection 
  * Update operating systems regularily 
  * Automate software updates 
  * Firewall
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

#### Security - Cookies

<details>
<summary>What are cookies? Explain cookie-based authentication</summary><br><b>
Cookies are pieces of data used to identify the user and their preferences. The browser returns the cookie to the server every time the page is requested. Specific cookies like HTTP cookies are used to perform cookie-based authentication to maintain the session for each user. The entire cookie-based authentication works in the following manner:

  * The user gives a username and password at the time of login. Once the user fills in the login form, the browser (client) sends a login request to the server.
  * The server verifies the user by querying the user data. If the authentication request is valid, the server generates the following:
    * A session by utilizing the user information
    * A unique ID, known as the session ID
  * The server then passes the session ID to the browser that keeps it. The server also keeps track of the active sessions.
  * The browser has to submit this generated session ID while sending a subsequent request. Every time the server validates the session ID. The session ID helps the authentication process identify the user and provides access accordingly.
  * When the user logs out of the application, the session gets destroyed from both the client (browser) and the server. It discontinues the authentication process from happening again through the respective session ID.
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

[Appviewx](https://www.appviewx.com/education-center/what-are-ssh-keys/#:~:text=for%20key%20management-,2.,remote%20machine%20over%20the%20internet.): SSH keys are a pair of public and private keys that are used to authenticate and establish an encrypted communication channel between a client and a remote machine over the internet.
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
Hashing is the process of converting a given key into another value. A hash function is used to generate the new value according to a mathematical algorithm. The result of a hash function is known as a hash value or simply, a hash.

A good hash function uses a one-way hashing algorithm, or in other words, the hash cannot be converted back into the original key.
</b></details>

<details>
<summary>How hashes are part of SSH?</summary><br><b>

Hashes used in SSH to verify the authenticity of messages and to verify that nothing tampered with the data received.
</b></details>

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
<summary>Explain OAuth</summary><br><b>
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

Cross-Site Request Forgery (CSRF) is an attack that makes the end user to initate a unwanted action on the web application in which the user has a authenticated session, the attacker may user an email and force the end user to click on the link and that then execute malicious actions. When an CSRF attack is successful it will compromise the end user data 

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
<summary>Briefly describe software supply chain. </summary><br><b>

[Increment](https://increment.com/apis/apis-supply-chain-software/): The fundamental idea of the software supply chain is to purchase and implement code solutions for a to-be system. This accelerates the development and deployment of a company’s product. Thus, playing an important role in the software's lifecycle and functionality.
</b></details>

<details>
<summary>Give examples of what a code solution could be. </summary><br><b>

  * API's, for instance:
    * Twilio - provides communication APIs such as information for incoming mobile text messages.
    * PayPal - provides a payment solution for e.g. e-commerce.
    * AWS - e.g. outsourcing infrastructures / data centers.
</b></details>

<details>
<summary>What're some benefits with software supply chain? </summary><br><b>

[Increment](https://increment.com/apis/apis-supply-chain-software/): Resource-saving. Using and paying for existing solutions to resource-heavy problems saves time as well as money. Hence resulting in efficient, cheap and greater opportunities to develop and deploy software products for consumers. 
</b></details>

<details>
<summary>What is a software supply chain attack? </summary><br><b>

[Aquasec](https://www.aquasec.com/cloud-native-academy/devsecops/supply-chain-security/): An attack by an actor who injects malicious software into a part of the software supply chain.
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

<details>
<summary> Briefly suggest some solutions related to those threats from a developer perspective. 
</summary><br><b>

[Aquasec](https://www.aquasec.com/cloud-native-academy/devsecops/supply-chain-security/): 

  * Carefully investigate the third party vendor’s security practices
  * Conduct an incident response plan that should be followed if an attack occurs. 
  * Raise awareness among employees of potential threats and critical attributes of the product and/or organization. 
</b></details>

<details>
<summary> Suggest and describe a specific tool that could enhance threat prevention from a developer perspective. 
</summary><br><b>

[Aquasec](https://www.aquasec.com/aqua-cloud-native-security-platform/): 
Aquasec is a tool which scans a project for potential security threats. This involves for instance vulnerability scanning, cloud security, Kubernetes security and serverless security.
</b></details>

#### Package management & Security 

<details>
<summary> What is a package manager?
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): A tool that allows you to easily download, add and thus reuse programming libraries in your project. E.g. npm or yarn.
</b></details>

<details>
<summary> What is a build tool?
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): A tool that fetches the packages (dependencies) that are required to compile, test and deploy your application. 
</b></details>

<details>
<summary> Describe bloated dependencies.
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): 
An application usually has different dependencies. Typically, not all of them are required for building and running the application. Bloated dependencies is the concept of including the unnecessary dependencies for building and running your application. 
</b></details>

<details>
<summary> Explain a few cons with bloated dependencies.
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): 

  * Challenging to manage.
  * Decreases performance of the application.
  * Risk for malicious code that a threathening actor can take advantage of. 
</b></details>

<details>
<summary> Briefly explain how DepClean for Maven projects work.
</summary><br><b>

[Baudry et al.](https://arxiv.org/pdf/2001.07808.pdf): You input your project consisting of bytecode, a project object model (POM) and the Maven central repository into DepClean. DepClean will identify the dependency tree and perform bytecode analysis of API member calls in order to determine what dependencies are actually used in the project. The used dependencies will be intact, whereas the idle dependencies are removed from the dependency tree. DepClean will ultimately produce a dependency usage report and a debloated POM file. 
</b></details>

<details>
<summary> Provide another solution to manage dependencies. 
</summary><br><b>

[Npm.js documentation](https://docs.npmjs.com/cli/v8/commands/npm-prune): Use clean-up commands that are usually provided by the package manager authors. For instance, npm prune will remove any extraneous package. 
</b></details>

<details>
<summary> How can a threatening actor take advantage of open source packages/libraries? 
</summary><br><b>

[Aquasec](https://www.aquasec.com/cloud-native-academy/devsecops/supply-chain-security/): An attacking actor may identify, target and inject malicious software in a vulnerable part of an open source package or a third party vendor’s code. The consumer of this code may consequently and unknowingly deploy the malicious code throughout their pipelines, thus infecting their own projects. An example of this happening is the hack of (link) SolarWinds.
</b></details>

<details>
<summary> How can you make sure that you use trustworthy packages for your project?
</summary><br><b>
You can’t. You will always be exposed to security risk once you start using open source or vendor packages. The goal is to minimize the risk in order to avoid security breaches.  
</b></details>

<details>
<summary> Explain checksum.
</summary><br><b>

[Fred Cohen (permission needed)](https://reader.elsevier.com/reader/sd/pii/0167404887900319?token=D5339ABC064AD9A2B50B74D8CE890B0E22A302A0BC461A50078D407BEA01052737DC6AAEF95A854E72A73B6D0C67E260&originRegion=eu-west-1&originCreation=20220502180611): Checksum is a way to verify the integrity of information in systems with no built-in protection. In other words, it provides a way of validating that the content of a file or a package / library is intact. This is useful since attacks or errors may occur during transmission of files. However, it requires that the package author has run a checksum function for the file / package which creates a specific hash for that version of the file. A minor change of the file content will result in a different checksum. If you have access to the original checksum of the file, you may run checksum on your own. In case the resulting checksum matches the original one, no changes have been made in the file. You can now conclude that no error or malicious injection was done during transmission of the file. 
</b></details>
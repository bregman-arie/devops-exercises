## Security

<details>
<summary>What is DevSecOps? What its core principals?</summary><br><b>
</b></details>

<details>
<summary>What the "Zero Trust" concept means? How Organizations deal with it?</summary><br><b>

[Codefresh definition](https://codefresh.io/security-testing/codefresh-runner-overview): "Zero trust is a security concept that is centered around the idea that organizations should never trust anyone or anything that does not originate from their domains. Organizations seeking zero trust automatically assume that any external services it commissions have security breaches and may leak sensitive information"
</b></details>

<details>
<summary>What it means to be "FIPS compliant"?</summary><br><b>
</b></details>

<details>
<summary>What is a Certificate Authority?</summary><br><b>
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
<summary>Explain MFA (Multi-Factor Authentication)</summary><br><b>

Multi-Factor Authentication (Also known as 2FA). Allows the user to present two pieces of evidence, credentials, when logging into an account.

- The credentials fall into any of these three categories: something you know (like a password or PIN), something you have (like a smart card), or something you are (like your fingerprint).  Credentials must come from two different categories to enhance security.

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

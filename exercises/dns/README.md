## DNS

<details>
<summary>What is DNS? What is it used for?</summary><br><b>

DNS (Domain Name Systems) is a protocol used for converting domain names into IP addresses.<br>
As you know computer networking is done with IP addresses (layer 3 of the OSI model) but for as humans it's hard to remember IP addresses, it's much easier to remember names. This why we need something such as DNS to convert any domain name we type into an IP address. You can think on DNS as a huge phonebook or database where each corresponding name has an IP.
</b></details>

<details>
<summary>What is DNS resolution?</summary><br><b>

The process of translating IP addresses to domain names.
</b></details>

<details>
<summary>What is a DNS record?</summary><br><b>

A mapping between domain name and an IP address.
</b></details>

<details>
<summary>How DNS works?</summary><br><b>

In general the process is as follows:

  * The user types an address in the web browser (some_site.com)
  * The operating system gets a request from the browser to translate the address the user entered
  * A query created to check a local entry of the address exists in the system. In case it doesn't, the request is forwarded to the DNS resolver
  * The Resolver is a server, usually configured by your ISP when you connect to the internet, that responsible for resolving your query by contacting other DNS servers
  * The Resolver contacts the root nameserver (aka as .)
  * The root nameserver responds with the address of the relevant Top Level Domain DNS server (if your address ends with org then the org TLD)
  * The Resolver then contacts the TLD DNS and TLD DNS responds with the IP address that matches the address the user typed in the browser
  * The Resolver passes this information to the browser
  * The user is happy :D
</b></details>

<details>
<summary>Explain the resolution sequence of: www.site.com</summary><br><b>

It's resolved in this order:

1) .
2) .com
3) site.com
4) www.site.com
</b></details>

<details>
<summary>What types of DNS records are there?</summary><br><b>

  * A
  * PTR
  * MX
  * AAAA
  ...

A more detailed list, can be found [here](https://www.nslookup.io/learning/dns-record-types)
</b></details>

<details>
<summary>What is a A record?</summary><br><b>

A (Address) Maps a host name to an IP address. When a computer has multiple adapter cards and IP addresses, it should have multiple address records.
</b></details>

<details>
<summary>What is a AAAA record?</summary><br><b>

An AAAA Record performs the same function as an A Record, but for an IPv6 Address.
</b></details>

<details>
<summary>What is a PTR record?</summary><br><b>

While an A record points a domain name to an IP address, a PTR record does the opposite and resolves the IP address to a domain name.
</b></details>

<details>
<summary>What is a MX record?</summary><br><b>
MX (Mail Exchange) Specifies a mail exchange server for the domain, which allows mail to be delivered to the correct mail servers in the domain.
</b></details>

<details>
<summary>Is DNS using TCP or UDP?</summary><br><b>

DNS uses UDP port 53 for resolving queries either regular or reverse. DNS uses TCP for zone transfer.
</b></details>

<details>
<summary>True or False? DNS can be used for load balancing</summary><br><b>

True.
</b></details>

<details>
<summary>Which techniques a DNS can use for load balancing?</summary><br><b>
</b></details>

<details>
<summary>What is DNS Record TTL? Why do we need it?</summary><br><b>
</b></details>

<details>
<summary>What is a zone? What types of zones are there?</summary><br><b>
</b></details>

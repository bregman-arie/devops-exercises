## Grafana

<details>
<summary>Explain what is Grafana</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana/latest/introduction): "Grafana is a complete observability stack that allows you to monitor and analyze metrics, logs and traces. It allows you to query, visualize, alert on and understand your data no matter where it is stored. Create, explore, and share beautiful dashboards with your team and foster a data driven culture."
</b></details>

<details>
<summary>What is Grafana Cloud</summary><br><b>

[Grafana cloud](https://grafana.com/products/cloud/) is the fully managed verision of Grafana that is offered as a service through the cloud. The service is set up, administered and maintained by Grafana Labs and offers both free and paid options.
</b></details>

<details>
<summary>What is Grafana Enterprise</summary><br><b>

[Grafana Enterprise](https://grafana.com/docs/grafana/latest/enterprise/#enterprise-plugins) is a commercial edition of Grafana offered with enterprise features such as _Enterprise datasource_ plugins and built-in collaboration features. The edition includes full-time support and training from Grafana team.
 </b></details>
 
<details>
<summary>In which OS can we install Grafana</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana/latest/installation/requirements/): Grafana can be installed on any platform, it is however only supported on the following platforms
- Windows
- MacOS
- Debian / Ubuntu
- Docker
- RPM-based linux (CentOS, Fedora, Red Hat, openSUSE, SUSE)
 </b></details>
 
<details>
<summary>What is the default HTTP port</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): Grafana runs on default port 3000.
</b></details>

<details>
<summary>How can we enforce HTTPS</summary><br><b>

[Grafana community](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): Set the protocol to https on the Configuration settings, Grafana will then expect clients to send requests using the HTTPS protocol. Any client that uses HTTP will receive an SSL/TLS error.
</b></details>

<details>
<summary>How can we install plugins</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): *Add answer
</b></details>

<details>
<summary>Explain what a 'Data source' is</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana-cloud/fundamentals/intro-to-datasources/): A data source is some storage backend that acts as a source of data for Grafana. Some popular data sources are Prometheus, InfluxDB, Loki, AWS cloudwatch.
</b></details>

<details>
<summary>Where is the configuration stored</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): It depends on the operating system Grafana runs on
  - Linux: /etc/grafana/grafana.ini
  - Windows: $WORKING_DIR/conf/defaults.ini
  - MacOS: /usr/local/etc/grafana/grafana.ini
</b></details>

<details>
<summary>What is the difference between "Default configuration" to "Custom configuration</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): 
</b></details>

<details>
<summary>Which external authentication is supported out-of-the-box</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/auth/overview/
): Grafana Auth is the built-in authentication system with password authentication enabled by default
</b></details>

<details>
<summary>How can we import a dashboard</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): 
</b></details>

<details>
<summary>What is the format for the dashboard</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/dashboards/json-model/
): Grafana dashboards are represented in JSON files as objects, they store metadata about a dashboard e.g. dashboard properties, panel metadata and variables.

</b></details>

<details>
<summary>How is the version upgrade done</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/dashboards/json-model/
): The version upgrade varies on how Grafana was installed:
- Debian package: Download and execute the latest grafana package to upgrade.
- APT repository: Run sudo apt-get update (or upgrade)
- Binary .tar file: Download and extract the new package and overwrite all existing files.
- Docker: Pull the latest docker image from docker hub registry and stop the current container with Grafana. Then remove the old container and start a new with the latest grafana image
- Windows: Download the latest Windows binary package and extract to the same location as the old files, overwriting them
- MacOS: run brew update and then brew reinstall grafana


</b></details>



 
 
 
 


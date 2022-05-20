## Grafana

<details>
<summary>Explain what is Grafana</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana/latest/introduction): "Grafana is a complete observability stack that allows you to monitor and analyze metrics, logs and traces. It allows you to query, visualize, alert on and understand your data no matter where it is stored. Create, explore, and share beautiful dashboards with your team and foster a data driven culture."
</b></details>

<details>
<summary>What is Grafana Cloud</summary><br><b>

[Grafana cloud](https://grafana.com/products/cloud/) is an edition of Grafana that is offered as a service through the cloud. The service is set up, administered and maintained by Grafana Labs and offers both free and paid options.
</b></details>

<details>
<summary>What is Grafana Enterprise</summary><br><b>

[Grafana Enterprise](https://grafana.com/docs/grafana/latest/enterprise/#enterprise-plugins) is a commercial edition of Grafana offered with enterprise features such as _Enterprise datasource_ plugins and built-in collaboration features. The edition includes full-time support and training from Grafana team.
 </b></details>
 
<details>
<summary>In which OS can we install Grafana</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana/latest/installation/requirements/): Grafana can be installed on any platform, it is however only supported on the following platforms: 
- Windows
- MacOS
- Debian / Ubuntu
- Docker
- RPM-based linux (CentOS, Fedora, Red Hat, openSUSE, SUSE)
 </b></details>
 
<details>
<summary>What is the default HTTP port?</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): Grafana runs on default port 3000.
</b></details>

<details>
<summary>Explain how we can enforce HTTPS</summary><br><b>

[Grafana community](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): Set the protocol to https on the Configuration settings, Grafana will then expect clients to send requests using the HTTPS protocol. Any client that uses HTTP will receive an SSL/TLS error.
</b></details>

<details>
<summary>How can we install plugins</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/plugins/installation/): Navigate to the [Grafana plugins page](https://grafana.com/grafana/plugins/), find the desired plugin and click on it, then click on the installation tab. There are two ways to install depending on where your Grafana server is running:
- Cloud: On the For field of the installation tab, select the name of the organization you want to install the plugin on (unless you are only part of one), then click **install plugin**. Grafana cloud will automatically install the plugin to your Grafana instance.
you may need to log out and back in to see the plugin
- Local grafana: You can use the Grafana CLI which lets you list available plugins and install them.
```
grafana-cli plugins list-remote
grafana-cli plugins install <plugin-id>
```
You can also install a packaged plugin by downloading the asset from the installation tab, then extract the archive into the plugin directory. The path to the plugin directory can be seen in the configuration file: ```unzip my-plugin-0.2.0.zip -d YOUR_PLUGIN_DIR/my-plugin```
</b></details>

<details>
<summary>Explain what a 'Data source' is</summary><br><b>

[Grafana Docs](https://grafana.com/docs/grafana-cloud/fundamentals/intro-to-datasources/): A data source is some storage backend that acts as a source of data for Grafana. Some popular data sources are Prometheus, InfluxDB, Loki, AWS cloudwatch.
</b></details>

<details>
<summary>Where is the configuration stored</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/getting-started/getting-started/): It depends on the operating system Grafana runs on
  - Linux: ```/etc/grafana/grafana.ini```
  - Windows: ```$WORKING_DIR/conf/defaults.ini```
  - MacOS: ```/usr/local/etc/grafana/grafana.ini```
</b></details>

<details>
<summary>What is the difference between "Default configuration" to "Custom configuration</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/administration/configuration/): The default configuration contains settings that Grafana use by default, the location depends on the OS environment:
- Windows: ```$WORKING_DIR/conf/defaults.ini```
- Linux: ```/etc/grafana/grafana.ini```
- macOS: ```/usr/local/etc/grafana/grafana.ini```

The custom configuration can be configured, either by modifying the custom configuration file or by adding environment variables that overrides current configuration. The configuration varies depending on the OS:
- Windows: There is a file ```sample.ini``` in the same directory as the defaults.ini file, copy sample.ini and name it ```custom.ini```. Uncomment the settings you want to override.
- Linux: Edit the configuration file at ```/etc/grafana/grafana.ini```
- macOS: Add a configuration file named ```custom.ini``` in the conf folder, if you installed Grafana using Homebrew then you can manually edit the ```conf/defaults.ini```
- Docker: You can override existing configuration in Grafana with environmental variables. An example is setting the Grafana instance name: ```E.g. export GF_DEFAULT_INSTANCE_NAME=my-instance```
</b></details>

<details>
<summary>Which external authentication is supported out-of-the-box</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/auth/overview/): Grafana Auth is the built-in authentication system with password authentication enabled by default
</b></details>

<details>
<summary>How can we import a dashboard</summary><br><b>

[Grafana getting started](https://grafana.com/docs/grafana/latest/dashboards/export-import/): A Grafana dashboard can be imported through the Grafana UI. Click on the + icon in the sidebar and then click import. You can import a dashboard through the following options:
- Uploading a dashboard JSON file, which is exported from the Grafana UI or fetched through the [HTTPS API](https://grafana.com/docs/grafana/latest/http_api/dashboard/#create-update-dashboard
)
- Paste a Grafana dashboard URL which is found at [grafana Dashboards](https://grafana.com/grafana/dashboards/), or a dashboard unique id into the text area.
- Paste raw Dashboard JSON text into the panel area.
Click load afterwards.
</b></details>

<details>
<summary>What is the format for the dashboard</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/dashboards/json-model/): Grafana dashboards are represented in JSON files as objects, they store metadata about a dashboard e.g. dashboard properties, panel metadata and variables.

</b></details>

<details>
<summary>How is the version upgrade done</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/dashboards/json-model/): The version upgrade varies on how Grafana was installed:
- Debian package: Download and execute the latest grafana package to upgrade.
- APT repository: Run sudo apt-get update (or upgrade)
- Binary .tar file: Download and extract the new package and overwrite all existing files.
- Docker: Pull the latest docker image from docker hub registry and stop the current container with Grafana. Then remove the old container and start a new with the latest grafana image
- Windows: Download the latest Windows binary package and extract to the same location as the old files, overwriting them
- MacOS: run brew update and then brew reinstall grafana
</b></details>

<details>
<summary>Explain the steps to share your dashboard with your team</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/sharing/share-dashboard/): Go to the homepage of your grafana Instance. Click on the share icon in the top navigation, from there three tabs are visible with the link tab shown.
- Direct link: Click copy, send the link to a Grafana user, note that the user needs authorization to view the link. This is done by adding the user to a team.
- Public Snapshot: Click on local snapshot to publish a snapshot to your local Grafana instance, or Publish to snapshots.raintank.io which is a free service for publishing dashboard snapshots to an external Grafana instance
You can configure snapshots to expire after a certain time and the timeout value to collect dashboard metrics
</b></details>
 
<details>
<summary>How can you organise your dashboards and users in Grafana</summary><br><b>

[Grafana docs](https://grafana.com/blog/2022/03/14/how-to-best-organize-your-teams-and-resources-in-grafana/
): The recommended way by Grafana labs is to create folders for grouping dashboards, library panels and alerts. Users can be organised through Teams which grants permissions to members of a group.
- [Folders](https://grafana.com/docs/grafana/latest/dashboards/dashboard_folders/): Click the + icon in the sidebar, then click "Create folder". In the create folder page, fill an unique name for the folder and click "Create"
- [Teams](https://grafana.com/tutorials/create-users-and-teams/) You need to be the server admin in order to create Teams. 
 1. Click the server admin (shield) icon in the sidebar, then in the Users tab, click New user.
 2. Enter the user details e.g. name, E-mail, Username and Password. The password can be changed later by the user
 3. Click Create to create the user account.
</b></details>
 
<details>
<summary>Explain the steps to create an Alert</summary><br><b>

[Grafana docs](https://grafana.com/docs/grafana/latest/alerting/old-alerting/create-alerts/): 
 
 "Navigate to the panel you want to add or edit an alert rule for, click the title, and then click Edit. On the Alert tab, click Create Alert. If an alert already exists for this panel, then you can just edit the fields on the Alert tab. Fill out the fields. Descriptions are listed below in Alert rule fields. When you have finished writing your rule, click Save in the upper right corner to save alert rule and the dashboard. (Optional but recommended) Click Test rule to make sure the rule returns the results you expect"
</b></details>


 
 
 
 


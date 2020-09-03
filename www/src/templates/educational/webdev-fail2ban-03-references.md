These references were used to troubleshoot our own experiences with `fail2ban`, and can be used for further configuration and advanced setups.

### fail2ban Official Links

- <https://www.fail2ban.org/wiki/index.php/Main_Page>
- <https://www.fail2ban.org/wiki/index.php/MANUAL_0_8>
- <https://www.fail2ban.org/wiki/index.php/MANUAL_0_8#Jails>

### OSI Networking and HTTP

- TCP/IP: <https://en.wikipedia.org/wiki/Transmission_Control_Protocol>
- UDP/IP: <https://en.wikipedia.org/wiki/User_Datagram_Protocol>
- HTTP: <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>
- HTTPS: <https://en.wikipedia.org/wiki/HTTPS>
- Looking-up IP Addresses: <https://www.ipvigilante.com/>

### Webservers

- Nginx: <https://www.nginx.com/resources/wiki/>
- cURL: <https://curl.haxx.se/>
- "Everything cURL" (book): <https://ec.haxx.se/>
- JSON Query Parsing: <https://stedolan.github.io/jq/manual/>
- <https://stackoverflow.com/questions/40396445/get-outputs-from-jq-on-a-single-line>
- <https://docs.nginx.com/nginx/admin-guide/security-controls/blacklisting-ip-addresses/>
- <https://stackoverflow.com/questions/22891148/nginx-how-to-run-a-shell-script-on-every-request>

A command to query the location details for an IP Address and then parse it out to a CSV entry of "City, State, Country":

```bash
IPADDR=999.999.999.999; curl -s https://ipvigilante.com/${IPADDR} | jq -r "[.data.city_name, .data.subdivision_1_name, .data.country_name]|@csv";
```

Just change the `999.999.999.999` value to the IP Address that you want to look-up.

### `fail2ban` and `iptables`

- [Discussion on iptables Config](https://gist.github.com/antoniocampos/1b8bc607d7b2d4a42e2a6e7df00645d0) (GitHub gist)
- Default Blocking Behavior: <https://github.com/fail2ban/fail2ban/issues/507>
- Blocking ASCII/Unicode Filters: <https://github.com/mariusv/nginx-badbot-blocker/issues/157>
- <https://www.the-art-of-web.com/system/fail2ban-filters/>
- <https://serverfault.com/questions/157375/reject-vs-drop-when-using-iptables>
- <https://www.cyberciti.biz/faq/linux-iptables-drop/>
- <https://www.cyberciti.biz/tips/linux-security.html>
- <https://www.linode.com/docs/security/using-fail2ban-to-secure-your-server-a-tutorial/>
- <https://www.nginx.com/blog/dynamic-ip-blacklisting-with-nginx-plus-and-fail2ban/>


### `firewalld` and `ipset`

Using `ipset` may not be possible on a VPS depending on how the container/image is being run. `ipset` requires Kernel-Space access in Linux, which is often highly restricted by default, in virtual systems especially. So these links provide some alternative approaches that may be less-resource-heavy and more preemptive, but you may not be able to run these commands in all VPS systems.

- <https://www.getpagespeed.com/server-setup/security/nginx-honeypot-the-easiest-and-fastest-way-to-block-bots>
- <https://www.linuxjournal.com/content/advanced-firewall-configurations-ipset>
- <https://www.cyberciti.biz/faq/enable-firewalld-logging-for-denied-packets-on-linux/>

This is going to be a very long and detailed discussion -- just a heads-up. We thought about breaking it up into multiple articles, but really it all goes together, so bear with us.

...
...

## Filter Configuration

So now, with `fail2ban` installed, you have what is called a `jail.conf` configuration file for setting the rules of which traffic requests to find and mark as "sketchy" -- adding them to your "banned" list.

One of the first things we suggest to help with testing and functionality is to create a new rule for indicating that you've manually banned an address (a Client).

In our case, we're calling this rule, and its filter file `manual`:

```INI
[manual]
bantime = 1036800
enabled = true
blocktype  = RETURN
returntype = DROP
filter  = manual
```

The `bantime` is in seconds, and says how long the address will remain in the "banned" file's list of IP Addresses.

The `enabled` option says whether or not this rule is used while `fail2ban` is running.

The `blocktype` and `returntype` are explained below.

The `filter` option should be the basename (no file-extension) of the "filter" file that you create and configure with the regular expression(s) used to search the webserver log file(s).

In our case, we're calling the filter file `manual.conf` and we don't need a regex, so we're just going to create the empty file as such:

```bash
sudo -E touch /etc/fail2ban/filter.d/manual.conf
```

Note that all your filter files should go into the `/etc/fail2ban/filter.d/` directory.

Now, with this filter added, we can save our changes (in `vim` thats with `ESC` then `:wq` then `ENTER`), and then restart `fail2ban` with:

```bash
sudo -E systemctl restart fail2ban
```

Confirm that `fail2ban` is running and there are no errors, with:

```bash
sudo -E systemctl status fail2ban
```

Now to add an IP manually to the ban list, you can `tail` your Nginx `access.log` file to find a sketchy request and do the following:

```bash
sudo -E fail2ban-client set manual banip 999.999.999.999
```

Where you need to replace `999.999.999.999` with the IP Address you want to ban, and you'll note that `manual` is the name from the config file section -- `[manual]` -- that we created.

The complete log file for `fail2ban` is at

```bash
/var/log/fail2ban.log
```

But, in there you'll find lots of internal messaging about all the goings on of `fail2ban`. If you just want to see which IP Addresses have been banned, you can use the following `grep` command:

```bash
sudo -E grep "Ban" /var/log/fail2ban.log
```

This will search for the (case-sensitive) term `Ban` and show each line of the log file that contains this word. After you've banned a few addresses manually or through other `fail2ban` filters you should see output like:

```bash
2020-07-22 13:27:28,422 fail2ban.actions        [438]: NOTICE  [manual] Ban 999.999.999.999
2020-07-22 14:44:07,367 fail2ban.actions        [5029]: NOTICE  [nginx-x00] Ban 999.999.999.999
2020-07-22 14:44:07,440 fail2ban.actions        [5029]: NOTICE  [manual] Ban 999.999.999.999
2020-07-22 14:44:07,611 fail2ban.actions        [5029]: NOTICE  [nginx-x00] Ban 999.999.999.999
2020-07-22 14:44:07,691 fail2ban.actions        [5029]: NOTICE  [manual] Ban 999.999.999.999
2020-07-22 14:44:07,836 fail2ban.actions        [5029]: NOTICE  [nginx-x00] Ban 999.999.999.999
2020-07-22 14:44:07,894 fail2ban.actions        [5029]: NOTICE  [manual] Ban 999.999.999.999
```

Note, of course, that all the IP Addresses won't be `999.999.999.999`, but should be different values. You may see repeated values, but you should notice that the number in the square-brackets will be different between repeated entries.

And with that, we now have a manual way to "ban" IP Addresses. Anything noted in that search of the log file will have also been configured to be blocked in some manner by the `iptables` utility.

To see how `iptables` is configured you can call:

```bash
sudo -E iptables -S
```

For each IP address you should see a line like this in the output:

```bash
-A f2b-manual -s 999.999.999.999/32 -j DROP
```

or 

```bash
-A f2b-manual -s 999.999.999.999/32 -j REJECT --reject-with icmp-port-unreachable
```

Below, in the "Autobanning with `iptables`" section, we discuss how the `-j` rule gets configured and what the different meanings are. Suffice it to say, for now, that if you see your banned IP Address in the `iptables -S` output, then something is happening.

And with that, we have the basic setup. Now, let's create a better filter with some help from the internet, to do some more robust auto-banning.

## Example Filter for Unicode Attacks

Now that we've created our `[manual]` rule, let's make a new rule for scanning `nginx` logs that we'll call `[nginx-x00]`, our zeroeth rule.

First, let's use `vim` and edit our `jail.local` file:

```bash
sudo -E vim /etc/fail2ban/jail.local
```

Now, in `vim` we can do `SHIFT`+`g` to jump to the bottom of the file, and then press `SHIFT`+`A` to append to the end of the line, add some newlines, and then create (or copy-then-paste) the following block:

```INI
[nginx-x00]
enabled    = true
port       = http,https
filter     = nginx-x00
logpath    = /var/log/nginx/access.log
bantime    = 86400
findtime   = 86400
blocktype  = RETURN
returntype = DROP
maxretry   = 2
```

So, a few things here to note.

Again, we explain `blocktype` and `returntype` in the next section.

The `maxretry` entry means that if the offender does something suspicious more than 2 times, then they're getting banned.

The `findtime` means that the counter for the `maxretry` setting will get returned to `0`, this many seconds after the first sketchy request. So if somebody does something sketchy-looking, our `findtime = 86400` means that if they do it 2 more times in the next 24 hours, then they're getting banned. If they only do it once or twice a day, then they won't get banned.

The `bantime` means how many seconds we want to ban them for. The banning action is described by the `returntype` setting, which is explained in the next section. If you set `bantime` to a negative number, you can make someone banned forever. One reason not to do this is that IP Addresses are dynamically assigned, especially IPv4 addresses. So while maybe you're getting a sketchy request from an IP one day, it could have be re-leased to somebody else another day, and they just wanna actually visit your site. So, it's not the worst idea to just have a day or two for bans if you don't want to block what could be a valid request.

The `logpath` is the log file that this rule will inspect _via_ the companion filter file.

As mentioned in the `[manual]` setup, the `filter` entry is the basename of the filter file that has the regex for searching the log(s). In this case the file name is `nginx-x00.conf`, which we create by doing the following:

```bash
sudo -E touch /etc/fail2ban/filter.d/nginx-x00.conf
```

And in this case its contents should be:

```bash
[Definition]
failregex = ^<HOST> .* ".*\\x.*" .*$
ignoreregex =
```

Now, this `failregex` was found _via_ the internet, at [this StackOverflow post](https://stackoverflow.com/a/52696223) -- as most regex's are.

This filter is meant to catch a particular kind of request that attempts to sneak ASCII/Unicode parsing past the webserver to a listening app that is trying to parse the request contents.

It's like trying to walk up to people's home/apartment windows and yelling out "Hey, Google, unlock the door.", to see if you have a Google Home device connected up to "smart" doorlocks.

We want to use `fail2ban` to make it so that the requests get noticed as soon as possible and they're blocked from any subsequent requests.

In addition to that, though, we should also make sure we don't do something like putting a Google Home connected to our doorlocks sitting next to a street facing window. So, we shouldn't have utilities blindly connected to our webserver and accepting packets of any kind.

As a brief aside, if you're using `nginx` and you've configured a `location` block, you can add the following line to restrict what kinds of requests are valid for that location:

```bash
limit_except GET POST { deny  all; }
```

That says, if anyone makes an HTTP request to this location (or any sub-location) that is anything other than `GET` or `POST`, then it will be denied a response.

_(Note that `HEAD` is a `GET` request that doesn't reply with a body, so you can add `HEAD` to that list if you want to be verbose, but Nginx will treat it as a `GET`, so `HEAD` is also allowed as written.)_

In this case, a denial is going to be an `HTTP 400` error code ("Bad Request"). If you know you're not making any `POST` requests, like if you just have static files and no forms for that location, you can even go so far as to remove the `POST` in that line.

Just remember that if you configure this and then expand your webapp's functionality, you may need to come back here and reconfigure to keep things running.

And so, now with the `jail.local` and `nginx-x00.conf` files setup, we can restart `fail2ban` and suspicious ASCII/Unicode/Hex attacks should get blocked for 24 hours:

```bash
sudo -E systemctl restart fail2ban
```

## Autobanning with `iptables`

As mentioned, you may not be able to use a more modern technique through `ipset` connection monitoring because of the requirements to access the Linux Kernel-Space. However, you should still be able to configure the `iptables` rules without needing Kernel-Space access in your VPS instance.

With `fail2ban`, we can configure our `jail.local` file to have "rules" (INI entry blocks) that can actually simplify things by automatically creating the `iptables` rules for us.

So, let's say you have your `[manual]` rule-block as we configured above, for adding certain IP Addresses to your "banned"-list.

Within that `[manual]` rule-block, you'll note that we added the following two entries:

```ini
blocktype  = RETURN
returntype = DROP
```

Now, be careful to note a couple things:

- If you don't add these two lines, your rule will still work, but all that will happen is that a suspicious IP address will end-up in the `fail2ban` logs. That IP address can still make requests, even after it's logged as "ban"-able, because you've not configured anything to happen.
- The `returntype` value of `DROP` does ___not___ mean that the TCP/IP requests will be "dropped", it means that whatever the configured `DROP` action for `iptables` _via_ `fail2ban` will happen.

On that first point, we just want to reiterate that those two lines are essential for `fail2ban` to actually "do" anything of value for us. Logging suspicious IPs isn't really useful unless you're sitting there monitoring the log(s).

That being said, if you wanted to test suspicious activity from a known-good system "attacking" your VPS, it may be useful to leave everything else alone but comment-out those two lines so that you don't get yourself blocked. Then you can check the logs but not have to worry about losing your connection to your server.

On the second point, this gets into the nuts-and-bolts of TCP/IP and HTTP requests.

When an HTTP `GET` request is made to a server, the underlying TCP/IP request is waiting for a `SYN-ACK` response. The establishing of a TCP/IP connection requires 3 steps between the client (requester) and server (requestee):

1. Client sends a `SYN` request to the Server.
1. A "good" Server responds with a `SYN-ACK` to the Client.
1. The Client acknowledges the Server's `SYN-ACK` by replying with their own `ACK`.

After those 3 steps, the "TCP Handshake" is completed and the Client and Server can continue communications with back-and-forth packets.

`SYN` refers to a Synchronization Packet message, while `ACK` refers to an Acknowledgement Packet message. We don't need to get into the details of these packets, we just need to understand the handshaking process.

That process, if successful, will establish a TCP/IP (bidirectional) Packet-based connection between two endpoints -- in this case, the Client and the Server. Multiple packets can then carry the HTTP (Hypertext Transfer Protocol) information between the Client and Server to provide the "application" functionality of a web-server.

In the circumstances of malicious activities, people can just setup computers to spew out packets around the internet, trying to establish connections to a server. And if they find a server, then they can progress to the next level of malicious investigation by trying to see if there's a dangling login page, or an old PHP exploit, or maybe even some kind of internet-facing database API that could grant access to a server.

Basically, this becomes a situation of whether or not you should respond. If an IP address starts sending sketchy packets, and `fail2ban` catches them from the logs, and decides to ban them, then what should you do the next time they try to establish a connection?

The two `iptables` options here are to either `REJECT` or `DROP`.

- For `iptables`, configuring a `REJECT` response means to reply to the Client and say "Go Away".
- For `iptables`, configuring a `DROP` response means that there is no reply to the Client, they send their `SYN` request and nothing happens, the packet is received by the server but there is no reply at all.

The first case is useful in terms of being "courteous", but also explicit. If you had an automated service connecting to a Server, a valid response can help with logging and troubleshooting, and could also produce a valid choice for "next steps". Maybe you want to have your service try a different endpoint or go to a different port, or whatever.

However, the second case (`DROP`) becomes more appealing when dealing with malicious investigations. If someone is just pinging out to addresses and looking for servers, then having your server not respond at all can help it seem like there's nothing there. If there's nothing there, then maybe they'll just stop reaching out.

This isn't an ironclad argument, it's just a suggestion. It's similar to the concept of not answering the phone if you don't recognize the number. If it's a telemarketer or a "spam" caller, then not answering could mean that no one's there, or the number's not in use anymore. And they even have said recently in the news and online that if you pick up the phone, you're giving some consent to being called, so by not answering at all you're avoiding any implicit consent to be called in the future. The hope being that at a certain point, they'll fail enough calls to you that you'll be taken off the list of numbers they try to call.

Who's to say what's really best? Either way, we have the option.

The point we're making here in this article is that `DROP` is used in 2 entirely different ways by 2 entirely separate utilities.

First, note that in the following lines from above, `DROP` refers to the `fail2ban` feature:

```ini
blocktype  = RETURN
returntype = DROP
```

Now, the question is, what does `DROP` in `fail2ban` terms, actually do? For that, we need to go to the `iptables.conf` file that should be located here:

```bash
/etc/fail2ban/action.d/iptables-common.conf
```

By default, you'll see a section that looks like this, towards the bottom of the file:

```bash
# Option:  blocktype
# Note:    This is what the action does with rules. This can be any jump target
#          as per the iptables man page (section 8). Common values are DROP
#          REJECT, REJECT --reject-with icmp-port-unreachable
# Values:  STRING
blocktype = REJECT --reject-with icmp-port-unreachable
```

What that says, is that when you "block" an IP Address by using the `fail2ban` config of `returntype = DROP`, then `iptables` will get the configuration rule to:

```bash
REJECT --reject-with icmp-port-unreachable
```

This is our first option, discussed above, where we reply to all requests and tell them to go away if they're a banned address.

If you prefer the "don't answer the phone" approach, you can change the `blocktype` so that your config file looks like this:

```bash
# Option:  blocktype
# Note:    This is what the action does with rules. This can be any jump target
#          as per the iptables man page (section 8). Common values are DROP
#          REJECT, REJECT --reject-with icmp-port-unreachable
# Values:  STRING
blocktype = DROP
```




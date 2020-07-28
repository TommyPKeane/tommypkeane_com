Running a Virtual Private Server (VPS) or a Webserver on the internet is diving into a bit of the digital "Wild West" these days.

For our own use, and yours too, we've created this page as an article to help explain how to setup and understand the use of a tool like `fail2ban`, which will scan your webserver logs, note ban-worthy IP Addresses, and then use `iptables` to auto-respond to them for you.

This tool is a little bit "controversial" amongst the internet security folks, it seems, if only because it's an _ad hoc_ (after the fact) kind of approach.

By using `fail2ban` we're waiting for someone to make a sketchy request, match a ban-worthy filter applied to the webserver logs, and then only after a couple bad requests do they actually get banned. This doesn't stop them from making the requests in the first place. And that is definitely a valid concern.

This is basically like you're sitting around noting the weirdos who knock on your front door or jiggle the handle to see if it's unlocked, and only yelling at them if they come back again later. Arguably, the real important stuff is to keep your doors locked, maybe have some motion-sensor-based lights, and stuff like that.

In internet terms, that means properly configuring your web-server, and blocking anything on any ports that you aren't using, and blocking anything you aren't doing on the ports that you do use. This also means using asymmetric, private-and-public keys when possible, instead of using passwords all the time.

That kind of stuff will be briefly mentioned here in context, but this article is specifically about `fail2ban`. So please be aware that this isn't the end-all/be-all, but we do hope it helps clarify some of the tricky nuances to getting everything up and running.

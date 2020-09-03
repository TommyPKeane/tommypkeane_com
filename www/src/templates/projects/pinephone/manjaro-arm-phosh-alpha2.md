# Manjaro ARM Phosh Operating-System

In August 2020, we downloaded the Alpha2 release of Manjaro ARM running the Phosh desktop environment, and successfully booted-it on our UBports Community Edition Pine64 PinePhone.

This page covers the process of how to download and run the operating system, how to configure it, and some of its notable features.

Since the phone was built to natively run the UBports Ubuntu-Touch operating system, a second OS can be run from the MicroSD slot under the back-cover of the phone. This way, if the secondary OS fails, the phone should be able to always reboot back into the Ubuntu-Touch OS, so as not to "brick" the phone.

As such, this is a pretty painless process and encourages lot of experimentation.

<div id="toc">
  <h3>Article Contents</h3>
  <ul></ul>
</div>

<div id="subBurnMicroSD" class="subsection">

## Burn a MicroSD Card Image

Per the [Official Release Notice](https://forum.manjaro.org/t/manjaro-arm-alpha2-with-phosh-pinephone/157249), the Alpha 2 version of Manjaro ARM with Phosh requires at least an __8GB MicroSD__ card.

We used a __32GB MicroSD__ (PNY) card and an SD Card adapter.

The SD Card adapter allowed us to use the SD card slot on our 2015 Macbook Air, to burn the image to the MicroSD card.

The image was downloaded from here, the `*.img.xz` compressed file:

- Download Image: [Manjaro ARM Phosh (Alpha 2)](https://osdn.net/projects/manjaro-arm/storage/pinephone/phosh/alpha2/)

The SHA and SIG files are optional downloads that you can use to verify that the compressed-image was not corrupted during your download. We did not verify our download -- we will update this article later with details on how to verify.

Once you've downloaded the `*.img.xz` file, you will need to write it to the MicroSD card that you need to mount on your main computer. The Operating System of your main computer should not matter.

To burn the image to the card, we used Etcher.io which is available here;

- [Etcher.io Image Writer App](https://www.balena.io/etcher/)

Etcher.io supports macOS, Windows, and Linux, and it is a free program. There are other ways to do this, but we found this to be quick, convenient, and reliable. Also, you'll likely find that Etcher.io is often recommended when burning images to USB or SD storage.

We needed no special configuration, we plugged in the MicroSD Card using the SD Card adapter, loaded the `*.img.xz` file into Etcher.io, and then pointed the app towards the mounted SD Card.

The image was successfully written in under 2 minutes.

Once finished, the MicroSD card can be unmounted and ejected (usually a one-step process), and then it can be placed into the phone.

It's recommended to turn-off the phone and disconnect it from USB power, as well as remove the battery. This will make it easier to instert the MicroSD card properly without risk of bending or breaking anything.

Here are the steps to install the MicroSD card and boot into the new image automatically:

1. Turn off PinePhone by holding "sleep" button on front-right-hand side of phone. When the message appears, choose "Shutdown" or "Turn Off Phone".
1. Once the phone is off, confirm that any cables are disconnected.
1. Use your finger or a tool to pop off the back cover by prying at the front-bottom-right corner, which should have an indentation in the back-cover.
1. Once the back is removed, it is probably best to go ahead and remove the battery.
1. Insert the MicroSD card in the slot above the battery towards the back-right of the phone. You should see the name/logo on the card facing up at you. The Card should slide into the MicroSD Card slot, and you should be able to push it in 1 or 2 mm further into the slot.
1. Reinsert the battery, take care to align the battery exposed leads to the pins on the bottom-left in the battery slot.
1. Once the battery is installed, you should notice a gap of about 1 to 2 mm between the battery and MicroSD card, if it is all installed properly.
1. Snap the back-cover back onto the phone. Be sure to check all edges to prevent dust/whatever from getting under the cover.
1. Hold the front-right "sleep" button to power-on the phone -- the front-top-left LED should blink as the phone boots.
1. The Phone should automatically boot into your new Operating System, if it was burned to the MicroSD Card properly.

<aside>

__Note:__ on first-boot, the Manjaro ARM Operating System will unpack and setup its configuration on the phone. You will notice a lot of small white text on a black background on the phone, and it'll take about 2 minutes for the phone to fully-boot the first time. After this, subsequent reboots are in the normal time of 30-45 seconds, or less.

</aside>

If you wish to revert back to the Ubuntu Touch installation, you can follow the above steps and (instead) remove the MicroSD card.

If the MicroSD card slot is empty, the pre-installed OS will boot.

If the MicroSD card slot has a card with a valid image inserted, then that system image will boot.

Per the release notice, here are the default credentials:

- Username: `manjaro`
- Passcode: `123456`
- Root user: `root`
- Root password: `root`

The `manjaro` user is part of the Linux `sudoers` group, and `sudo` is pre-installed, so by default your phone passcode is also your `sudo` password when you are logged in as the `manjaro` user.

This code can be changed from the `Settings` app, once booted in Manjaro ARM.
</div>

<div id="subHeadlessSystem" class="subsection">

## Headless System

In contemporary computing, a computer that has no monitor, display, or visible graphical user-interface (GUI) is often called a __Headless System__ or __Headless Computer__.

Many dedicated webservers and embedded systems operate in a headless manner, where you need to make a "remote connection" to the system in-order to control and configure it. The remote connection can be through Serial, USB, Ethernet, WiFi, Bluetooth, or any other communications protocol/channel.

For contemporary (OSI) network-connected systems (TCP/IP) with security in mind, the SSH protocol is the most common means of connecting to a system remotely.

In this case, with the Pine64 PinePhone, using SSH to connect from a separate computer can be an approach to allow for easier typing and interaction with the shell environment running in the Linux Operating-System (OS) that is on the phone. Here, we're now running Manjaro ARM with the Phosh Desktop Environment (the GUI for the OS). But, while the [squeekerboard]() touchscreen keyboard is quite good, it is still more difficult than a normal computer keyboard for interacting with the shell environment.

For faster, easier setup and control of the system, using SSH to connect to the phone from a laptop or desktop computer can be really preferable. Almost everything here can be done on the phone, directly, but using the phone's touchscreen keyboard for shell commands can be quite cumbersome. If you have access still to the computer where you burned the image onto the MicroSD card, then you could use that system to remotely connect and make things easier for yourself.

The Manjaro ARM system is running `sshd` (the SSH daemon - background service) by default, so you only need to get the phone connected to your WiFi LAN, and then you can SSH into the system from any other Ethernet or WiFi connected system on the LAN.

The next few subsections give the full details on how to achieve that connection to the PinePhone over SSH. While this is not necessary for following along with the other sections in this article, we do suggest that you do this, since it can be really, really convenient.

<div id="subsubGetIPAddress" class="subsubsection">

### Get PinePhone IP Address

The following assumes that you've connected your PinePhone to the LAN through WiFi or a compatible USB-C to Ethernet adapter that is recognized by the system. For reference, we've tested the following only using WiFi (2.4 GHz, since the PinePhone does not support 5GHz).

One way to get the current IP Address of the phone is to open the __Terminal__ application and run the following command (pressing the Enter or Return key to send the command):

```bash
ip addr show | grep inet
```

The `iproute2` toolkit's `ip` command has an `addr` subcommand with its own `show` subcommand that will print-out all the connection information for the Network Interface Devices that are currently configured for the system.

You would normally see lots of information about addresses and protocols that may be a bit overwhelming. To simplify the output, we can "pipe" (`|`) it to the "Global Regular Expression Printer" (`grep`) utility and search for the string `inet`.

IPv4 addresses are shown from `ip addr show` with the label `inet`, while IPv6 addresses are shown with `inet6` labels. If you're on a LAN, it's unlikely that you'd need to use IPv6, but you can if you want.

IPv6 was created to deal with the number of connected devices on the internet becoming more numerous than the available unique addresses under the IPv4 scheme. It's been mostly ubiquitously supported over the past few years, though almost all networks still rely on IPv4 addresses for compatibility, and the addresses are shorter and easier to type. Either would work, though, provided that your laptop/desktop (client) actually has IPv6 enabled, and that your LAN switch is new enough to support it. Note that some Operating Systems disable IPv6 by default, depending on when the OS was released.

Typical IPv4 addresses on a LAN are in the `192.168.1.0/24` subnet, meaning that all addresses start with `192.168.1.` and the last number (binary octet) is unique to each device on the network. You may also see addresses like `192.168.0.xxx`, `10.77.xxx.yyy`, `192.168.11.xxx`, and so on. You can learn more about [Private IP Addresses](https://en.wikipedia.org/wiki/Private_network) at that link to Wikipedia.

The output from the above command will look something like:

```bash
inet 127.0.0.1 netmask 0xff000000
inet6 ::1 prefixlen 128
inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
inet6 fe80::14bd:47d3:cc94:3ede%en0 prefixlen 64 secured scopeid 0x5
inet 192.168.1.169 netmask 0xffffff00 broadcast 192.168.1.255
inet6 fe80::806d:8bff:fed0:79ca%awdl0 prefixlen 64 scopeid 0x9
inet6 fe80::806d:8bff:fed0:79ca%llw0 prefixlen 64 scopeid 0xa
```

As you may have multiple network adapters running, and the address you are looking for is from Line 5, above:

```bash
inet 192.168.1.169 ...
```

This is the publicly accessible (private to the LAN) address of the PinePhone.

<aside>

__Note:__ `127.0.0.1` is what is known as the `localhost` address. It is a private address that is only accessible from within the same hardware ecosystem, meaning that only things running within the Operating System that is hosting the network adapter are able to reach that address. All systems use the IPv4 `127.0.0.1` or `localhost` alias for internal bindings. You __can not__ access `localhost` from outside the Operating System. You could access it __after__ you SSH into the system, but you __can not__ use it to establish an SSH connection. If your device has `127.0.0.1` as its only IPv4 (`inet`) address, that means that it was not assigned a DHCP (leased) address, or IPv4 was turned-off in favor of IPv6. So you can either re-enable, request an address again (disconnect, reconnect to WiFi switch), or go ahead with one of the public IPv6 addresses. The `fe80:...` IPv6 addresses are [IPv6 Link-Local](https://en.wikipedia.org/wiki/Link-local_address) addresses, which should be accessible from within the same LAN.

</aside>

The alternative approach is to use the Phosh Desktop Environment and use the __Settings__ app. You can go into the system settings, go to the __WiFi__ section, and you should see the list of visible SSIDs for the WiFi networks around you. Your WiFi network should be enabled and selected, and so a circular button with a gear icon should be to the right of the SSID name. If you click the gear icon you will go into a submenu that shows the details of the network connection. Here, there should be a line that shows the IPv4 address of the phone on this WiFi network. Again, it will likely be a private address as formatted above.
</div>

<div id="subsubConnectSSH" class="subsubsection">

### Connecting over SSH

So, now, to connect to the PinePhone over SSH, we need 3 things:

- PinePhone running Manjaro ARM with `sshd` running.
- IP Address of PinePhone (example: `192.168.1.100`).
- Computer with SSH on the same LAN and in a two-way accessible subnet.

If you followed the above, and connected your PinePhone running Manjaro ARM to your WiFi network after the first boot, then you should be all set with the PinePhone setup as the "server", since `sshd` will be running by default.

The previous subsection describes how to get the PinePhone's IP address, and for this tutorial we'll assume that it is `192.168.1.100`, which needs to be accessible on the LAN.

The PinePhone will be the SSH "server" and your computer will be the SSH "client".

We only need the server IP address, because the client will initiate the connection to the server. The only use of the client IP address is if you want to check the server's access logs or if you wanted to restrict SSH access to be only from a specific system -- though that can be an easy way to get yourself locked out if you make a mistake or forget the address.

So, now, we make sure the PinePhone is on and running Manjaro ARM, but the display can be asleep, that's ok.

Next, go to your computer and bring up a terminal emulator, and use the following command:

```bash
ssh manjaro@192.168.1.100
```

We're using the `ssh` utility to start the connection, we're connecting to the `192.168.1.100` address which should have an `sshd` server-application running, and we're indicating that we're going to login with the username `manjaro`.

If you just tried `ssh 192.168.1.100` the `ssh` utility would use the name of whatever user you are on your computer and send that as the login username to the PinePhone. So, unless your computer username and your PinePhone username happen to be the same, it's not going to work. Even if they were the same, being specific is never a bad thing, because it'll make troubleshooting easier, in case of issues.

Now, once the connection is established you'll get asked 2 questions:

1. You'll likely be warned the the Public-Key is tied to a different address than the `192.168.1.100` address that you're connecting to. This is common because the LAN address is assigned by DHCP, so the `sshd` service associates its public encryption key with the phone (device) and not its temporary IP Address. As long as you're sure that you are connecting to the right address, this is just a circumstantial warning that you can ignore. You will be asked if you want to continue with the connection process despite this "mismatch" and you can type `yes` to continue. You will likely be asked this every time you connect, but it's ok.
1. You'll then be asked for the password for the `manjaro` user. This will be whatever your password is for that account. From the installation section we can see that the default password is `123456`, which is also the passcode for the phone. Unless you changed it, that will be the password that you need to enter here.

And that's it, you should now be connected to the PinePhone, as if you were in it's __Terminal__ app, running whatever the shell is for the `manjaro` user -- which will be `bash`, as configured by the `/home/manjaro/.bashrc` file, by default.

Now that you're connected to the phone in the `bash` shell, you can run any viable commands and they'll all be happening on the phone, as if you're just using your computer keyboard and screen to control the __Terminal__ app on the phone.

This is a text-based protocol, SSH, so you cannot see any graphical output, only text-output. If you were trying to do a RemoteDesktop-like connection to the phone, to see and interact with the OS visually, that would be a separate approach through the __VNC__ (Virtual Network Connection) protocol. This requires compatible applications on both the phone and your computer, and this is discussed in a different section of this article.
</div>
</div>

<div id="subSavingRAM" class="subsection">

## Saving RAM

Running Manjaro ARM Phosh `alpha2`, we first noticed that out of the 2GB of RAM on the system, we only had like 200MB to 400MB free, after the phone booted successfully.

At the moment, we're not using the Phone as a phone, because we don't have a SIM Card and didn't want to "fully commit" to the PinePhone while things are still in `alpha`. So, in this section we'll go through a few things we did to disable the Modem services of the phone that were just eating up RAM And CPU cycles, so we can get more out of the device as a pocket Linux system on WiFi.

First, to check the memory use you'll want to:

1. Open the __Terminal__ application.
1. Run the `top` command.
1. Hold `SHIFT` and press `M` (or send capital `M`).

This will sort the processes by RAM percentage usage, and the header in the display will show the actual megabytes of RAM that are available and in use, in total.

After verifying that Phosh, Phoc, and GNOME were all part of the phone's desktop-environment OS GUI, we started checking on the other running applications and then also used `systemctl` to see what `systemd` was running.
</div>

<div id="subDateTimeFailure" class="subsection">

## In Case of DateTime Failure

One thing we ran into was that `pacman` stopped working because none of the certificates could be verified.

We kept getting a message about an unknown GPG identity/key, so all installers that were downloaded will only provide the option to keep or delete the download, and installation would otherwise fail every time.

After inspecting the messages, we realized that somehow the System Clock was out of sync with the actual time. In fact, on 2020-08-12, the phone was displaying a date sometime in August in the year 2115. Since it's not 100 years into the future, right now, the certificate verification failed because the timestamps were too far apart, as configured.

Turning the [NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol) service/feature off then on, again, did _not_ work.

To fix the timestamp, you can do the following, because the system `hwclock` (Hardware Clock) should be accurate, since it would've been set when the NTP server was still accessible.

To double-check, run:

```bash
timedatectl
```

The output for the above should look like:

```bash
...
```

_[[TODO: Fill in output above]]_

To use the `hwclock` to set the other other clocks, you can run the following:

```bash
timedatectl set-ntp False
timedatectl set-time "`hwclock | awk -F'.' '{print $1}'`"
```

The above will turn-off the NTP check, and then use the date and truncated timestamp to fix the system time.

<aside>

__Note:__ Yes, that is some dark-magicks `awk` stuff that we definitely had to google. Basically, the `hwclock` shows you the time, but it does it with extra microsecond details that the `set-time` subcommand can't handle. So, using the backticks to internally pre-execute a command, we get the output of the `hwclock` and pipe it into `awk` where we split the response string on the period `.` character, and then printout only everything before the first period. Since there's only 1 period in the output, this is equivalent to truncating everything after the period, which makes the `hwclock` output compatible as an input to the `timedatectl set-time` command. Also note the judicious use of single-quotes so as to not break the double-quote parsing.

</aside>

Over time this will fall out of step with the actual time, so this is not intended as a longterm solution. However, since certificate verification and `gpg` key-checks will fail without a relatively correct system-time, this is necessary to keep certain things working. You can do the above and then continue to use `pacman` to install critical updates or new applications, and then on a reboot of the phone, you should try to see if you can get NTP re-enabled.

This is still only the `alpha2` release, so there are going to be hiccups with the system.
</div>

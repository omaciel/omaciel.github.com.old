---
layout: post
title: "Version Controlled Blogging"
categories: [blogging, programming]
tags: [jekyll, vcs]
---
{% include JB/setup %}

I have toyed with the idea of having a blog that was managed by one of the available versioning control systems out there, but I guess I was too lazy to leave the confort of my [WordPress](http://wordpress.org)-based blog which I have been maintaining for many years now. I also didn't want to take the time to figure out what the best way would be to migrate the contents of many years over to a new system, not wanting to lose all the history I've accumulated so far.

"Why user a VCS to manage a blog", you may ask? I guess because it would allow me to practice using either **git** or **mercurial** on a daily basis. I'm a firm believer that practice does make things perfect and I usually try to start a new project or write something that I depend on. This way I **have** to learn whatever the technology involved is or I may stuck for real. The idea is to rely (heavily) on this tool/project so that you don't have much of a choice and improve it or make it do what you need.

The second reason for doing this is actually based on a very bad experience I had when early last year (January 2011 to be exact) I decided to migrate my WordPress blog from my **DreamHost** server to my own virtual machine. I paid for a 300MB instance and to make a long story short, the system could not handle a couple of, what I assume to be, some very basic plugins, and the machine would reboot whenever I generated a bit of traffic with a blog post. I then switched to a **EC2 micro instance** that I got completely free for one year, thanks to a promotion that **Amazon** had, but that also proved to be not enough for my blogs. That is when I started considering the scenarion of serving static content instead of a more dynamic configuration.

So here goes my very first post, the first of many I hope. So far, I'm really digging [Jekyll](http://jekyllbootstrap.com) and am looking forward to using it every day!

<img src="/_images/jekyll-page-20120127.png" alt="First look" />

**UPDATE:** Had to modify the indentation of my paragraphs, as well as add an empty line between them so that they would render correctly.

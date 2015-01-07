Extending the default EC2 root partition: Follow up
###################################################
:slug: extending-the-default-ec2-root-partition-follow
:date: 2012-11-30 02:24
:category:
:tags: EC2, english

|EC2 wizard|

Just wanted to follow up on my previous
`post <http://ogmaciel.tumblr.com/post/36760809108/extending-the-default-ec2-root-partition-for-an>`__
in regards to how to resize the root partition of an EC2 instance. Turns
out that, once you’ve edited the root partition while in the launch
panel, you can then perform the resize command right away, as soon as
the instance is up and running and you have ssh’ed to it.

    [root@ip-aa-bb-cc-dd ~]# resize2fs /dev/xvde1

This is definitely better than what I thought one had to do to get a
bigger root partition.

.. |EC2 wizard| image:: https://lh4.googleusercontent.com/-_FwLIhjJu1s/ULaGxX9ch7I/AAAAAAACppg/KR_KZG-hLfM/s400/Screenshot%2520from%25202012-11-28%252015%253A15%253A38.png

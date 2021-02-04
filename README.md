# SSH-DSS-Key-Search-Script
This program searches through publicly released SSH-DSS keys to identify the private key equivalent to you public key.

The use of DSS keys in SSH authentication has been outdated for a while now, but many systems continue to use it in their internal networks. When you encounter such a server, you may be easily able to gain illicit access to it if you can read the system's authorized keys file. Then you can use this script to locally brute force the public key against the publicly available key-pair [database](https://github.com/g0tmi1k/debian-ssh). 

This is a very basic script to look through the publicly released DSS keys database for a private key equivalent to your supplied public key.

If you need it, the database can be downloaded from here: https://github.com/g0tmi1k/debian-ssh

    Usage: python3 finder.py <path to keys directory> <public-key file eg. id_rsa.pub> 

#!/usr/bin/python

from ipcalc import Network
from optparse import OptionParser
import subprocess


def main():
    parser = OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target ip in network to scan -t 192.168.192.0.10/24")
    parser.add_option("-w", "--timeout", dest="timeout", help="ping timeout, default: 2")
    (options, args) = parser.parse_args()

    if not options.target or not '/' in options.target:
        print "please specify a target: -t 192.168.0.10/24"
        return

    timeout = 2
    count = 1

    if options.timeout:
        timeout = options.timeout

    target = options.target
    net = Network(target)

    hosts_up = []
    for ip in Network(str(net.host_first()) + '/' + target.split('/')[1]):
        if subprocess.call(['ping', '-i', '0.2', '-w', str(timeout), '-c', str(count), str(ip)]) == 0:
            hosts_up.append(ip)

    print "Hosts up:"
    for host in hosts_up:
        print host

if __name__ == '__main__':
    main()

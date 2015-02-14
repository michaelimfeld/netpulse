#!/usr/bin/python

from ipcalc import Network
from optparse import OptionParser
import subprocess
import os


def main():
    parser = OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target ip in network to scan -t 192.168.192.0.10/24")
    parser.add_option("-w", "--timeout", dest="timeout", help="Ping timeout, default: 2")
    parser.add_option("-c", "--count", dest="count", help="Stop after sending <count> requests to host, default: 1")
    parser.add_option("-i", "--interval", dest="interval", help="Wait <interval> seconds between sending packet, default: 0.2")
    (options, args) = parser.parse_args()

    if not options.target or not '/' in options.target:
        print "please specify a target: -t 192.168.0.10/24"
        return

    interval = (options.interval if options.interval else '0.2')
    timeout = (options.timeout if options.timeout else '2')
    count = (options.count if options.count else '1')
    target = options.target
    net = Network(target)

    DEVNULL = open(os.devnull, 'w')
    for ip in Network(str(net.host_first()) + '/' + target.split('/')[1]):
        if subprocess.call(['ping', '-i', interval, '-w', timeout, '-c', count, str(ip)], stdout=DEVNULL) == 0:
            print str(ip)


if __name__ == '__main__':
    main()

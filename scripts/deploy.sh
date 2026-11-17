#!/bin/bash
mkdir -p ~/armsystem/outfs2/project
cp ~/Desktop/linux-embedded-project/client_and_servers/tcp_server.py ~/armsystem/outfs2/project/
cp ~/Desktop/linux-embedded-project/client_and_servers/monitor_server.py ~/armsystem/outfs2/project/
cp ~/Desktop/linux-embedded-project/client_and_servers/serial_server.py ~/armsystem/outfs2/project/
echo "Deployed."

# run to deploy the servers and related to the qemu machine, instead of manually
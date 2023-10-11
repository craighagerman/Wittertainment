#!/bin/bash
# AWS install script
sudo -u ec2-user -i <<'EOF'
cd /usr/local/bin
sudo mkdir ffmpeg && cd ffmpeg

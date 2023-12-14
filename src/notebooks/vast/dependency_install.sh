
################################################################################
# Install EITHER rclone OR AWS CLI tools
################################################################################
# rclone -------------------------------
wget -q https://downloads.rclone.org/v1.62.2/rclone-v1.62.2-linux-amd64.deb
dpkg -i rclone-v1.62.2-linux-amd64.deb

# AWS CLI tools
sudo apt update 
sudo apt install awscli


################################################################################
# Install whisper dependencies
################################################################################
# FFMPEG and Cython are needed as prerequisites to install the requirements
sudo apt update 
sudo apt install vim
sudo apt install cython3
sudo apt install ffmpeg


################################################################################
# Setup data directory
################################################################################
# mkdir /workspace
mkdir /workspace/podcasts
mkdir /workspace/transcripts



################################################################################
# Setup rclone and copy data
################################################################################
# copy or create rclone.conf file 
vi rclone.conf

# list folders in S3 to confirm it works
rclone --config rclone.conf lsd vast-s3:cph-wittertainment-ls/vast

# copy data to local
rclone --config rclone.conf copy vast-s3:cph-wittertainment-ls/vast/tmp/ /workspace/podcasts/ 




s3://cph-wittertainment-ls/vast

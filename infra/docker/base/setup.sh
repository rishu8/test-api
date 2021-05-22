# Set the timezone
rm /etc/localtime
ln -s /usr/share/zoneinfo/Australia/Sydney /etc/localtime

# Copy over the repo files.
cp etc/yum.repos.d/*.repo /etc/yum.repos.d/

# Activate the repo GPG keys.
rpm --import etc/pki/rpm-gpg/RPM-GPG*

# update the system
yum -y makecache --disableplugin=fastestmirror
yum -y update --disableplugin=fastestmirror


# Install extra packages
yum -y install --disableplugin=fastestmirror python36-devel python36-setuptools make nmap gcc-c++
yum -y clean --disableplugin=fastestmirror all

# Sort out the python3 link and grab pip.
python3 -m ensurepip
pip3 install --upgrade "pip<=20.2"

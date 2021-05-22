# Remove packages that we don't need for run-time
yum remove -y --disableplugin=fastestmirror gcc-c++ gcc
yum autoremove -y

cd /root
rm -r .cache

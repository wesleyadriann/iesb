echo "SLAVE ENTRYPOINT"
sleep 2
ping -c 3 master
echo "============================"
sleep 2

yes | ssh-keygen
ssh-copy-id $USER@master
echo "============================"
sleep 2

sudo mount master:/home/$USER/openmpi/pasta_compartilhada ~/openmpi/pasta_compartilhada
ls ~/openmpi/pasta_compartilhada

tail -f /dev/null
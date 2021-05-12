echo "MASTER ENTRYPOINT"
sleep 2
ping -c 3 slave
echo "============================"
sleep 2

yes | ssh-keygen
ssh-copy-id $USER@slave

echo 'teste pasta compartilhada' > ~/openmpi/pasta_compartilhada/teste.txt

tail -f /dev/null
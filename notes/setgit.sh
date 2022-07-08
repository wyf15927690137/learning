#!/bin/bash
git config --unset user.name
git config --unset user.email
git config --global user.name "yanfeiw"  
git config --global user.email "weiyanfei@sjtu.edu.cn" 

ssh-keygen -t rsa -C "weiyanfei@sjtu.edu.cn"    #input id_rsa_wyf for step1: name key1
ssh-keygen -t rsa -C "w1552160035@gmail.com"    #input id_rsa_wxz for step1: name key2

cat>config <<END
# wyf(weiyanfei@sjtu.edu.cn)
Host wyf
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_wyf
User wyf15927690137

# wxz(w1552160035@gmail.com)
Host wxz
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_wxz
User w1552160035
END

#how to use
#ssh -T -i id_rsa_wyf git@wyf
#git clone git@wyf:wyf15927690137/learncpp.git
#git push
#git xxx
#
#ssh -T -i id_rsa_wxz git@wxz
#git clone git@wxz:w1552160035/wyf_test.git

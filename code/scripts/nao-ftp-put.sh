#!/bin/sh
export SSHPASS=nao
sshpass -e sftp -oBatchMode=no -b - nao@$1 << !
    lcd $2
		cd $3
    put $4
    bye
    !
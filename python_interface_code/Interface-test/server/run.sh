#!/bin/sh
get_config_ini_value()
{
	if [ -f $1 ];then
		awk -F= -v tmpkey="$2"  ' $1==tmpkey {print $2} '  $1  ;
	else 
		
		echo NULL ;
	fi
}

TEST_LOCAL_IP="`ifconfig | grep "inet" | grep -v  "inet6" | grep -v  127.0.0.1 | awk -F: '{print $2}' | awk '{print $1}'`"
FUJIAN_PORT=`get_config_ini_value 		./config.ini fujian`
SHANGHAI_PORT=`get_config_ini_value 	./config.ini shanghai`
BEIJING_PORT=`get_config_ini_value 		./config.ini beijing`

echo $TEST_LOCAL_IP
echo "fujian_port	="$FUJIAN_PORT
echo "shanghai_port	="$SHANGHAI_PORT
echo "beijing_port	="$BEIJING_PORT


echo "start fujian"
cd ./server_fujian
python httpserver_fujian.py $TEST_LOCAL_IP $FUJIAN_PORT &
cd -

echo "start shanghai"
cd ./server_shanghai
python httpserver_shanghai.py $TEST_LOCAL_IP $SHANGHAI_PORT &
cd -

echo "start beijing"
cd ./server_beijing
python httpserver_beijing.py $TEST_LOCAL_IP $BEIJING_PORT &
cd -
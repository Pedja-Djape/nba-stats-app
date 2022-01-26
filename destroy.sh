for pid in  $(ps -ef | grep "postgres" | awk '{print $2}'); do
	        kill -9 $pid;
		    done

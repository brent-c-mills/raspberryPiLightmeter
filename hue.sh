#!/bin/bash

state=${1};

if [ ${state} = "On" ]; then
	curl -X PUT --data '{"on":true}' "http://${bridge_ip}/api/${user_id}/lights/${light_id}/state/";
else
	curl -X PUT --data '{"on":false}' "http://${bridge_ip}/api/${user_id}/lights/${light_id}/state/";
fi


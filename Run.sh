#!/bin/bash

# command to run:
# ./Run.sh 

echo "Running my script to start multiple services. . ." 

appiumServer1="appium server --config /Users/masoodahmed/Desktop/Appium_Parallel_Testing_Selenium_Grid_4/resources/servers/appium_1.yml"
appiumService2="appium server --config /Users/masoodahmed/Desktop/Appium_Parallel_Testing_Selenium_Grid_4/resources/servers/appium_2.yml"
runDocker="docker-compose -f /Users/masoodahmed/Desktop/Appium_Parallel_Testing_Selenium_Grid_4/docker-compose.yml up"
# runTetsingScript="npx wdio"

osascript -e "tell application \"Terminal\" to do script \"${appiumServer1}\""
echo "Running appium server 1 and Waiting for 5 seconds. . ."
sleep 5
osascript -e "tell application \"Terminal\" to do script \"${appiumService2}\""
echo "Running appium server 2 and Waiting for 5 seconds. . ."
sleep 5
osascript -e "tell application \"Terminal\" to do script \"${runDocker}\""
# echo "Running docker and waiting for it to initialize by Waiting for 30 seconds. . ."
# sleep 30
# osascript -e "tell application \"Terminal\" to do script \"${runTetsingScript}\""
# echo "Running testing script. . ."
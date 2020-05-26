*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           Selenium2Library
Library           date


*** Variables ***
${LOGIN URL}      http://localhost:7272
${BROWSER}        Chrome

*** Test Cases ***
Valid Login

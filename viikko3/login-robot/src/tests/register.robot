*** Settings ***
Resource  resource.robot
Test Setup    Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    sipuli  sipuli666
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle  kalle123
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    si  sipuli
    Output Should Contain    Username has to be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    sipuli666  sipuli
    Output Should Contain    Username should only contain letters a-z

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    sipuli  sipulili
    Output Should Contain  Password should contain at least one number

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
    
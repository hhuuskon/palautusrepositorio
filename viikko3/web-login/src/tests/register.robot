*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username     sipuli
    Set Password     sipuli666
    Set Confirmation     sipuli666
    Click Button    Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username    si
    Set Password    sipuli666
    Set Confirmation    sipuli666
    Click Button    Register
    Creating Should Fail With Message    Username has to be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username    sipuli
    Set Password    sipulipuli
    Set Confirmation    sipulipuli
    Click Button    Register
    Creating Should Fail With Message     Password should contain at least one number

    
    

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Creating Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    
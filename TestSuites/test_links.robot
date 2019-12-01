*** Settings ***
Documentation        My first mpulse tests
Variables           ../helpers/Constants.py
Library             ../Resources/Blog.py    ${outputdir}  ${BROWSER}    ${URL}
Library             Collections
Library             String



*** Variables ***
@{list}         Architecture  Infrastructure   Data    Design  Product   Culture   Internship
${github}       Grofers · GitHub
${twitter}      Grofers Engineering (@groferseng) | Twitter
${search_info}  Architecture


*** Test Cases ***
Test Title link
    click header
    capture screenshot
    ${val}=  get header txt
    should be equal as strings  ${val}   Learn all about engineering at Grofers

Test link headers
    :FOR  ${key}  IN  @{list}
    \       click header links   ${key}
    \       sleep  3
    \       ${val}=  get tilte of page
    \       ${contains}=    Run Keyword And Return Status    Should Contain    ${val}   ${key}
    \       should be true  ${contains}
    \       browser go back


Test Github Link
    click github
    sleep  3s
    capture screenshot
    switch to tab
    sleep  3s
    capture screenshot
    ${val}=  get tilte of page
    ${contains}=    Run Keyword And Return Status    Should Contain    ${val}   ${github}
    should be true  ${contains}



Test Twitter Link
    click twitter
    sleep  3s
    capture screenshot
    switch to tab
    sleep  3s
    capture screenshot
    ${val}=  get tilte of page
    ${contains}=    Run Keyword And Return Status    should be equal as strings    ${val}   ${twitter}
    should be true  ${contains}

Test Lambda Search Tab
    input_search_tab    ${search_info}
    sleep  2s
    capture screenshot
    ${val}=  get tilte of page
    ${contains}=    Run Keyword And Return Status    Should Contain  ${val}  ${search_info}
    sleep  3s
    should be true  ${contains}


Test all links
    ${list_href}=    find all links on page
    :FOR  ${key}  IN  @{list_href}
    \           go to url  ${key}
    \           capture screenshot
    \           ${title}=  get tilte of page
    \           log   ${list_href["${key}"]}
    \           ${contains}=    Run Keyword And Return Status    should contain   ${title}    ${list_href["${key}"]}
    \           should be true  ${contains}














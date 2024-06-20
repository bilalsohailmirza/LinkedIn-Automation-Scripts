# LinkedIn Automation Scripts

## Setup Requirements
##### Required Packages
* selenium
* linkedin_scraper

#### Installation
` pip install selenium`
<br>
` pip install linkedin_scraper`

#### Setting up the Environment
* Setting up chrome Profile Directory:
  * For Linux:
    
    ` options.add_argument(r"--user-data-dir=/home/username/.config/google-chrome")`
    <br>
    ` options.add_argument(r'--user-profile=Default')`

  * For Windows:
    
    `options.add_argument(r"--user-data-dir=C:\Users\username\AppData\Local\Google\Chrome\UserData")`
    `options.add_argument(r'--user-profile=name_of_the_profile')`


#### Required Modifications
  * #### Changes in the url in the messagin and connection script
      - Change the network part in the url to the network code of the account you are using (it will be visile in url handler when you go to serch in your linkedin account)
        
        ###### Example:
        `https://www.linkedin.com/search/results/people/?network=your_network_code&origin=FACETED_SEARCH&page=`

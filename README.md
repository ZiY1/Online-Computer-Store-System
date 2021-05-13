# Online-Computer-Store-System

**Online-Computer-Store-System** is a platform which customers can use to purchase workstations, computers, laptops, computer parts and everything related to computers. The components would be processed by store staff and delivered by delivery companies. 

There are 6 types of users in our system: browsers, registered customers, store clerks, store manager, delivery companies and computer companies. All registered accounts are able to view their account information. 
* Browsers are allowed to browse the platform including the listings of the computer, computer parts and discussion forum. They are unable to do anything else until they sign up for as a registered customer.
* Registered customers are able to browse the platform, make purchase options, browse purcahse history purchase, submit item review, report a review, file a complaint to store staff/computer company/delivery company. He/she can also view his/her personal account information including address and available balance. 
* Store clerks are able to deal with complaints directed to clerks, participate in discussion forum, edit taboo list and assign delivery company accordingly
* Delivery companies are able to deal with complaints directed to delivery companies, bid for purchase order and provide tracking information. 
* Computer companies are able to deal with complaints directed to computer companies
* Store managers are able to recommend 3 computer systems for browsers and customers, edit taboo list, view suspicious biddings, deal with unsatisfied complaints/reports and issue warnings.

A brief summary of how the system works:
The browser can registered to become a registered customer. The registered customer can place an order after credit card information and balance is added. Delivery companies then could bid for the order package. Once the clerk assigned a delivery company, the delivery company could deliver and update the status package. After the registered received the order, he/she can submit item review and rating. If the registered customer was dissatified with the item or shipment, he /she can file a complaint. The complaint party will try to resolve issues with the registered customer. The registered customer can report an inappropriate review. Lastly the manager will handle any unsatisified complaints and reports. For a variety of reasons, managers can issue warnings and ban a registered customer, store clerk, delivery company and computer company if 3 warnings are reached. 

This application is developped by Billy Davila, Ziyi Huang, Ai Hua Li and	Toma Suciu for our Software Engineering class.

## Privileged Users Accounts
Some of the priviledged users login information are provided below. However, all privileged users accounts login informations are located in the *csv_files/privileged_users* when you cloned the github repository. 

| Type_user    | Username            | Password |
| --------     | ------------------- | --------
| Super user   | admin@lenovo.com    | 123 |
| clerk        | ada_wong@lenovo.com | p |
| delivery     | ups@lenovo.com      | p |
| delivery     | on_track@lenovo.com | p |
| computer     | sony@lenovo.com     | p |

## Installation 
**Clone the repository**
```bash
https://github.com/billydavila/Online-Computer-Store-System.git
```
**Install necessary libraries**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following modules/libraries

```bash
pip install numpy
```

```bash
pip install pandas 
```

```bash
pip install tkinter
```

```bash
pip install Image
```

```bash
pip install xlrd
```

```bash
pip install openpyxl
```

```bash
pip install credit_card_checker
```

```bash
pip install smartystreets.py
```
## Copyright Disclaimer
We do not have any affiliations with Lenovo Corporation or anything related with the images used in the development of this small project.

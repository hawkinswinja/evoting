# iKURA online voting system
<img src="docs/images/ballot.png" alt="iKURA" width="400" height="300">

## Introduction

iKURA voting system is an online system that allows institutions to conduct elections online allowing students ot vote remotely and the results updated in real time. The system is designed for use in institutions of higher learning. 
This system allows for voter authentication based on stored data, fast voting process with easy to use interface, and real time votes updates.

For more information you can visit [**iKURA landing page**](https://hawkinswinja.github.io/evoting)<br>
Also check out my blog on the project at [Working My First Project](https://www.linkedin.com/pulse/working-my-first-project-gilbert-winja)<br>
linkedin profile: [hawkinswinja](https://linkedin.com/in/hawkinswinja/)

## Installation
### Prerequisites

**List of software and dependencies required to run the project.**
1. python3
2. pip
3. postgresql

### Getting Started
* Clone this repo locally
* Navigate into ikura-app directory
* Activate virtual environment (venv) and install the dependencies listed in requirements.txt
* Create a database
* Set the environment variables below
```bash
SECRET_KEY = application secret key
POSTGRES_USER = database username
POSTGRES_HOST = database HOST
POSTGRES_PASSWORD = database password
POSTGRES_DB = name of database created
```
* Start the app using
```bash
python run.py
```

## Usage

* Manually add voter data to the database. _Assumption is institutions already have this data stored_
* Login as the administrator and setup the electorate positions and candidates
    >> The admin can create and delete election positions for the election.<br> Without any position defined, the election ballot pages are designed to fail. <br>The candidates section allows the administrator to add candidates to the system

* Access the login access from your browser by typing in _localhost:5000/login_
    >> Students select their candidate by name and click the Vote button to confirm and post results. <br>
    >> The positions navigation allows voters to switch through different election positions ensuring they can vote only for the positions they want to<br>
    >> Clicking the E-results will display current results. Refreshing the page will update the results

## Contributing

Contributions to this project are highly appreciated in making the system much efficient in real time updates and UI.
Create a new pull request and I will gladly make the updates to the system

## Related projects

The following are simlar projects working on the same concept on digital voting platforms others even include Blockchain implementation; [evoting projects](https://github.com/topics/e-voting)

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License v3.0.
See the GNU General Public License for more details

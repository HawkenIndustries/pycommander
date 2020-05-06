![Commander Logo](https://www.kmccontrols.com/wp-content/uploads/2018/11/logo_kmccommander_white.svg)

---

**This library allows you to quickly and easily use the Commander Web API v1 via Python.**

We hope you build great add ons and applications with Commander and take charge on the platform for sustainability

We highly recommend using `pylint` and code editors with `Intelisense/AutoComplete` to quickly traverse through the classes and functions


## Table of contents

* [Installation](#installation)
* [Tokens](#tokens)
* [API](#api)
* [Networks](#networks)
* [Devices](#devices)
* [Points](#points)
* [Alarms](#alarms)
* [Trends](#trends)
* [Schedules](#schedules)
* [Projects](#projects)

---


## Installation 

---

**This package supports all Python 3 versions only**

```bash
    python -m pip install pycommander
```


## Tokens
---
Each request to Commander's Web API must be authenticated with a **JWT** token.

Use your login credentials to obtain a jwt token

```python
    from pycommander import CommanderToken

    def get_token():
        # Intiate the token class with your login credentials and license id of your project
        token = CommanderToken('email', 'password', 'licenseId')
        jwt = token.get_token()
        ## Save the token preferably in environment variables
```

## API

___

`pycommander` provides the `CommanderAPIClient` class that can be initiated with a valid `JWT` token 

```python
    import os
    from pycommander import CommanderAPIClient

    # Initialize CommanderAPIClient with token of your project
    # Refer above on how to get a token

    token  = os.environ.get('COMMANDER_TOKEN')
    building = CommanderAPIClient(token)

```

## Networks

The Networks class is a property of the API Client and has the following functions

```python
    token  = os.environ.get('COMMANDER_TOKEN')
    building = CommanderAPIClient(token)

    # variable building now has access to api endpoints of your project

    # Returns List of all network tag objects 
    networks = building.networks.get_all_networks()

    # Returns a network tag object associated with the id
    network = building.networks.get_network_details(network_id="id")

    # Create and return a network tag object

    network_obj = {
        "tags": {
            "dis": "Up18",
            "subnet": "10.3.3.18",
            "sourcePort": (0-65535 or None),
            "destinationPort": (0-65535 or None),
            "instanceMin": (0-4194303 or None),
            "instanceMax": (0-4194303 or None),
            "bacnetNetwork": (0-65535 or None),
            "destinationAddress": (0-255 or None),
            "instanceRange": False,
            "network": True
        },
        "tagTypes": {
            "dis": "Str",
            "subnet": "Str",
            "sourcePort": "Number",
            "destinationPort": "Number",
            "instanceMin": "Number",
            "instanceMax": "Number",
            "bacnetNetwork": "Str",
            "destinationAddress": "Str",
            "instanceRange": "Marker",
            "network": "Marker"
        }
    }

    n_network = building.networks.create_network(network_obj)

    # Update Network -  Update a network based on a network_id and network tag object

    u_network = building.networks.update_network(network_id="id", network_obj=network_obj)


    # Delete Network - Delete network taking network id as a parameter

    building.networks.delete_network(network_id="id")
```




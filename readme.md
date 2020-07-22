![Commander Logo](KMCLogo.png)

---

**This library allows you to quickly and easily use the Commander Web API v1 via Python.**

We hope you build great add ons and applications with Commander and take charge on the platform for sustainability

We highly recommend using `pylint` and code editors with `Intelisense/AutoComplete` to quickly traverse through the classes and functions


Table of contents

___

- [Installation](#installation)
- [Tokens](#tokens)
- [API](#api)
- [Networks](#networks)
- [Devices](#devices)
- [Points](#points)
- [Alarms](#alarms)
- [Trends](#trends)
- [Schedules](#schedules)
- [Projects](#projects)

---


## Installation 

---

**This package supports all Python 3 versions only**

```bash
    python -m pip install commanderiot
```


## Tokens
---
Each request to Commander's Web API must be authenticated with a **JWT** token.

Use your login credentials to obtain a jwt token

```python
    from commanderiot import CommanderToken
    import os
    def generate_token():
        # Intiate the token class with your login credentials and license id of your project
        token = CommanderToken('email', 'password', 'licenseId')
        jwt = token.get_token()
        ## Save the token preferably in environment variables
        return token
    
    token = generate_token()
    
    ## Save the token preferably in environment variables

    os.environ.set('COMMANDER_TOKEN', token) # This will only set the variable for current session to persist please 
```

## API

___

`commanderiot` provides the `CommanderAPIClient` class that can be initiated with a valid `JWT` token 

```python
    import os
    from commanderiot import CommanderAPIClient

    # Initialize CommanderAPIClient with token of your project
    # Refer above on how to get a token

    token  = os.environ.get('COMMANDER_TOKEN')

    if token is None:
        token = CommanderToken('email', 'password', 'licenseId').get_token()
    project = CommanderAPIClient(token)

```

## Networks
___

The Networks class is a property of the API Client and has the following functions

```python
    token  = os.environ.get('COMMANDER_TOKEN')
    project = CommanderAPIClient(token)

    # variable project now has access to api endpoints of your project

    # Returns List of all network tag objects 
    networks = project.networks.get_all_networks()

    # Returns a network tag object associated with the id
    network = project.networks.get_network_details(network_id="id")

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

    n_network = project.networks.create_network(network_obj)

    # Update Network -  Update a network based on a network_id and network tag object

    u_network = project.networks.update_network(network_id="id", network_obj=network_obj)


    # Delete Network - Delete network taking network id as a parameter

    project.networks.delete_network(network_id="id")
```

## Devices

___

Device class is a property of the API Client which can be accessed with `project.devices`

```python
    # Returns a list of all devices objects within the project 

    all_devices = project.devices.get_all_devices()

    # Returns a device taking in network id and device id as an argument
    device = project.devices.get_device_details(network_id="network_id", device_id="device_id")

    # Returns list of devices by model_name

    model_devices = project.devices.get_devices_by_model_name(model_name="model_name")

    # Delete a device from project using device id

    project.devices.delete_device(device_id="device_id")
```


## Points

___

Points class is a property of the API Client which can be accessed with `project.points`


```python
    # Points


    # Returns a list of points associated with the project
    points =  project.points.get_all_point_for_project()

    # Returns a list of points associated with the project filtered by list of id

    points_by_ids = project.points.get_points_by_ids(ids="List of ids")

    # Returns a list of points associated with the project filtered by device id

    points_by_device = project.points.get_points_for_device(device_id="device_id")

    # Return latest trend data by point id

    trends = project.points.get_point_trend_data_by_id(point_id="point_id")


    # set a point value by point id and desired current value

    project.points.set_point_value_by_id(point_id="point_id", cur_val="cur_val")
```

## Alarms
___

Alarms class is a property of the API Client which can be accessed with `project.alarms`

```python
    # Alarms


    # Returns a list of alarms in the project

    alarms = project.alarms.get_all_alarms()

    """
    Returns a list of alarm objects for the given date and timeframe
    :param time_frame Any of ('min', 'hour', 'day')
    :param date  Date in the format of YYYY/DD/MM
    """

    alarms_by_time_frame = project.alarms.get_alarms_by_time_frame(time_frame="day", date="2019/07/07")


    # Create Alarm

    alarm_object = {
    "tags": {
        "dis": "Room 206 COOL_SP",
        "value": 60,
        "type": "range",
        "priority": "info",
        "threshold": 60,
        "ackRequired": "",
        "deviceRef": "",
        "pointRef": "BV39",
        "dynamicDeviceRef": None,
        "dynamicPointRef": None,
        "rangeType": "low",
        "range": 55,
        "alarm": True,
        "message": None,
        "group": None
    },
    "tagTypes": {
        "dis": "Str",
        "value": "Number",
        "type": "Str",
        "priority": "Str",
        "threshold": "Number",
        "ackRequired": "Bool",
        "deviceRef": "Ref",
        "pointRef": "Ref",
        "dynamicDeviceRef": "Ref",
        "dynamicPointRef": "Ref",
        "rangeType": "Str",
        "range": "Number",
        "alarm": "Marker",
        "message": "Str",
        "group": "Str"
    }
    }

    # New alarm

    """
    Update an alarm for the project
    alarm_id Id of alarm object
    :param alarm_object  Alarm Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#743e6adf-3766-5a65-1bab-76132b49d2d4

    Example provide above
    """
    new_alarm = project.alarms.create_alarm(alarm_object=alarm_object)

    # Update alarm by alarm id

    updated_alarm = project.alarms.update_alarm(alarm_id="alarm_id", alarm_object=alarm_object)


    # Delete alarm by alarm id

    project.alarms.delete_alarm(alarm_id="alarm_id")

```

## Trends

___

Trends class is a property of the API Client which can be accessed with `project.trends`


```python

    # Trends

    # Returns a list of all trend settings for the project

    trends = project.trends.get_all_trends_settings()


    # param trend_object Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#d4b79184-c18e-5923-1ac7-1827d74abfb7

    trend_object = {} 


    # Create a trend setting 

    new_trend = project.trends.create_trend_settings(trend_object=trend_object)

    # Delete trend setting

    project.trends.delete_trend(trend_id="trend_id")

```

## Schedules
___

Trends class is a property of the API Client which can be accessed with `project.schedules`

```python
    # Schedules


    # Returns a list of schedules

    schedules = project.schedules.get_all_schedules()

    # Create schedule

    schedule_object = {} # schedule Haystack Object. Refer to https://api.docs.kmccommander.com/?version=latest#7549d641-dee7-aa4e-34d5-f58188f72ba1

    new_schedule = project.schedules.create_schedule(schedule_object=schedule_object)


    # Update schedule

    updated_schedule = project.schedules.update_schedule(schedule_id = "schedule_id", schedule_object=schedule_object)
```

## Projects
___

Projects class is a property of the API Client which can be accessed with `project.projects`


```python
    # Project 

    # Returns Project update logs (CRUD) operations

    timestamp = 1589246791057 # Unix epoch value

    logs = project.projects.get_update_logs(timestamp=timestamp)
```








# Repair cafe shop — Neighborhood Repair Café Log

Coffee lovers, think green: don't throw away what can be repaired. 

## Concept

A small community repair café app for cataloguing items brought in for repair, 
assigning volunteer repairers, and tracking each repair ticket. 
It needs no user accounts: owners and repairers are represented as ordinary domain data.

## It is going to be composed of three apps and several _models_:
1. catalog - handles received coffee machines by category and item
  - `Category`: unique name and description; `__str__`
  - `Item`: owner name, category (`ForeignKey`), brand, problem description,
optional photo URL.
2. `volunteers` - handles voluntary repair technicians
  - `Repairer`: name, skill choice, phone, optional email, and optional notes.
3. `repairs`
  - `RepairTicket`: unique generated code, item (`ForeignKey`), serial number,
status choices (`received`, `in_progress`, `fixed`, `unfixable`),
intake date, diagnosis, non-negative cost estimate,
and repairers (`ManyToManyField`).

## Setup and configuration
Needed steps to prepare the app: 
1. Install dependencies:
```shell
pip install -r requirements.txt
```
2. Make migrations:
```shell
pyhton manage.py migrate
```

TODO: project requirements, credentials, environment variables

# Documentation

## Tutorial Content Overview

---

Docker:

    - [x] Django
    - [x] Redis
    - [x] Celery
    - [x] Celery Beat
    - [x] Flower
    - [x] Visual Studio Code Extension

Database:

    - [x] Validators
    - [x] Field refactoring
    - [x] Add new models

Testing

    - [ ] Unit testing Promotion app
    - [ ] Unit testing Celery

Promotion App Scope: 

    - [x] Add a new promotion to selectable individual products
    - [x] Bulk apply discount as a percentage to all chosen products in a promotion
    - [x] Manually override discount price to allow users to define a custom price
    - [x] Promotion prices must be auditable over multiple promotions
    - [x] Specify a timescale (start, end) for the promotion to be active
    - [x] Promotions can be manually started or stopped
    - [x] Promotions can be, if flagged, automatically started or stopped based on the promotion timescale
    - [x] Should allow selection of multiple promotion types (User Defined, Coupons)
    - [x] A daily automated scheduled task should manage promotion activation (run at 1am every day)

API:

    - [ ] API endpoint refactor to include promotion price


    

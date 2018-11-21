# SendIT

[![Build Status](https://travis-ci.org/leni1/send-it-app.svg?branch=develop)](https://travis-ci.org/leni1/send-it-app/)
[![Coverage Status](https://coveralls.io/repos/github/leni1/send-it-app/badge.svg)](https://coveralls.io/github/leni1/send-it-app)
[![Maintainability](https://api.codeclimate.com/v1/badges/e993b64734b96cd0f40b/maintainability)](https://codeclimate.com/github/leni1/send-it-app/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e993b64734b96cd0f40b/test_coverage)](https://codeclimate.com/github/leni1/send-it-app/test_coverage)

## Project Overview

SendIT is a courier service that helps users deliver parcels to different destinations.

### Required Features

1. Users can create an account and log in.
2. Users can create a parcel delivery order.
3. Users can change the destination of a parcel delivery order.
4. Users can cancel a parcel delivery order.
5. Users can see the details of a delivery order.
6. Admin can change the **status** and **present** **location** of a parcel delivery order.
7. The application should display a Google Map with Markers showing the **pickup location** and the **destination**.

### Optional Features

1. The application should display a Google Map with a line connecting both Markers (**pickup location** and the **destination**).
2. The application should display a Google Map with computed travel distance and journey duration between the **pickup location** and the **destination**.
3. The user gets real-time email notification when Admin changes the **status** of their parcel or when Admin changes the **present location** of their parcel.

#### Note

1. The user can only cancel or change the **destination** of a parcel delivery when the parcel’s **status** is yet to be marked as **delivered**.
2. Only the user who created the parcel delivery order can cancel the order.


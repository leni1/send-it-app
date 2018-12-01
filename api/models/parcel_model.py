from datetime import datetime


class Parcel:
    """Parcel class

    Parcel class that has the attributes we wish to store
    about parcels.

    Attributes:
        par_id: The parcel's unique integer id.
        placed_by: The integer id of the user who has placed the parcel
        delivery order.
        weight: The parcel's weight as a float type.
        weight_metric: The metric in that the weight of the parcel is given.
        delivered_on: Date the parcel was delivered.
        status: The parcel's delivery status which can be any of the following:
        'placed', 'transiting' or 'delivered'.
        orig: Where the parcel is coming from
        dest: Where the parcel is to be delivered to."""

        par_id = attr.ib(validator=attr.validators.instance_of(int))
        placed_by = attr.ib(validator=attr.validators.instance_of(str))
        weight = attr.ib(validator=attr.validators.instance_of(float))
        weight_metric = attr.ib(validator=attr.validators.instance_of(str))
        delivered_on = attr.ib(validator=attr.validators.instance_of(datetime))
        status = attr.ib(validator=attr.validators.instance_of(str))
        origin = attr.ib(validator=attr.validators.instance_of(str))
        dest = attr.ib(validator=attr.validators.instance_of(str))

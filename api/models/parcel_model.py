class Parcel:
    """Parcel class

    Parcel class that has the attributes we wish to store
    about parcels.

    Attributes:
        par_id: The parcel's unique id.
        placed_by: The id number of the user who has placed the parcel
        delivery order.
        weight: The parcel's weight as a float type.
        weight_metric: The metric in that the weight of the parcel is given.
        delivered_on: When the parcel was delivered.
        status: The parcel's delivery status which can be any of the following:
        'placed', 'transiting' or 'delivered'.
        orig: Where the parcel is coming from
        dest: Where the parcel is to be delivered to."""

    def __init__(self, par_id, placed_by, weight, weight_metric, delivered_on, status, orig, dest, current_loc):
        """Initializes the class with its attributes"""

        self.par_id = par_id
        self.placed_by = placed_by
        self.weight = weight
        self.weight_metric = weight_metric
        self.delivered_on = delivered_on
        self.status = status
        self.orig = orig
        self.dest = dest

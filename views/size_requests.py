import sqlite3
import json
from models import Size

def get_all_sizes():

    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            si.id,
            si.size,
            si.price
        FROM Size si
        """)

        # Initialize an empty list to hold all size representations
        sizes = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an size instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # size class above.
            size = Size(row['id'], row['size'], row['price'])

            sizes.append(size.__dict__)

    return sizes


def get_single_size(id):
    # Variable to hold the found size, if it exists
    requested_size = None

    # Iterate the SIZES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size

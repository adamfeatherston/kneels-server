import sqlite3
import json
from models import Metal


def get_all_metals():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM Metal m
        """)

        # Initialize an empty list to hold all metal representations
        metals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an metal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Metal class above.
            metal = Metal(row['id'], row['metal'], row['price'])

            metals.append(metal.__dict__)

    return metals

    # Function with a single parameter


def get_single_metal(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            m.id,
            m.metal,
            m.price
        FROM Metal m
        WHERE m.id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        metal = Metal(
            data["id"],
            data["metal"],
            data["price"],
                       
        )

        return metal.__dict__


def update_metal(id, new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Metal
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """,
            (
                new_metal["metal"],
                new_metal["price"],
                id,
            ),
        )

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
import sqlite3
import json
from models import Order
from models import Metal
from models import Size
from models import Style


def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            o.id,
            o.timestamp,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.metal metal_metal,
            m.price metal_price,
	        si.size size_size,
            si.price size_price,
	        st.style style_style,
            st.price style_price
        FROM [Order] o
        JOIN Metal m
            ON m.id = o.metal_id
        JOIN Size si 
	        ON si.id = o.size_id
        JOIN Style st
            ON st.id = o.style_id
        """
        )

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row
            order = Order(
                row["id"],
                row["timestamp"],
                row["metal_id"],
                row["size_id"],
                row["style_id"],
            )
            # Create a Metal instance from the current row
            metal = Metal(row["id"], row["metal_metal"], row["metal_price"])
            # Create a Size instance from the current row
            size = Size(row["id"], row["size_size"], row["size_price"])
            # Create a Size instance from the current row
            style = Style(row["id"], row["style_style"], row["style_price"])

            # Add the dictionary representation of the metal, size, style to the order
            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            # Add the dictionary representation of the order to the list
            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        SELECT
            o.id,
            o.timestamp,
            o.metal_id,
            o.size_id,
            o.style_id   
        FROM [Order] o
        WHERE o.id = ?
        """,
            (id,),
        )

        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        order = Order(
            data["id"],
            data["timestamp"],
            data["metal_id"],
            data["size_id"],
            data["style_id"],
            
        )

        return order.__dict__


def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO [Order]
            ( timestamp, metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ?, ? );
        """,
            (
                new_order["timestamp"],
                new_order["metal_id"],
                new_order["size_id"],
                new_order["style_id"],
            )
        )

        id = db_cursor.lastrowid

        new_order["id"] = id

    return new_order 

def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM [Order]
        WHERE id = ?
        """,
            (id,),
        )


def update_order(id, new_order):
    # Iterate the CUSTOMORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(CUSTOMORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            CUSTOMORDERS[index] = new_order
            break

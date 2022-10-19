import sqlite3
import json
from models import Style

def get_all_styles():

    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            st.id,
            st.style,
            st.price
        FROM Style st
        """)

        # Initialize an empty list to hold all style representations
        styles = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an style instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # style class above.
            style = Style(row['id'], row['style'], row['price'])

            styles.append(style.__dict__)

    return styles



def get_single_style(id):
    # Variable to hold the found style, if it exists
    requested_style = None

    # Iterate the STYLES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style

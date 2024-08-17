"""Get data from database."""

import os
from pypika import Query, Table
import pypika.functions as fn
import sqlite3

from util import ModelException, dict_factory


ENV_VAR = "DB"


def connect(path = None):
    """Connect to database."""
    if path is None:
        path = os.getenv(ENV_VAR)
    if not path:
        raise ModelException(f"Environment variable {ENV_VAR} not set")
    connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = dict_factory
    return connection


def add_staff(personal, family):
    """Add staff member, generating staff ID."""
    staff = Table("staff")
    subquery = Query.from_(staff).select(fn.Max(staff.staff_id) + 1)
    query = Query.into(staff).insert(subquery, personal, family)
    try:
        connection = connect()
        connection.execute(str(query))
        connection.commit()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def all_staff():
    """Get all staff."""
    staff = Table("staff")
    query = Query.from_(staff).select(staff.staff_id, staff.personal, staff.family)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))

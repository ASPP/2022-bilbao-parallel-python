import time

pwdb = {
    "pelita": "81d",
    "aspp": "8d91",
    "ASPP": "1djk",
}


def check_user_exists(username):
    """
    Check whether a user with `username` exists in the database.

    Parameters
    ----------
    username : str
        Username to check.

    Returns
    -------
    bool
        Whether the user exists in the database.
    """
    time.sleep(0.5 * len(username))  # mimick slow server-side processing

    return username in pwdb

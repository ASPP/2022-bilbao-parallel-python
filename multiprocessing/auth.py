import sys
import time

pwdb = {
    "pelita": "81d",
    "aspp": "8d91",
    "ASPP": "1djk",
    "tiziano": "asd,123",
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
    wait = len(username)
    while wait > 0:
        # mimick slow server-side processing
        time.sleep(min(wait, 1))
        sys.stdout.write('.')
        sys.stdout.flush()
        wait -= 1

    return username in pwdb

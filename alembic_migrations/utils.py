import os


def prevent_dangerous_downgrade():
    downgrade_db = os.getenv("DowngradeDB", "False")
    if downgrade_db != "True":
        raise Warning("You are trying to apply a downgrade to the database which may cause irreversible damage."
                      "If the downgrade was intentional, please, set up the env variable \"DowngradeDB\" to True"
                      f"Not applying downgrade as the value is set to \"{downgrade_db}\"")

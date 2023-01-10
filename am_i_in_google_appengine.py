import os


def am_in_appengine() -> bool:
    """
    This function detects whether it's running in a local environment or in Google App Engine.

    This utilizes the $GAE_ENV env variable. If you have it configured in your local machine, ensure that it doesn't start with: 'standard'.

    Returns:
        bool: True if running in Google App Engine, False otherwise
    """
    # Source https://cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app?tab=python#detecting_application_runtime_environment
    return bool(os.getenv("GAE_ENV", "").startswith("standard"))

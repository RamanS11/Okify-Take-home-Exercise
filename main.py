def get_project_status(inputStatus: list):
    """
    Function that output the project status following the logic defined in the exercise statement.
    :param inputStatus: List containing the status of all the tasks of a project (from 0 to N)
    :return: One of the values stated by dictStatus.
    """

    # Make sure input value given is a list
    assert type(inputStatus) is list, "Input variable must be a list"

    # If all tasks are in the same status, the project is also in that status
    if len(set(inputStatus)) == 1:
        return inputStatus[0]

    # If some task is Missing info, the project's status is also Missing info
    if "Missing info" in inputStatus:
        return "Missing info"

    # If some task is Processed, the project's status is also Processed
    if "Processed" in inputStatus:
        return "Processed"

    # The project status is Activated only if all tasks are Activated or Canceled
    if all(status in ["Activated", "Canceled"] for status in inputStatus):
        return "Activated"

    # In all other cases, the project is Requested
    return "Requested"


if __name__ == "__main__":
    get_project_status(["Activated"])

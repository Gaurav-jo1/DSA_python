def activity_selection(activities):
    # Sort activities based on their end times
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # The first activity always gets selected
    selected_activities = [sorted_activities[0]]

    # The end time of the last selected activity
    last_end_time = sorted_activities[0][1]

    for activity in sorted_activities[1:]:
        if activity[0] >= last_end_time:
            selected_activities.append(activity)
            last_end_time = activity[1]

    return selected_activities

# List of activities with their start and end times
activities = [(1, 3), (2, 4), (0, 6), (5, 7), (8, 9), (5, 9)]

# Call the function and print the result
selected_activities = activity_selection(activities)
print("Selected activities:", selected_activities)

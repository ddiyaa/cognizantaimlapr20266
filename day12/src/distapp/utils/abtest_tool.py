from statsig import statsig_event,statsig,statsig_user

def abtest_tool():
    # Initialize Statsig with your server secret key
    statsig.initialize("secret-uOj2IK6AXOoOgplkFEVAx97gmDTff0ammwjQePsWxLS")
    for i in range(10):
        # Create a user object with custom properties
        user = statsig_user.User(
            user_id=f"user_{i}",
            email=f"user_{i}@example.com"
        )
        # Log an event for the user
        statsig_event.log_event(user, "test_event", {"value": i})
        # Check if the user is in the experiment
        in_experiment = statsig.check_gate(user, "experiment_name")
        if in_experiment:
            print(f"User {i} is in the experiment")
        else:
            print(f"User {i} is not in the experiment")
    #flush the events to ensure they are sent to Statsig
    statsig.flush()
    #shutdown the Statsig client to clean up resources
    statsig.shutdown()

if __name__ == "__main__":
    abtest_tool()

from prefect import flow
"""
In this example, the flow is deployed as a Prefect Serve deployment using 'flow_name.server()' command.
Cron jobs are usually included in this type of deployment.
"""

@flow
def my_flow():
    print("Hello, Prefect!")


if __name__ == "__main__":
    my_flow.serve(name="my-first-deployment", cron="* * * * *")
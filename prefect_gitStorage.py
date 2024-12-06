from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "world"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/mfonekpo/deploy-test.git",
        entrypoint="path/to/your/flow.py:your_flow_function"
    ).deploy(
        name="my-deployment",
        work_pool_name="my-work-pool",
    )

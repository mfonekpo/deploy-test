from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "world"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/mfonekpo/deploy-test.git",
        entrypoint="prefect_gitStorage.py:my_flow",
    ).deploy(
        name="mygithub-deployment",
        work_pool_name="managedPrefect-workpool",
    )

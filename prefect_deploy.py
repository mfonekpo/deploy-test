from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "world"):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    my_flow.deploy(
        name="my-deployment",
        work_pool_name="docker-workpool",
        image="my-docker-image:dev",
        push=False
    )

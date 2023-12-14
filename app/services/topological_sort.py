from app.resources.data import src

dependencies = []


async def get_tasks_order(build_name: str) -> list:
    build_tasks: list = src.builds.get(build_name, [])

    if not build_tasks:
        raise Exception("There is no such build")

    result = []

    for task in build_tasks:
        node = await sort_task(task)
        dependencies.append(node)
        result.extend(dependencies)
        dependencies.clear()

    return result


async def sort_task(node):
    children = src.tasks[node]
    if not children:
        return node

    for child in children:
        completed_node = await sort_task(child)
        dependencies.append(completed_node)

    return node

import yaml

from app.logger.logger import logger


class ResourseData:
    def __init__(self):

        with open("app/resources/config.yaml") as config:
            cfg = yaml.safe_load(config)

        self._tasks_path: str = cfg['paths']['tasks']
        self._builds_path: str = cfg['paths']['builds']
        self.tasks: dict = {}
        self.builds: dict = {}

    async def get_data_tasks(self) -> None:
        data: dict = await get_data_form_file(self._tasks_path)
        self.tasks = {item['name']: item['dependencies'] for item in data['tasks']}
        logger.success("Tasks has been read")

    async def get_data_builds(self) -> None:
        data: dict = await get_data_form_file(self._builds_path)
        self.builds = {item['name']: item['tasks'] for item in data['builds']}
        logger.success("Builds has been read")


async def get_data_form_file(path: str) -> dict:
    with open(path) as file:
        data = yaml.safe_load(file)
    return data

src = ResourseData()


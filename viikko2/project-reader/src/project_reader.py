from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = toml.loads(content)
        #print(parsed_toml)
        name = parsed_toml["tool"]["poetry"]["name"]
        description = parsed_toml["tool"]["poetry"]["description"]
        authors = parsed_toml["tool"]["poetry"]["authors"]
        dependencies = parsed_toml["tool"]["poetry"]["dependencies"]
        development_dependencies = parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]
        project_entry = Project(name, description, authors, dependencies, development_dependencies)
        return project_entry

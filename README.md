# Topological-Sorting
***
### About service
Microservice for resolving the order of execution of tasks of the required build.
***
### About algorithm
The Depth-first (DFS) search algorithm is used to resolve the order of tasks. The time complexity of DFS is O(V + E), 
where V represents the number of vertices and E represents the number of edges in the graph.
The space complexity of DFS is O(V), where V represents the number of vertices in the graph.
***
### Launch and installation

Go to the working directory and run Git command
```commandline
git clone https://github.com/VolokidoIra/Topological-Sorting.git
```
Go to the project directory and run app
```commandline
cd Topological-Sorting
docker build -t topological_sorting . 
docker run -d --name topological_sorting_app -p 80:80 topological_sorting 
```
To test, follow the [http://127.0.0.1:80/docs](http://127.0.0.1:80/docs)
***
### Project structure
    Topological-Sorting/   # Root directory.
    |- app/                # App directory.
     |- core/              # Folder with settings.
     |- logger/            # Logger configuration
     |- resources/         # Working with resources
     |- routers/           # Working with API
      |- v1/               # API
      |- validators/       # Validators for requests
     |- schemas/           # Schemas
     |- services/          # Business logic of the application
    |- builds/             # Data files for work
    |- logs/               # Application operation logs
***
Author 
[Volokido Irina](https://www.linkedin.com/in/ira-volokido-292978231/)

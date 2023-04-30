## Implementation of "A cascade information diffusion based label propagation algorithm for community detection in dynamic social networks"

### Team members: 
1. Anuj Yadav
2. Nrittik Sarmah
3. Shashank Maurya
4. Chandrakanta Choudhury
5. Udit Talukdar

### Dependencies/Packages
1. networkx
2. numpy
3. python-louvain
4. scikit-learn

## Steps for running the algorithm:
1. Go inside the `src` folder in your terminal/Open your code editor inside the `src` folder.
2. To add a new dataset, go into the dataset folder and create a folder by the name of your dataset.
3. Add 2 files inside your dataset, `t1.txt` - for the edgeslist of the network at the 1st timestamp and `input.txt` - for the entire input of nodes, timestamps and the edgeslist of each timestamp.
4. Go to the project notebook, import `coderunner` and call `run_cidlpa` by passing in the name of your dataset.

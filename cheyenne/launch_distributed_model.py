from smartsim import Experiment
from smartsim.settings import MpirunSettings

"""
Create a simple model that runs a hello_world.c program

Make sure to have openmpi loaded (module load openmpi)

this example runs in an interactive allocation. When using openmpi
on cheyenne, be sure to include the number of `mpiprocs` in your
allocation line.

i.e. qsub -l select=2:ncpus=20:mpiprocs=20 -l walltime=01:00:00 -A <account> -q premium -I
"""

exp = Experiment("simple", launcher="pbs")

# see https://www.craylabs.org/docs/api/smartsim_api.html#mpirunsettings
mpirun = MpirunSettings("hello") # hello is name of executable
mpirun.set_tasks(40)

# create a model with the settings we have defined
# this is like pythonic reference to a running job
hello_world = exp.create_model("hello_world", mpirun)

# create directory for output files of this model
exp.generate(hello_world, overwrite=True)

# start the model and block until completion
exp.start(hello_world, block=True, summary=True)

# get the status (should be Completed because we set block=True)
print(f"Model status: {exp.get_status(hello_world)}")


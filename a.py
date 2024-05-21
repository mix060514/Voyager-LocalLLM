
from voyager import Voyager
openai_api_key = "dummy"


# First instantiate Voyager with skill_library_dir.
voyager = Voyager(
    mc_port=59341,
    openai_api_key=openai_api_key,
    # skill_library_dir="ckpt_dir2", # Load a learned skill library.
    ckpt_dir="ckpt_dir_auto_1", # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
    resume=False, # Do not resume from a skill library because this is not learning.
    ollama_model_name='codeqwen',
    use_ollama=True,
)

# Run task decomposition
voyager.learn()
# task = "Craft a word pickaxe" # e.g. "Craft a diamond pickaxe"
# sub_goals = voyager.decompose_task(task=task)
# voyager.inference(sub_goals=sub_goals)

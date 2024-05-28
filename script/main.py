from voyager import Voyager

if __name__ == '__main__':
    openai_api_key = "dummy"

    # First instantiate Voyager with skill_library_dir.
    voyager = Voyager(
        mc_port=33913,
        openai_api_key=openai_api_key,
        # skill_library_dir="skill_library/trial1", # Load a learned skill library.
        ckpt_dir="ckpt_dirs/ckpt8", # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
        resume=False, # Do not resume from a skill library because this is not learning.
        # resume=True,
        ollama_model_name='codeqwen',
        use_ollama=True,
    )
    # Run task decomposition
    voyager.learn()
    # task = "Craft a word pickaxe" # e.g. "Craft a diamond pickaxe"
    # sub_goals = voyager.decompose_task(task=task)
    # voyager.inference(sub_goals=sub_goals)

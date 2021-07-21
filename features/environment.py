def after_scenario(context, feature):
    import os
    os.remove("test.txt")

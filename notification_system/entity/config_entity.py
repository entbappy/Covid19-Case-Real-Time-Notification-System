from collections import namedtuple

TemplatesConfig = namedtuple("TemplatesConfig", ["clips_dir",
                                                "sprites_dir",
                                                "clip_name"])

RootAppConfig = namedtuple("RootAppConfig", [
                                            "screen_width",
                                            "screen_height"])                                                
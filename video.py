"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, Amazing_cats: str, amazing_cats_video_id: str, cat_animal, Sequencestr):
        """Video constructor."""
        self._title = Amazing_cats
        self._video_id = amazing_cats_video_id
        
        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(cat_animal)
    def __init__(self, Another_Cat_Video: str, another_cat_video_id: str, cat_animal, Sequencestr):
        """Video constructor."""
        self._title = Another_Cat_Video
        self._video_id = another_cat_video_id
        self._tags = tuple(cat_animal)
    def __init__(self, Funny_Dogs: str, funny_dogs_video_id: str, dog_animal, Sequencestr):
        """Video constructor."""
        self._title = Funny_Dogs
        self._video_id = funny_dogs_video_id
        self._tags = tuple(dog_animal)
    def __init__(self, Life_at_Google: str, life_at_google_video_id: str, google_career, Sequencestr):
        """Video constructor."""
        self._title = Life_at_Google
        self._video_id = life_at_google_video_id
        self._tags = tuple(google_career)
    def __init__(self, Video_about_nothing: str, nothing_video_id: str, Sequencestr):
        """Video constructor."""
        self._title = Video_about_nothing
        self._video_id = nothing_video_id



    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags





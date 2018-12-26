class Novel:
    """A container the novel information and methods involving information for novels"""

    def __init__(self, title, latest_chapter, current_chapter):
        """Initialize a novel with parameters"""
        self.title = title
        self.latest_chapter = latest_chapter
        self.current_chapter = current_chapter

    def new_update(self):
        """Compares latest novel with bookmark, returns true if there is a new update"""
        if self.latest_chapter != self.current_chapter:
            return True
        return False

    def printNovel(self):
        print(self.title, self.latest_chapter, self.current_chapter)

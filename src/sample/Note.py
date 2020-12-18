class Note:
    def __init__(self, name, note):
        # name
        if not name:
            raise Exception("Empty value")
        if not isinstance(name, str):
            raise Exception("Not string")
        self.name = name

        # note
        if not isinstance(note, float):
            raise Exception("Not float type")
        if not 2 <= note <= 6:
            raise Exception("Value not from 2 to 6")
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
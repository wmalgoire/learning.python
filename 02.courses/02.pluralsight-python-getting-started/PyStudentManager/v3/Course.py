class Course:

    school_name = "Unknown"

    def __init__(self, name, id= 666):
        self.course_name = name
        self.course_id= id

    def __str__(self):
        return "{0} course: {1}".format(self.school_name, self.course_name).title()

    def get_name_capitalized(self):
        return self.course_name.title()



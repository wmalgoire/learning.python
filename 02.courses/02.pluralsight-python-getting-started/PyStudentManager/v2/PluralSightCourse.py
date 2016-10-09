from Course import Course


class PluralSightCourse(Course):

    school_name = "PluralSight"

    def get_name_capitalized(self):
        base_value = super().get_name_capitalized()
        return f"[PS] {base_value}"

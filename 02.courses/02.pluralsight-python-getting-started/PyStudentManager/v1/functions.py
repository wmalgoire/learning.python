Courses = []


def get_courses_list():
    courses_list = []
    for course in Courses:
        courses_list.append(course)
    return courses_list


def print_courses_list():
    courses_list = get_courses_list()
    for course in courses_list:
        print("Course {0}".format(course))


# def add_course(course_name, course_id=None):
#    courses.append({"name": course_name.title(), "id": course_id})

# Lambda function example
add_course = lambda course_name, course_id=None: Courses.append(
    {"name": course_name.title(), "id": course_id})


def save_course(course):
    try:
        f = open("courses.txt", "a")
        f.write(course + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("courses.txt", "r")
        # for course_name in f.readlines():
        for course_name in read_courses(f):
            add_course(course_name)
        f.close()
    except Exception:
        print("Could not read file")


def read_courses(f):
    """Example of generator function: recreate the f.readlines()"""
    for line in f:
        yield line.strip()


read_file()
print_courses_list()

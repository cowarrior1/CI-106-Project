class Discussion:
    def __init__(self):
        self.owners = []
        self.followers = []
        self.responses = []
        self.classrooms = []
    def __init__(self, owners):
        self.owners = owners
        self.followers = []
        self.responses = []
        self.classrooms = []
    def __init__(self, owners, followers, responses, classes):
        self.owners = owners
        self.followers = followers
        self.responses = responses
        self.classrooms = classes
    def get_owners(self):
        return self.owners
    def set_owners(self, owners):
        self.owners = owners
    def get_followers(self):
        return self.followers
    def set_followers(self, followers):
        self.followers = followers
    def get_responses(self):
        return self.responses
    def set_responses(self, responses):
        self.responses = responses
    def get_classrooms(self):
        return self.classrooms
    def set_classrooms(self, classrooms):
        self.classrooms = classrooms
    def add_owner(self, owner):
        self.owners = self.owners.append(owner)
    def add_follower(self, follower):
        self.followers = self.followers.append(follower)
    def add_response(self, response):
        self.responses = self.responses.append(response)
    def add_classroom(self, classroom):
        self.classrooms = self.classrooms.append(classroom)


class User:

    def __init__(self):
        self.name = ""
        self.email = ""
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_events(self):
        events = []
        return events
    def add_event(self, title, datetime):
        pass
    def remove_event(self, title):
        pass
class Student(User):
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Teacher(Student):
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Response:
    def __init__(self):
        self.author = User()
        self.body = ""
    def __init__(self, author, body):
        self.author = author
        self.body = body
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def get_body(self):
        return self.body
    def set_body(self, body):
        self.body = body

class Question(Response):
    def __init__(self):
        self.resolved = False
        self.author = User()
        self.body = ""
    def __init__(self, resolved, author, body):
        self.resolved = resolved
        self.author = author
        self.body = body
    def resolve(self, resolver):
        if self.author is resolver:
            self.resolved = True
class Answer(Response):
    def __init__(self):
        self.certified = False
        self.author = User()
        self.body = ""
    def __init__(self, certified, author, body):
        self.certified = certified
        self.author = author
        self.body = body
    def certify(self):
        self.certified = True
    #def certify(self, certifier):


class Classroom:
    def __init__(self):
        self.name = ""
        self.url = ""
        self.students = []
        self.teachers = []
    def __init__(self, name, url, students, teachers):
        self.name = name
        self.url = url
        self.students = students
        self.teachers = teachers
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_students(self):
        return self.students
    def set_students(self, students):
        self.students = students
    def get_teachers(self):
        return self.teachers
    def set_teachers(self, teachers):
        self.teachers = teachers
    def add_student(self, student):
        self.students = self.students.append(student)
    def add_teacher(self, teacher):
        self.teachers = self.teachers.append(teacher)
    def certify(self, teacher, answer):
        if teacher in self.get_teachers():
            answer.certify()
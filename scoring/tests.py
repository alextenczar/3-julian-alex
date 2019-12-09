from django.test import TestCase

from scoring.models.Judge_Assignment import Judge_Assignment
from scoring.models.Judge import Judge
from scoring.models.Student import Student
from scoring.models.Project import Project

class ProjectModel(TestCase):
    def test_stringrepresentation(self):
        pid = Project(project_id="Test Project")
        self.assertEqual(str(pid), pid.project_id)

class JudgeModel(TestCase):
    def test_stringrepresentation(self):
        jid = Judge(judge_id="Test Judge")
        self.assertEqual(str(jid), jid.judge_id)

class StudentModel(TestCase):
    def test_stringrepresentation(self):
        sid = Judge(id="Test Student")
        self.assertEqual(str(sid), sid.id)

class JAModel(TestCase):
    def test_stringrepresentation(self):
        jaid = Judge(ja_id="Test Student")
        self.assertEqual(str(jaid), jaid.ja_id)

class SiteTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
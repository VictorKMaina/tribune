from django.test import TestCase
from .models import *

# Create your tests here.
class EditorTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.james = Editor(first_name = "James", last_name = "Muriuki", email = "james@moringaschool.com")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # Testing the save method
    def test_save_method(self):
        self.james.save()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Test the delete method
    def test_delete_method(self):
        self.james.save()
        self.james.delete()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)

    # Test the method for displaying all editor objects
    def test_all_editors_method(self):
        self.james.save()
        john = Editor.objects.create(first_name = "John", last_name = "Doe", email = "johndoe@example.com")

        editors = Editor.all_editors()
        print("Editors: ", editors)
        self.assertTrue(len(editors) > 0)

    def test_update_editor_method(self):
        self.james.save()
        self.james.update_editor("email", "james@example.com")

        self.assertNotEqual(self.james.email, "james@moringaschool.com")
        self.assertEqual(self.james.email, "james@example.com")

class tagsTestClass(TestCase):
    """
    Test class to test tags class properties
    """
    def setUp(self):
        self.tag1 = tags.objects.create(name = "tag1")

    def test_tags_instance(self):
        self.assertTrue(isinstance(self.tag1, tags))

    def test_new_tag(self):
        tags.new_tag("tag2")
        tag2 = tags.objects.filter(name = "tag2").first()

        self.assertEqual(tag2.name, "tag2")

class ArticleTestClass(TestCase):
    """
    Test class for testing Article class methods
    """
    def  setUp(self):
        self.john = Editor(first_name = "John", last_name = "Doe")
        self.john.save()

        self.new_tag = tags(name = "testing")
        self.new_tag.save()

        self.new_article = Article(title = "Article heading", post = "Article content", editor = self.john)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = "2017-03-17"
        date = dt.datetime.strptime(test_date, "%Y-%m-%d").date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 블로그 리스트를 가져와 정상적으로 페이지 로드를 확인함
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        # 페이지 타이블이 맞는지 확인
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')

        # Blog, About Me 라는 문구가 네이게이션 바에 있는지 확인
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 포스트가 하나도 없다면?
        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        ## 등등..

import unittest,os
import sys 
testdir = os.path.dirname(__file__)
srcdir = '../wrecon'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
print (os.path.abspath(os.path.join(testdir, srcdir)))
from wrecon import Tree
from wrecon import Wrecon

class Test(unittest.TestCase):

    #set from parameter
    URL_VALID='http://localhost'

    def test_main_is_remove_outliers_from_recursive_javascript(self):
        url_test2 = 'javascript://void(false);'
        parser = Wrecon.remove_outliers_from_recursive(self,url_test2)
        self.assertEqual(parser, False)
    
    def test_main_is_remove_outliers_from_recursive_none(self):
        url_test2 = None
        parser = Wrecon.remove_outliers_from_recursive(self,url_test2)
        self.assertEqual(parser, False)

    def test_simple_tree(self):
        c= Tree("test")
        self.assertEqual(c.data, "test", "Most be test")

    def test_tree_with_nodes(self):
        a= Tree("test")
        b= Tree("node")
        a.children = b
        self.assertEqual(a.children.data, "node", "Most be node")
    
    def test_main_valid_max_urls(self):
        argv1 = ['-u', self.URL_VALID, '-r', '1']
        self.parser = Wrecon.parse_args()
        parsed = self.parser.parse_args(argv1)
        self.assertEqual(parsed.max_urls, 1)

    def test_main_valid_default_max_urls(self):
        argv1 = ['-u', self.URL_VALID]
        self.parser = Wrecon.parse_args()
        parsed = self.parser.parse_args(argv1)
        self.assertEqual(parsed.max_urls, 1),

    def test_main_valid_url(self):
        argv1 = ['-u', self.URL_VALID, '-r', '1']
        self.parser = Wrecon.parse_args()
        parsed = self.parser.parse_args(argv1)
        self.assertEqual(parsed.url, self.URL_VALID)

    def test_main_is_fragment_identifier_true(self):
        url_test = 'http://localhost:8178/api-docs/#/'
        parser = Wrecon.is_fragment_identifier(self,url_test)
        self.assertEqual(parser, True)

    def test_main_is_fragment_identifier_false(self):
        url_test = 'http://localhost:8178/'
        parser = Wrecon.is_fragment_identifier(self,url_test)
        self.assertEqual(parser, False)

    def test_main_is_valid_url_true(self):
        url_test = 'http://localhost:8178/'
        parser = Wrecon.is_valid_url(self,url_test)
        self.assertEqual(parser, True)
    
    def test_main_double_html_false(self):
        url_test = 'https://www.dodododododododorning.comhttps://www.dodododododododorning.com/page-sitemap.xml'
        parser = Wrecon.is_valid_url(self,url_test)
        self.assertEqual(parser, False)
    
    def test_main_html_interno(self):
        url_test = 'http://sqoui0098xpt/reports/mobile'
        parser = Wrecon.is_valid_url(self,url_test)
        self.assertEqual(parser, True)
    
    def test_main_is_valid_url_false_http(self):
        url_test2 = 'httppppp://localhost:8178/'
        parser = Wrecon.is_valid_url(self,url_test2)
        self.assertEqual(parser, False)
    
    def test_main_is_valid_url_false_number(self):
        url_test2 = 'http://local1ost/'
        parser = Wrecon.is_valid_url(self,url_test2)
        self.assertEqual(parser, True)
    
    def test_main_is_valid_url_javascript(self):
        url_test2 = 'javascript:void(false);'
        parser = Wrecon.is_valid_url(self,url_test2)
        self.assertEqual(parser, False)

    def test_main_is_valid_url_none(self):
        url_test2 = None
        parser = Wrecon.is_valid_url(self,url_test2)
        self.assertEqual(parser, False)

    def test_request_valid(self):
        url_test2 = self.URL_VALID
        w=Wrecon()
        data = w.request_get(url_test2)
        self.assertEqual(data.status_code,200)

    def test_request_invalid_url(self):
        url_test2 = 'axxaxaxax'
        w=Wrecon()
        data = w.request_get(url_test2)
        self.assertEqual(data.status_code,400)
            
    def test_request_invalid_request(self):
        url_test2 = 'https://api.github.com/authorizations'
        w=Wrecon()
        data = w.request_get(url_test2)
        self.assertNotEqual(data.status_code,200)

    def test_outliers_true(self):
        url_test2 = self.URL_VALID
        w=Wrecon()
        data = w.remove_outliers_from_recursive(url_test2)
        self.assertEqual(data,True)

    def test_outliers_false(self):
        url_test3 = 'http://www.styleshout.com/'
        w=Wrecon()
        data2 = w.remove_outliers_from_recursive(url_test3)
        self.assertEqual(data2,False)
    
    def test_robots_true(self):
        url_test2 = self.URL_VALID
        w=Wrecon()
        data = w.robots(url_test2)
        self.assertEqual(len(data),9)
    
    def test_robots_true_only_robots(self):
        url_test2 = 'https://api.github.com/authorizations'
        w=Wrecon()
        data = w.robots(url_test2)
        self.assertEqual(len(data),1)

    def test_robots_no_itens(self):
        url_test2 = 'http://localhost:8178/api-docs/#/'
        w=Wrecon()
        data = w.robots(url_test2)
        self.assertEqual(len(data),0)   
   

    def test_start_r1(self):
        root = Tree(self.URL_VALID)
        w=Wrecon()
        root.children = w.start (root,1)
        self.assertEqual(len(root.children),37) 
    
    def test_start_r2(self):
       root = Tree(self.URL_VALID)
       w=Wrecon()
       root.children = w.start (root,2)
       self.assertEqual(len(root.children),28) 
    
    def test_request_invalid_cookie_None(self):
        url_test2 = None
        w=Wrecon()
        data = w.is_valid_cookie(url_test2)
        self.assertEqual(data,False)

    def test_request_invalid_cookie_short(self):
        url_test2 = 'as'
        w=Wrecon()
        data = w.is_valid_cookie(url_test2)
        self.assertEqual(data,False)
    
    def test_request_invalid_cookie_short_with_iqual(self):
        url_test2 = '=s'
        w=Wrecon()
        data = w.is_valid_cookie(url_test2)
        self.assertEqual(data,False)

    def test_request_invalid_cookie_large_string(self):
        url_test2 = 'aaaaaaaaaaaaaaaaaaaaaa'
        w=Wrecon()
        data = w.is_valid_cookie(url_test2)
        self.assertEqual(data,False)
    
    def test_request_invalid_cookie_valid(self):
        url_test2 = 'PHP=123'
        w=Wrecon()
        data = w.is_valid_cookie(url_test2)
        self.assertEqual(data,True)

    def test_main_is_capture_double(self):
        url_test = 'http://localhost:8178/api-docs/#/'
        href = '//testasdasdhaujs.com'
        result = 'https://testasdasdhaujs.com'
        w=Wrecon()
        parser = w.capture(url_test,href)
        self.assertEqual(parser, result)

    def test_main_is_capture_fragment_identifier_true(self):
        url_test = 'http://localhost:8178/api-docs'
        href = '#abrir'
        result = 'http://localhost:8178/api-docs/#abrir'
        w=Wrecon()
        parser = w.capture(url_test,href)
        self.assertEqual(parser, result)

    def test_main_is_capture_None_true(self):
        url_test = 'http://localhost:8178/api-docs/'
        href = None
        result = None
        w = Wrecon()
        parser = w.capture(url_test,href)
        self.assertEqual(parser, result)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Test.URL_VALID = sys.argv.pop()  
    unittest.main()
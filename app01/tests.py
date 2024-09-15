from django.test import TestCase

# Create your tests here.
import os
import django
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_bbs.settings')
    django.setup()
    # 测试文件的搭建
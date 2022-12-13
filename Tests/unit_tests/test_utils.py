"""
This file demonstrates writing tests using the unittest module.
"""

import django
from django.test import TestCase
from parameterized import parameterized
import os
import sys

"""
When we use Django, we have to tell it which settings we are using. We do this by using an environment variable, DJANGO_SETTINGS_MODULE. 
This is set in manage.py. We need to explicitly set it for tests to work with pytest.
"""

sys.path.append(os.path.join(os.getcwd(), 'Application'))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "python_webapp_django.settings"
)
django.setup()

from app.utils import bmi_calculator

class BmiCalculatorTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(BmiCalculatorTest, cls).setUpClass()

    @parameterized.expand({
        [1.6, 55, 21.48, '健康體位'],
        [1.77, 77, 24.58, '過重']
    })
    def test_bmi_result_normal(self):
        """Tests bmi result."""
        height = 1.6
        weight = 55
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 21.48)
        self.assertEqual(bmi_means, '健康體位')
    
    def test_bmi_result_light_heavy(self):
        """Tests bmi result."""
        height = 1.77
        weight = 90
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 28.73)
        self.assertEqual(bmi_means, '輕度肥胖')
    
    def test_bmi_result_middle_heavy(self):
        """Tests bmi result."""
        height = 1.77
        weight = 100
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 31.92)
        self.assertEqual(bmi_means, '中度肥胖')

    def test_bmi_result_high_heavy(self):
        """Tests bmi result."""
        height = 1.77
        weight = 110
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 35.11)
        self.assertEqual(bmi_means, '重度肥胖')
    
    def test_bmi_result_thin(self):
        """Tests bmi result."""
        height = 1.77
        weight = 54
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 17.24)
        self.assertEqual(bmi_means, '過輕')
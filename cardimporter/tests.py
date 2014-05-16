"""
This is a collection of tests for the cardimporter django app
"""

from django.test import TestCase
from ankiconverter import ankiToMarkDown

class ankiconverterTest(TestCase):
    """This is the ankiconverter testsuite"""


    def generic_wrap_test(self,htmltag,mdwrap):
        result = ankiToMarkDown("text<"+htmltag+">wraptext</"+htmltag+">text")
        expected = "text"+mdwrap+"wraptext"+mdwrap+"text"
        returnresult = (result == expected, result+"!="+expected)
        return returnresult

    def test_ankiconverter_basicbold(self):
        """Tests that text<b>wraptext</b>text gets converted to text**wraptext**text."""
        result = self.generic_wrap_test("b","**")
        self.assertTrue(result[0],result[1])

    def test_ankiconverter_basicitalics(self):
        """Tests that text<i>wraptext</i>text gets converted to text*wraptext*text."""
        result = self.generic_wrap_test("i","*")
        self.assertTrue(result[0],result[1])

    def test_ankiconverter_basicunderline(self):
        """Tests that text<u>wraptext</u>text gets converted to text_wraptext_text."""
        result = self.generic_wrap_test("u","_")
        self.assertTrue(result[0],result[1])

    def test_ankiconverter_basicsubtext(self):
        """Tests that text<sub>wraptext</sub>text gets converted to text~wraptext~text."""
        result = self.generic_wrap_test("sub","~")
        self.assertTrue(result[0],result[1])

    def test_ankiconverter_basicsuptext(self):
        """Tests that text<sup>wraptext</sup>text gets converted to text^wraptext^text."""
        result = self.generic_wrap_test("sup","^")
        self.assertTrue(result[0],result[1])

    def test_ankiconverter_nestedHtml(self):
        """Tests that text<b><i>italicbold</i></b>text get converted to text***italicbold***text"""
        result = ankiToMarkDown("text<b><i>italicbold</i></b>text")
        self.assertEqual(result,"text***italicbold***text")

    def test_ankiconverter_escapeText(self):
        """Tests that markdown tags get escaped when in html content"""
        result_u = ankiToMarkDown("text_wraptext_text")
        result_i = ankiToMarkDown("text*wraptext*text")
        result_b = ankiToMarkDown("text**wraptext**text")
        result_sub = ankiToMarkDown("text~wraptext~text")
        result_sup = ankiToMarkDown("text^wraptext^text")

        self.assertEquals(result_u,r"text\_wraptext\_text")
        self.assertEquals(result_i,r"text\*wraptext\*text")
        self.assertEquals(result_b,r"text\**wraptext\**text")
        self.assertEquals(result_sup,r"text\^wraptext\^text")
        self.assertEquals(result_sub,r"text\~wraptext\~text")

    def test_ankicoverter_donttouchmath(self):
        """Tests that [$$] and [$] content does not get escaped or converted"""
        expected = "te\_xt$$important_math^with*syntax$$te\*xt"
        expected_one = "te\_xt$important_math^with*syntax$te\*xt"
        result = ankiToMarkDown("te_xt[$$]important_math^with*syntax[/$$]te*xt")
        result_one = ankiToMarkDown("te_xt[$]important_math^with*syntax[/$]te*xt")

        self.assertEquals(result,expected)
        self.assertEquals(result_one,expected_one)

    def test_ankicoverter_donttouchmultiplemath(self):
        """Tests that multiple [$$] or [$] content does not get escaped or converted"""
        expected = "te\_xt$$important_math^with*syntax$$te\*xt$important_math^with*syntax$te\^xt"

        result = ankiToMarkDown("te_xt[$$]important_math^with*syntax[/$$]te*xt[$]important_math^with*syntax[/$]te^xt")

        self.assertEquals(result,expected)

    def test_ankiconverter_styleAttributeUnderline(self):
        """Tests that text<b style="text-decoration: underline">underlinebold</b>text gets converted
        to text_**underlinebold**_text"""
        expected = "text_**underlinebold**_text"

        result = ankiToMarkDown("""text<b style="text-decoration: underline">underlinebold</b>text""")

        self.assertEquals(result,expected)

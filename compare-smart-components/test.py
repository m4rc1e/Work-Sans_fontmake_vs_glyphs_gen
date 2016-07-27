'''Check if fontmake decomposes smart components.'''

import unittest
from fontTools.ttLib import TTFont


class TestDecompose(unittest.TestCase):

    def setUp(self):
        '''Load fonts generated from fontmake and from glyphsapp'''
        self.glyphsapp_smart_gen = TTFont('./glyphs_gen/instance_ttf/smartcomponentstest-Regular.ttf')
        self.fontmake_smart_gen = TTFont('./fontmake_gen/instance_ttf/smartcomponentstest-Regular.ttf')

    def test_smart_component_is_decomposed(self):
        '''fontmake should decompose smart components in the same manner as
        Glyphsapp. They should be outlines, not composites'''
        # Check glyphsapp's generated font contains outlines and not comps for glyph 'n'
        self.assertEqual(False, self.glyphsapp_smart_gen['glyf']['n'].isComposite())
        self.assertEqual(1, self.glyphsapp_smart_gen['glyf']['n'].numberOfContours)

        # Repeat assertions on font generated from fontmake
        self.assertEqual(False, self.fontmake_smart_gen['glyf']['uni006E'].isComposite(),
                         'Glyph is a component! it should be decomposed.')
        self.assertEqual(1, self.fontmake_smart_gen['glyf']['uni006E'].numberOfContours)


if __name__ == '__main__':
    with open('../test-results/compare_smart_components.txt', 'w') as report:
        runner = unittest.TextTestRunner(report)
        unittest.main(testRunner=runner)

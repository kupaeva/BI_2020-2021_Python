import unittest
from classes import Rna, Dna

class Test_classes(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.rna = Rna('AUGC')
        self.rna_a = Rna('A')
        self.rna_g = Rna('G')
        self.rna_empty = Rna('')
        self.dna = Dna('ATGC')
#reverse complement tests
    def test_rna_rc(self):
        self.rna_rc = self.rna.reverse_complement()
        self.assertEqual(self.rna_rc, 'GCAU')
    def test_rna_a_rc(self):
        self.rna_a_rc = self.rna_a.reverse_complement()
        self.assertEqual(self.rna_a_rc, 'U')
    def test_rna_empty_rc(self):
        self.rna_empty_rc = self.rna_empty.reverse_complement()
        self.assertEqual(self.rna_empty_rc, '')
    def test_dna_rc(self):
        self.dna_rc = self.dna.reverse_complement()
        self.assertEqual(self.dna_rc, 'GCAT')
# gc content tests
    def test_dna_gc_content(self):
        self.dna_gc_content = self.dna.gc_content()
        self.assertEqual(self.dna_gc_content, 0.5)
    def test_rna_gc_content(self):
        self.rna_gc_content = self.rna.gc_content()
        self.assertEqual(self.rna_gc_content, 0.5)
    def test_rna_a_gc_content(self):
        self.rna_a_gc_content = self.rna_a.gc_content()
        self.assertEqual(self.rna_a_gc_content, 0)
    def test_rna_g_gc_content(self):
        self.rna_g_gc_content = self.rna_g.gc_content()
        self.assertEqual(self.rna_g_gc_content, 1)
    def test_rna_empty_gc_content(self):
        self.rna_empty_gc_content = self.rna_empty.gc_content()
        self.assertEqual(self.rna_empty_gc_content, None)


if __name__ == '__main__':
    unittest.main()

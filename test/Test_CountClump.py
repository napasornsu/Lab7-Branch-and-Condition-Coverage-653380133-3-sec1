import unittest

from source.CountClump import CountClump


class Test_CountClump(unittest.TestCase):
    
    def test_TC01(self):
        # TC01: ลิสต์ว่าง
        nums = []
        expected_result = 0
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC02(self):
        # TC02: ลิสต์เป็น None
        nums = None
        expected_result = 0
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC03(self):
        # TC03: ลิสต์ที่มีความยาว 1
        nums = [1]
        expected_result = 0
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC04(self):
        # TC04: ลิสต์ที่ไม่มีคลัมป์
        nums = [1, 2, 3, 4, 5]
        expected_result = 0
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC05(self):
        # TC05: ลิสต์ที่มีคลัมป์เดียว
        nums = [1, 1, 2, 3]
        expected_result = 1
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC06(self):
        # TC06: ลิสต์ที่มีหลายคลัมป์
        nums = [1, 1, 2, 2, 3, 3]
        expected_result = 3
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC07(self):
        # TC07: ลิสต์ที่มีค่าเดียวกันทั้งลิสต์
        nums = [1, 1, 1, 1, 1]
        expected_result = 1
        self.assertEqual(CountClump.count_clumps(nums), expected_result)
        
    def test_TC08(self):
        # TC08: ลิสต์ที่มีหลายคลัมป์และค่าเดียวกันในลิสต์
        nums = [1, 1, 2, 3, 3, 4, 4, 4, 1]
        expected_result = 3
        self.assertEqual(CountClump.count_clumps(nums), expected_result)

if __name__ == '__main__':
    unittest.main()

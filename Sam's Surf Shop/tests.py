# Write your code below:
import surfshop
import unittest

class mySurfShopTests(unittest.TestCase):
  def setUp(self):
    self.cart=surfshop.ShoppingCart()
  def test_add_surfboards(self):
    for num in range(2,5):
      with self.subTest(num):
        self.assertEqual(self.cart.add_surfboards(num),f'Successfully added {num} surfboards to cart!')
        self.cart=surfshop.ShoppingCart()
  def test_adding_surfboards(self):
    self.assertEqual(self.cart.add_surfboards(2),'Successfully added 2 surfboards to cart!')
  #@unittest.skip
  def test_TooManyBoardsError(self):
    self.assertRaises(surfshop.TooManyBoardsError,self.cart.add_surfboards(5))
  
  def test_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()

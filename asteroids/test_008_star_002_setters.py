"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import star

class TestStarSetters( unittest.TestCase ):

    def setUp( self ):
        initial_x = 11
        initial_y = 22
        initial_dx = 0
        initial_dy = 0
        self.expected_rotation = 0
        self.expected_radius = 2
        self.expected_world_width = 600
        self.expected_world_height = 800
        self.expected_max_brightness = 255
        self.expected_min_brightness = 0
        self.expected_color = ( 255, 255, 255 )
        
        self.expected_dx = initial_dx
        self.expected_dy = initial_dy
        self.expected_x = initial_x
        self.expected_y = initial_y
        
        self.constructed_obj = star.Star( initial_x, initial_y, self.expected_world_width, self.expected_world_height )
        
        return

    def tearDown( self ):
        return

    def test001_SetsBrightness( self ):
        new_brightness = 111
        new_color = ( new_brightness, new_brightness, new_brightness )
        self.constructed_obj.setBrightness( new_brightness )
        self.assertEqual( self.constructed_obj.getBrightness( ), new_brightness )
        self.assertEqual( self.constructed_obj.getColor( ), new_color )
        return
    
    def test002_SetsLowBrightness( self ):
        new_brightness = 0
        new_color = ( new_brightness, new_brightness, new_brightness )
        self.constructed_obj.setBrightness( new_brightness )
        self.assertEqual( self.constructed_obj.getBrightness( ), new_brightness )
        self.assertEqual( self.constructed_obj.getColor( ), new_color )
        return
    
    def test003_SetsHighBrightness( self ):
        new_brightness = 255
        new_color = ( new_brightness, new_brightness, new_brightness )
        self.constructed_obj.setBrightness( new_brightness )
        self.assertEqual( self.constructed_obj.getBrightness( ), new_brightness )
        self.assertEqual( self.constructed_obj.getColor( ), new_color )
        return
    
    def test004_DoesNotSetLowBrightness( self ):
        new_brightness = -1
        old_brightness = self.constructed_obj.getBrightness( )
        old_color = self.constructed_obj.getColor( )
        self.constructed_obj.setBrightness( new_brightness )
        self.assertEqual( self.constructed_obj.getBrightness( ), old_brightness )
        self.assertEqual( self.constructed_obj.getColor( ), old_color )
        return
    
    def test005_DoesNotSetHighBrightness( self ):
        new_brightness = 256
        old_brightness = self.constructed_obj.getBrightness( )
        old_color = self.constructed_obj.getColor( )
        self.constructed_obj.setBrightness( new_brightness )
        self.assertEqual( self.constructed_obj.getBrightness( ), old_brightness )
        self.assertEqual( self.constructed_obj.getColor( ), old_color )
        return
    
 
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestStarSetters )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )

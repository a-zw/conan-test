# conan-test

Testing Conan behavior


Package hierarchy in this test:


               [top]
                 |
         +-------+-------+
         |               |
         v               v
         |               |
     [mid_left]      [mid_right]
         |               |
    my_option=a      my_option=b
         |               |
         +-----+   +-----+
               |   |
               v   v
              [lower]



Run test.sh to see how conan handles this.

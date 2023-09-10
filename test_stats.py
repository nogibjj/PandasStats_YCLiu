import pandas as pd
import statsYC

# case1
# case1_l = [['Angel', 'F', 10], ['Nick', 'M', 15], ['John','M', 13],
#         ['Celine', 'F', 16], ['Greg', 'M', 8], ['Oliver','M', 13]]
  
# case1 = pd.DataFrame(case1_l, columns=['Name', 'Sex', 'Age'])
  
# case1.to_csv('TestCase1.csv', index = False)


#Functionality Test
def testStats():
    TestCase1 = pd.read_csv('TestCase1.csv', header = 0)
    assert statsYC.calMean(TestCase1, 'Age') == 12.5
    assert statsYC.calMedian(TestCase1, 'Age') == 13
    assert statsYC.countItemOcc(TestCase1, 'Sex', 'M') == 4
    assert statsYC.calItemRate(TestCase1, 'Sex', 'M') == (4*100)/6
    statsYC.printNumStats(TestCase1, 'Age')
    statsYC.printOccStats(TestCase1, 'Sex', 'M')
    pass

if __name__ == '__main__':
    testStats()
    pass

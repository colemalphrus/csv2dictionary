# timeconMT
A conversion from csv file to dictionary by Malphrus Tech

## Usage

### import
```python
from csv2dictionary.csvpro import CsvBrain
```
### use

#### data
```python
case1 = CsvBrain('test.csv')
case1.data
#returns a list of dictionaries
#the first line in the csv are the keys in the dictionaries
```

#### headers
```python
case1 = CsvBrain('test.csv')
case1.header_labels
#returns a list of Header labels
```

#### Search
```python
case1 = CsvBrain('test.csv')
case1.search('dog')
#returns a list of dict's that contain "dog" as a value under any key
```

#### castInt
```python
case1 = CsvBrain('test.csv')
case1.castInt('age')
#loops thru the list of dictionaries and changes cast all values under an 'age' key to integers
```
#### castInt
```python
case1 = CsvBrain('test.csv')
case1.castFloat('age')
#loops thru the list of dictionaries and changes cast all values under an 'age' key to Floats
```


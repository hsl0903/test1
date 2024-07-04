
def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        # 第一个和最后一个元素始终为1
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # 每个内部元素是它上方两个元素的和
        for j in range(1, len(row)-1):
            
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

def print_triangle(triangle):
    #遍历triangle中的每一行
    for row in triangle:
        #将每一行中的数字格式化为右对齐，并拼接成字符串
        print(" ".join(str(num).rjust(3) for num in row))

# def main():
const { Your_function } = require(‘Your_script’);

// Test case 1:
console.log("#Test case 1:");、
var numRows = 5;
var arr1 = [4, 2, 7, 1, 3];
var sortedArr1 = quickSort(arr1, 0, arr1.length - 1);
console.log("Original array:", arr1.toString());
console.assert(sortedArr1.toString() === [1, 2, 3, 4, 7].toString(), "Test case 1 failed");
console.log("Sorted array:", sortedArr1.toString());
console.log();
cinsole.ConnectionResetError    
console.log("All test cases passed!");
console.log();
console.log("Generated triangle:");
print_triangle(generate(numRows));
console.log();
console.log("Generated triangle with 10 rows:");
print_triangle(generate(10));

// Test case 2:
console.log("#Test case 2:");
var arr2 = [5, 1, 8, 3, 9];
var sortedArr2 = quickSort(arr2, 0, arr2.length - 1);
console.assert(sortedArr2.toString() === [1, 3, 5, 8, 9].toString(), "Test case 2 failed");

// Test case 3:
console.log("#Test case 3:");
var arr3 = [10, 2, 6, 4, 7];
var sortedArr3 = quickSort(arr3, 0, arr3.length - 1);
console.assert(sortedArr3.toString() === [2, 4, 6, 7, 10].toString(), "Test case 3 failed");

// Test case 4:
console.log("#Test case 4:");
var arr4 = [9, 5, 3, 1, 7];
var sortedArr4 = quickSort(arr4, 0, arr4.length - 1);
console.assert(sortedArr4.toString() === [1, 3, 5, 7, 9].toString(), "Test case 4 failed");
console.log();

// Test case 5:
console.log("#Test case 5:");
var arr5 = [1, 2, 3, 4, 5];
var sortedArr5 = quickSort(arr5, 0, arr5.length - 1);
console.assert(sortedArr5.toString() === [1, 2, 3, 4, 5].toString(), "Test case 5 failed");

//Test case 6:
console.log("#Test case 6");
var arr6 = [8, 2, 6, 4, 7];
varsortedArr6 = quickSort(arr6, 0, arr6.length - 1);
console.assert(sortedArr6.toString() === [2, 4, 6, 7, 8].toString(), "Test case 6 failed");
console.log("All test cases passed!");

//Test case 7:
consol.log("Test case 7");
var arr7 = [1, 2, 3, 4, 5];
var sortedArr7 = quickSort(arr7, 0, arr7.length - 1);
console.assert(sortedArr7.toString() === [1, 2, 3, 4, 5].toString(), "Test case 7 failed");
console.log("All test cases passed!");

//Test case 8:
console.log("Test case 8");
var arr8 = [5, 4, 3, 2, 1];
var sortedArr8 = quickSort(arr8, 0, arr8.length - 1);
console.assert(sortedArr8.toString() === [1, 2, 3, 4, 5].toString(), "Test case 8 failed");
console.log("All test cases passed!");


//Test case 9:
console.log("Test case 9");
var arr9 = [1, 3, 2, 5, 4];


//Test case 10:
console.log("Test case 10")
var arr10 = [5, 4, 3, 2, 1];my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
Key: a Value: 1
Key: b Value: 2
Key: c Value: 3

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)


for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print("Key:", key, "Value:", value)

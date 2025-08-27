from analyze_time import analyze_time, plot_results, pretty_time

@analyze_time()
def bubble_sort(arr : list): # Import!!! Type hints must be used
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@analyze_time(sizes=[10000, 20000, 40000, 80000, 160000])
def reverse_string(string : str):
    return string[::-1]

@analyze_time(sizes=[50, 100, 200, 400, 800])
def count_palindromic_substrings(text: str) :
    count = 0
    n = len(text)
    
    for i in range(n):           # O(n) outer loop
        for j in range(i, n):    # O(n) inner loop  
            substring = text[i:j+1]
            if substring == substring[::-1]:  # palindrome check
                count += 1
    
    return count

if __name__ == "__main__":

    # Bubble Sort - Test
    results_bubble_sort = bubble_sort.analyze_complexity()
    for size, time in results_bubble_sort:
        print("Input size: ", size, "Time Taken: ", pretty_time(time) , "MS")
    plot_results(results_bubble_sort)   

    # Reverse String - Test : O(n)
    # results_reverse_string = reverse_string.analyze_complexity()
    # for size, time in results_reverse_string:
    #     print("Input size: ", size, "Time Taken: ", pretty_time(time) , "MS")
    # plot_results(results_reverse_string)

    # Count Palindromic Substrig - Test : O(n^2)
    # results_pali_string = count_palindromic_substrings.analyze_complexity()
    # for size, time in results_pali_string:
    #     print("Input size: ", size, "Time Taken: ", pretty_time(time) , "MS")
    # plot_results(results_pali_string)

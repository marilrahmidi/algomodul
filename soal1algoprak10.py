def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1 
    
    return -1  

def search_element(arr, target):
    
    arr.sort() 
    print("List setelah diurutkan:", arr)
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Elemen {target} ditemukan pada indeks {result}.")
    else:
        print(f"Elemen {target} tidak ditemukan dalam list.")

arr = [2, 15, 23, 28, 31, 34, 56, 87, 89, 200]
target = 23
search_element(arr, target)

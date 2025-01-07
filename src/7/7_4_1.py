import concurrent.futures

def square(n):
    return n*n

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(square, range(100)))
    print(results)

if __name__ == "__main__":
    main()
